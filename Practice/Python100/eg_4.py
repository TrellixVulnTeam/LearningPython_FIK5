#!/usr/bin/env python
# -*- coding: UTF-8 -*-
############################################################
#  Created on: 2017-12-26
#  Author: Joe Aaron
#  Email:  pant333@163.com
#  Description:  输入某年某月某日，判断这一天是这一年的第几天？
############################################################
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print 'data error'
sum += day
leap = 0
leap = 0
if(year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    leap = 1
if(leap == 1) and (month > 2) :
    sum += 1

print 'it is the %dth day.' % sum
