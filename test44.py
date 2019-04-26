#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as ny
from numpy import *

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9],
     [1, 2, 3]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

x_row = ny.size(X, 0)  # X行数
x_col = ny.size(X, 1)  # X列数
y_row = ny.size(Y, 0)  # Y行数
y_col = ny.size(Y, 1)  # Y列数

result = zeros((x_row, y_col))

result_temp = 0
if x_col != y_row:
    print('数据错误')
else:
    for r in range(y_col):
        for m in range(x_row):
            for n in range(y_col):
                result_temp += X[m][n] * Y[n][r]
            result[m][r] = result_temp
            result_temp = 0


print(result)
