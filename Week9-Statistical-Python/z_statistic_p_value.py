from scipy import stats
import math

# h0 = float(input('Please enter H\u2080 value: '))
form = input('Please enter the alternative hypothesis form\n(two-tailed, upper-tailed, or lower-tailed): ')
# alpha = float(input('Please enter the type I error (\u03B1): '))
z = float(input('Please enter the z value: '))

if form == 'lower-tailed':
    print('p-value = P(z < {:.9f}) = {:.9f}'.format(z, stats.norm.cdf(z)))
elif form == 'upper-tailed':
    print('p-value = P(z > {:.9f}) = {:.9f}'.format(z, 1 - stats.norm.cdf(z)))
elif form == 'two-tailed':
    print('p-value = P(z < {:.9f} or z > {:.9f}) = {:.9f}'.format(-math.fabs(z), math.fabs(z), 2 * stats.norm.cdf(-math.fabs(z))))
else:
    print(form, 'is invalid form. The valid forms are two-tailed, upper-tailed, or lower-tailed')
