from scipy import stats


form = input('Please enter the alternative hypothesis form\n(two-tailed, upper-tailed, or lower-tailed): ')
alpha = float(input('Please enter the type I error, level of significance (\u03B1): '))

if form == 'lower-tailed':
    print('Rejection Region z < {:.9f}'.format(stats.norm.ppf(alpha)))
elif form == 'upper-tailed':
    print('Rejection Region z > {:.9f}'.format(stats.norm.ppf(1 - alpha)))
elif form == 'two-tailed':
    print('Rejection Region z < {:.9f} or z > {:.9f}'.format(stats.norm.ppf(alpha / 2), stats.norm.ppf(1 - alpha / 2)))
else:
    print(form, 'is invalid form. The valid forms are two-tailed, upper-tailed, or lower-tailed')
