
import numpy as np

def L2(v, *args):
    """Computes the L2 norm of a vector
    
    INPUTS
    ========
    v: list, required
       List of numbers
    args: list, optional
       A vector of weights. Must have the same length as the
       input vector
          
    RETURNS
    ========
    L2 norm: float
       A ValueError exception is raised if the dimension of the weights
       and the vector does not match
    
    EXAMPLES
    ========
    >>> L2([3,4])
    5.0
    """
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)