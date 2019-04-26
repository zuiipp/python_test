#!/usr/bin/env python 
# -*- coding:utf-8 -*-

for num in range(100,1000):
    i = int(num / 100)
    j = int((num - i * 100) / 10)
    k = int(num - i * 100 - j * 10)
    if (i**3 + j**3 + k**3) == num:
        print(num)
