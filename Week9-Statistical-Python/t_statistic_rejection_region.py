from scipy import stats

form = input('Please enter the alternative hypothesis form\n(two-tailed, upper-tailed, or lower-tailed): ')
alpha = float(input('Please enter the type I error, level of significance (\u03B1): '))
df = int(input('Please enter degree of freedom: '))

if form == 'lower-tailed':
    print('Rejection Region t < {:.3f}'.format(stats.t.ppf(alpha, df)))
elif form == 'upper-tailed':
    print('Rejection Region t > {:.3f}'.format(stats.t.ppf(1 - alpha, df)))
elif form == 'two-tailed':
    print('Rejection Region t < {:.3f} or t > {:.3f}'.format(stats.t.ppf(alpha / 2, df), stats.t.ppf(1 - alpha / 2, df)))
else:
    print(form, 'is invalid form. The valid forms are two-tailed, upper-tailed, or lower-tailed')
