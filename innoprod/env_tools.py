import torch

def is_in_google_colab():
    try:
        import google.colab  # type: ignore
        return True
    except ImportError:
        return False
    

def cuda_device():
    """
    Returns the appropriate device for PyTorch computations.
    If a GPU is available, it returns 'cuda', otherwise 'cpu'.
    """
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")
