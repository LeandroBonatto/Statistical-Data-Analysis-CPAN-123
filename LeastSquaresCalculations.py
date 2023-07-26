import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_frame_x = pd.read_csv('data_x.csv', header=None)
data_frame_y = pd.read_csv('data_y.csv', header=None)
data_x = np.array(data_frame_x).ravel()
data_y = np.array(data_frame_y).ravel()
x_mean = np.mean(data_x)
x_std_dev = np.std(data_x, ddof=1)

y_mean = np.mean(data_y)
y_std_dev = np.std(data_y, ddof=1)

SS_xx = np.dot(a=(data_x - x_mean), b=(data_x - x_mean))
SS_xy = np.dot(a=(data_x - x_mean), b=(data_y - y_mean))
SS_yy = np.dot(a=(data_y - y_mean), b=(data_y - y_mean))

Beta1 = SS_xy / SS_xx
Beta0 = y_mean - Beta1 * x_mean

SSE = np.dot(data_y - (Beta0 + Beta1 * data_x), data_y - (Beta0 + Beta1 * data_x))

s2 = SSE / (len(data_x) - 2)
s = np.sqrt(SSE / (len(data_x) - 2))

s_beta1 = s / np.sqrt(SS_xx)
t_c = Beta1 / s_beta1

r = SS_xy / math.sqrt(SS_xx * SS_yy)
r_2 = r ** 2

print('*******************************************')
print('x_mean = {:.4f}'.format(x_mean))
print('x_variance = {:.4f}'.format(x_std_dev ** 2))
print('x_std_dev = {:.4f}'.format(x_std_dev))
print('*******************************************')
print('y_mean = {:.4f}'.format(y_mean))
print('y_variance = {:.4f}'.format(y_std_dev ** 2))
print('y_std_dev = {:.4f}'.format(y_std_dev))
print('*******************************************')
print('SS_xx = {:.4f}'.format(SS_xx))
print('SS_xy = {:.4f}'.format(SS_xy))
print('SS_yy = {:.4f}'.format(SS_yy))
print('*******************************************')
print('Model: y = {:.4f} + {:.4f}x'.format(Beta0, Beta1))
print('*******************************************')
print('SSE = {:.4f}'.format(SSE))
print('*******************************************')
print('s^2 = {:.4f}'.format(s2))
print('s = {:.4f}'.format(s))
print('*******************************************')
print('s_beta1 = {:.4f}'.format(s_beta1))
print('t_c = {:.4f}'.format(t_c))
print('*******************************************')
print('r = {:.4f}'.format(r))
print('r^2 = {:.4f}'.format(r_2))
print('*******************************************')

print('>>> END <<<')

plt.scatter(data_x, data_y, c='orange')
x_range = np.linspace(start=data_x.min(), stop=data_x.max(), endpoint=True, num=100)
plt.xticks(font='Times New Roman', fontsize=16)
plt.yticks(font='Times New Roman', fontsize=16)
plt.plot(x_range, Beta0 + Beta1 * x_range)
plt.savefig('LinearRegressionModel.png', format='png', dpi=1200)
plt.show()

print('>>> END <<<')
