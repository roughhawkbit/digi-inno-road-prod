import os
from huggingface_hub.utils import _runtime

HF_USE_TOKEN = False

def bypass_hf_hub_xet_download():
    os.environ["HF_HUB_DISABLE_XET"] = "1"
    os.environ["HF_HUB_DOWNLOAD_TIMEOUT"] = "60"
    os.environ["HF_HUB_ETAG_TIMEOUT"] = "15"
    _runtime._is_google_colab = False
