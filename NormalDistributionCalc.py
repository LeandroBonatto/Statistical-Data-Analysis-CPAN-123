import scipy
from scipy import stats

mu = float(input('Please Enter the Mean: '))
sigma = float(input('Please Enter the Standard Deviation: '))

x1 = float(input('Please Enter the lower  number: '))
x2 = float(input('Please Enter the higher number: '))

cdf1 = scipy.stats.norm.cdf(x1, mu, sigma)
cdf2 = scipy.stats.norm.cdf(x2, mu, sigma)

print('P({:.4f} < x < {:.4f}) = {:.4f}'.format(x1, x2, cdf2 - cdf1))
