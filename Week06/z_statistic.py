from scipy import stats

mu = 0
sigma = 1

confidence_level = float(input('Please enter confidence level: '))

print('z_{:.3f} = {:.3f}'.format((100 - confidence_level) / 200, stats.norm.ppf(0.50 + confidence_level / 200, mu, sigma)))
