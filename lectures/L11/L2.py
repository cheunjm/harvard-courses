import numpy as np

def L2(v, *args):
    """Compute the weighted L2 norm.
    
    INPUTS
    =======
    v: a list of floats
    args: a list of variable input arguments
       args[0]: a list of weights, floats
    
    RETURNS
    ========
    s: the weighted L2 norm of the input v

    NOTES
    =====
    PRE: 
         - v is a list of floats
         - the weights are stored in args[0]
    POST:
         - a, b, and c are not changed by this function
         - raises a ValueError exception if len(v) .ne. len(args[0])
         - returns a float

    EXAMPLES
    =========
    >>> L2([3.0, 4.0], [1.0, 2.0])
    8.54400374531753
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
