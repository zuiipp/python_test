#!/usr/bin/env python 
# -*- coding:utf-8 -*-


num_arry = [0]
delta_arry = [0]

i = 1
while True:
    num = i * i
    num_arry.append(num)
    length = len(num_arry)
    flag = 0
    for j in range(1, length):
        delta_num = num_arry[length-1] - num_arry[j-1]
        if delta_num == 168:
            x = (num - 268)
            print('x = %d' % x)
            flag = 1
            break
    if i > 100:
        print(num_arry)
        break
    i += 1






