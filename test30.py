#!/usr/bin/env python 
# -*- coding:utf-8 -*-

s = input('输入5位数：')
l_s = len(s)
flag = 1
for i in range(int(l_s/2)):
    if s[i] != s[l_s-i-1]:
        flag = 0
        break

if flag == 1:
    print('是回文数字')
else:
    print('不是回文数字')
