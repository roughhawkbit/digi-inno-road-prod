import numpy as np

def rand_jitter(arr, stdev=None):
    if stdev is None:
        stdev = .01 * (max(arr) - min(arr))
    r = np.random.randn(len(arr),1)
    r = r * stdev
    return arr.astype('float') + r
