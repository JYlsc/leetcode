#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 11:39
# @Author  : Leishichi
# @File    : 20.py
# @Software: PyCharm
# @Tag:

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for char in s:
            if char in dict:
                stack.append(char)
            elif not stack or char != dict[stack.pop()]:
                return False
        return not stack
