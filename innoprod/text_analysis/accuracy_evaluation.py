import torch

from ..env_tools import cuda_device

def evaluate_ordinal_metrics(predictions, targets):
    """
    Calculates Exact Accuracy, Adjacent Accuracy, and MAE for an ordinal scale.
    """
    # 1. Round predictions to nearest integer
    rounded_preds = torch.round(predictions)

    # 2. Clamp predictions to the valid ordinal range (1 to 9)
    clamped_preds = torch.clamp(rounded_preds, min=1.0, max=9.0)

    # Ensure targets are float for math operations, but conceptually they are integers
    targets = targets.float()

    # 3. Calculate Exact Match Accuracy
    exact_matches = (clamped_preds == targets).sum().item()
    exact_accuracy = exact_matches / len(targets)

    # 4. Calculate Adjacent (Within-1) Accuracy
    absolute_differences = torch.abs(clamped_preds - targets)
    adjacent_matches = (absolute_differences <= 1).sum().item()
    adjacent_accuracy = adjacent_matches / len(targets)

    # 5. Calculate Mean Absolute Error (MAE)
    mae = absolute_differences.mean().item()

    return exact_accuracy, adjacent_accuracy, mae


def validate(model, val_loader):
  device = cuda_device()
  model.eval()
  all_preds = []
  all_targets = []

  with torch.no_grad():
    i = 1
    for input_ids, attention_mask, labels in val_loader:
      i += 1
      input_ids = input_ids.to(device)
      attention_mask = attention_mask.to(device)
      logits, _ = model(input_ids, attention_mask)
      all_preds.append(logits.squeeze())
      all_targets.append(labels)

  all_preds_tensor = torch.cat(all_preds)
  all_targets_tensor = torch.cat(all_targets)
  all_preds_tensor = all_preds_tensor.to(device)
  all_targets_tensor = all_targets_tensor.to(device)
  return evaluate_ordinal_metrics(all_preds_tensor, all_targets_tensor)