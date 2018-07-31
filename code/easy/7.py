#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 11:38
# @Author  : Leishichi
# @File    : 7.py
# @Software: PyCharm
# @Tag:

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1,-1][x<0]
        abs_x = abs(x)
        res_x = 0
        while abs_x > 0:
            res_x *= 10
            res_x += abs_x % 10
            abs_x //= 10
        return sign*res_x if -2**31<sign*res_x<2**31-1 else 0