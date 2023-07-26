from scipy import stats

confidence_level = float(input('Please enter confidence level: '))
df = int(input('Please enter degree of freedom: '))

print('t_{:.3f} = {:.3f}'.format((100 - confidence_level) / 200, stats.t.ppf(0.50 + confidence_level / 200, df)))
