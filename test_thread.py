#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from threading import Thread
import time


def fun1(x, y):
    for i in range(x, y):
        print(i, end='')
    print()
    print(x, time.time())
    time.sleep(10)
    print(x, time.time())


t1 = Thread(target=fun1, args=(15, 20))
t1.start()
t1.join(1)
t2 = Thread(target=fun1, args=(5, 10))
t2.start()
