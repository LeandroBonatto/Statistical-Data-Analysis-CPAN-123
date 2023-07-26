from scipy import stats
import math

form = input('Please enter the alternative hypothesis form\n(two-tailed, upper-tailed, or lower-tailed): ')
t = float(input('Please enter the t value: '))
df = int(input('Please enter degree of freedom: '))

if form == 'lower-tailed':
    print('p-value = P(t < {:.4f}) = {:.7f}'.format(t, stats.t.cdf(t, df)))
elif form == 'upper-tailed':
    print('p-value = P(t > {:.4f}) = {:.7f}'.format(t, 1 - stats.t.cdf(t, df)))
elif form == 'two-tailed':
    print('p-value = P(t < {:.4f} or t > {:.4f}) = {:.7f}'.format(-math.fabs(t), math.fabs(t), 2 * stats.t.cdf(-math.fabs(t), df)))
else:
    print(form, 'is invalid form. The valid forms are two-tailed, upper-tailed, or lower-tailed')
