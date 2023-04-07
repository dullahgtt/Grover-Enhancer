import numpy as np

def softmax(x):
    """Compute softmax values for each row of x."""
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)
