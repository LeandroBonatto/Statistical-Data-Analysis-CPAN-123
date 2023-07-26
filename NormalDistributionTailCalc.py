import scipy
from scipy import stats

mu = float(input('Please Enter the Mean: '))
sigma = float(input('Please Enter the Standard Deviation: '))

x = float(input('Please Enter the number: '))
low_high = input('Please Enter low or high: ')

cdf = scipy.stats.norm.cdf(x, mu, sigma)

if low_high == 'low':
    print('P(x < {:.4f}) = {:.4f}'.format(x, cdf))
elif low_high == 'high':
    print('P({:.4f} < x) = {:.4f}'.format(x, 1 - cdf))
