#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 09:54
# @Author  : Leishichi
# @File    : 9.py
# @Software: PyCharm
# @Tag:
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0) | ((x % 10 == 0) & (x != 0)):
            return False

        tmp = 0
        while True:
            tmp = tmp * 10 + x % 10
            x = x // 10
            if tmp >= x:
                break
        return (x == tmp) | (x == tmp // 10)


s = Solution()
print(s.isPalindrome(10))
