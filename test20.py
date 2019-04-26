#!/usr/bin/env python 
# -*- coding:utf-8 -*-

h = 100.0
sum_h = 0
for i in range(1, 11):
    sum_h += h
    h = h / 2.0


print('共经过%f米' % (sum_h*2+100))
print('第10次反弹%f米' % h)
