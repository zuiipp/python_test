#!/usr/bin/env python 
# -*- coding:utf-8 -*-

s = input('输入5个字符')

l_s = len(s)
# for i in range(l_s):
#     t = s[l_s-i-1]
#     print(t)


def func(string_s, length):
    if length == 0:
        return
    print(string_s[length-1])
    func(string_s, length-1)


func(s, l_s)
