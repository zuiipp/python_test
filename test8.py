#!/usr/bin/env python 
# -*- coding:utf-8 -*-

for colum in range(1, 10):
    print()
    for row in range(1, colum+1):
        print('%d * %d = %d' % (colum, row, row * colum), end='   ')
        # if row == colum:
        #     print()



###########

