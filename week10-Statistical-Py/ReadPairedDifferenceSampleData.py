import pandas as pd

df1 = pd.read_csv('data1.csv', header=None)
df2 = pd.read_csv('data2.csv', header=None)
df = df1 - df2
df.to_csv('data_difference.csv', index=False, header=False)
sample_mean = df.mean()[0]
sample_std_dev = df.std()[0]

print('Sample Mean = {:.4f}'.format(sample_mean))
print('Sample Variance = {:.4f}'.format(sample_std_dev ** 2))
print('Sample Standard Deviation = {:.4f}'.format(sample_std_dev))

print('>>> END <<<')
