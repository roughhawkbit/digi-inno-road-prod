from .env_tools import is_in_google_colab

import numpy
import random
import transformers

if is_in_google_colab():
    import torch # type: ignore


def set_all_random_seeds(seed):
    # This is quite possibly overkill, since transformers.set_seed(seed) should
    # set the seed for both numpy and random, but no harm in making sure.
    random.seed(seed)
    numpy.random.seed(seed)
    transformers.set_seed(seed)
    if is_in_google_colab():
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
