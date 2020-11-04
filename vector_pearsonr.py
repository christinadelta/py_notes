# vector pearson correlation
# based on scipy.stats.pearsonr and NumPy vectorized correlation coefficient by John Herman

# Author: ChristinaDelta
# September 2020

# TODO: return p-value

import numpy as np
import scipy
from scipy import stats

# define ss function (scipy has
def ss(data, axis):
    return np.sum(data * data, axis=axis)

# define pearson r function
def pearsonr_vector(X, y):

    '''
    inputs:
    X = matrix N x k
    y = vector 1 x k

    output:
    correlation coefficients of X and y

    if X and y are not np arrays:
        X = np.asarray(X)
        y = np.asarray(y)
    '''

    meanX = X.mean(axis=-1)
    meany = y.mean(axis=-1)

    Xmean, ymean = X - meanX[..., None], y - meany[..., None]
    r_num = np.add.reduce(Xmean * ymean, axis=-1)
    r_den = np.sqrt(ss(Xmean, axis=-1) * ss(ymean, axis=-1))

    return r_num / r_den
