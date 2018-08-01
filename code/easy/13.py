#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 10:28
# @Author  : Leishichi
# @File    : 13.py
# @Software: PyCharm
# @Tag:

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        tmp = 0
        for i in reversed(s):
            value = dic[i]
            if value < tmp:
                result-=value
            else:
                result+=value
            tmp = value
        return result


s = Solution()
print(s.romanToInt('MCMXCIV'))
print("hello")
