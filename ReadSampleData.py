import numpy as np
import pandas as pd
import statistics as stat

data_frame = pd.read_csv('data.csv', header=None)
data = np.array(data_frame)
sample_mean = np.mean(data)
sample_std_dev = np.std(data, ddof=1)

print('Sample Mean = {:.4f}'.format(sample_mean))
print('Sample Standard Deviation = {:.4f}'.format(sample_std_dev))

print('>>> END <<<')
