#!/usr/bin/env python 
# -*- coding:utf-8 -*-

n = int(input('输入数字：'))
m = int(input('输入位数：'))

a = 0
sum_num = 0
for i in range(0, m):
    a += n * (10**i)
    print(a)
    sum_num += a

print(sum_num)

