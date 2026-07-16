from peft import get_peft_model, LoraConfig, TaskType
import torch
from transformers import BertModel

from .document_attention import DocumentAttention
from .huggingface_config import HF_USE_TOKEN

class HANBERTLora(torch.nn.Module):
    """
    End-to-end Hierarchical Attention Network over a LoRA-adapted BERT-large.
    """
    def __init__(self, num_classes=1, model_name='bert-base-uncased'):
        super().__init__()

        # 1. Load the frozen base BERT model
        base_model = BertModel.from_pretrained(model_name, token=HF_USE_TOKEN)

        # 2. Configure and apply LoRA
        lora_config = LoraConfig(
            task_type=TaskType.FEATURE_EXTRACTION,
            r=lora_rank,
            lora_alpha=lora_alpha,
            target_modules=["query", "value"],
            lora_dropout=lora_dropout,
            bias="none"
        )
        # get_peft_model automatically freezes the base model and injects LoRA adapters
        self.bert = get_peft_model(base_model, lora_config)

        hidden_size = base_model.config.hidden_size # 1024 for BERT-large

        # 3. Initialize Firm-Level Attention
        self.document_attention = DocumentAttention(hidden_size)

        # 4. Final Head (Regression for continuous score, or Classification for discrete)
        # Using num_classes=1 implies a regression task for the Digital Readiness Score
        self.classifier = torch.nn.Linear(hidden_size, num_classes)

        self.to(DEVICE)

    def load_checkpoint_state(self, checkpoint_path):
        trainable_state_dict = torch.load(checkpoint_path, map_location=DEVICE)
        self.load_state_dict(trainable_state_dict, strict=False)
        self.eval()
        print(f"Checkpoint loaded from {checkpoint_path}")
      

    def forward(self, input_ids, attention_mask):
        # Expected Input Shapes: (batch_size, num_questions, sequence_length)
        batch_size, num_questions, seq_len = input_ids.size()

        # Flatten the batch and question dimensions to process through BERT
        # New shape: (batch_size * num_questions, sequence_length)
        flat_input_ids = input_ids.view(-1, seq_len)
        flat_attention_mask = attention_mask.view(-1, seq_len)

        # Pass through the LoRA-adapted BERT
        outputs = self.bert(
            input_ids=flat_input_ids,
            attention_mask=flat_attention_mask
        )

        # Extract the [CLS] token embeddings
        # Shape: (batch_size * num_questions, hidden_size)
        cls_embeddings = outputs.last_hidden_state[:, 0, :]

        # Reshape back to group embeddings by firm
        # Shape: (batch_size, num_questions, hidden_size)
        reshaped_embeddings = cls_embeddings.view(batch_size, num_questions, -1)

        # Apply the document-level attention
        aggregated_representation, att_weights = self.document_attention(reshaped_embeddings)

        # Generate the final readiness score prediction
        logits = self.classifier(aggregated_representation)

        # Returning attention weights is highly recommended for academic research
        # as it allows you to explain *which* questions drove the prediction.
        return logits, att_weights

    def save(self, filepath):
      trainable_state_dict = {
          name: param.cpu()
          for name, param in self.named_parameters() 
          if param.requires_grad
      }
      torch.save(trainable_state_dict, filepath)
      print(f"Efficient checkpoint saved to {filepath} (~3-4MB)")
