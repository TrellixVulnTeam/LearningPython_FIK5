#!/usr/bin/env python
# -*- coding: UTF-8 -*-
############################################################
#  Created on: 2017-12-26
#  Author: Joe Aaron
#  Email:  pant333@163.com
#  Description:  输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
############################################################
import string

s = raw_input('input a string:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1

print 'char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others)
