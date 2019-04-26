#!/usr/bin/env python 
# -*- coding:utf-8 -*-

s = input('请输入字符串：\n')

letter_num = 0
space_num = 0
digit_num = 0
others_num = 0

for n in s:
    if n.isalpha():
        letter_num += 1
    elif n.isspace():
        space_num += 1
    elif n.isdigit():
        digit_num += 1
    else:
        others_num += 1

print('字母个数：%d' % letter_num)
print('空格个数：%d' % space_num)
print('数字个数：%d' % digit_num)
print('其他个数：%d' % others_num)
