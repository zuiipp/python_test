#!/usr/bin/env python 
# -*- coding:utf-8 -*-

money = float(input("净利润:"))

money_level = [100, 60, 40, 20, 10, 0]
bonus_rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

bonus = 0.0
for i in range(0, 6):
    if money > money_level[i]:
        bonus += (money - money_level[i]) * bonus_rat[i]
        print((money - money_level[i]) * bonus_rat[i])
        money = money_level[i]


print('奖金：%f' %bonus)

