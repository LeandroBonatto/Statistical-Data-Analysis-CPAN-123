import scipy
from scipy import stats

mu = float(input('Please Enter the Mean: '))
sigma = float(input('Please Enter the Standard Deviation: '))

p = float(input('Please Enter the percentile: '))

ppf = scipy.stats.norm.ppf(p / 100, mu, sigma)

print('P(x < {:.4f}) = {:.2f}'.format(ppf, p))
