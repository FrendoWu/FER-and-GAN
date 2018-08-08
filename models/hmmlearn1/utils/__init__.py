import numpy as np
import sklearn

def normalize(A, axis=None):
    """Normalize the input array so that it sums to 1.

    Parameters
    ----------
    A: array, shape (n_samples, n_features)
        Non-normalized input data.
    axis: int
        Dimension along which normalization is performed.

    Returns
    -------
    normalized_A: array, shape (n_samples, n_features)
        A with values normalized (summing to 1) along the prescribed axis

    WARNING: Modifies the array inplace.
    """
    #print "before normalize", A
    A += np.finfo(float).eps
    A[np.isnan(A)] = 0.0
    Asum = A.sum(axis)
    if axis and A.ndim > 1:
        # Make sure we don't divide by zero.
        Asum[Asum == 0] = 1
        shape = list(A.shape)
        shape[axis] = 1
        Asum.shape = shape
    # print 'A', A
    # print 'Asum', Asum
    # print type(Asum)
    # print type(Asum) != numpy.float64
    # if type(Asum) != numpy.float64:
    #     for i, j in enumerate(Asum):
    #         if np.isnan(j):
    #             Asum[i] = 1.0
    A /= Asum
    # TODO: should return nothing, since the operation is inplace.
    #print("after normalize", A)
    return A
