#!/usr/bin/env python 
# -*- coding:utf-8 -*-

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                a = i*100 + j*10 +k
                print(a)


