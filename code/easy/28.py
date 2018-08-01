#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 17:57
# @Author  : Leishichi
# @File    : 28.py
# @Software: PyCharm
# @Tag:

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        KMP 算法
        """
        if needle == "":
            return 0
        next = self.KMP(needle)
        i = 0
        j = 0

        while (i < len(haystack)):
            if (j == -1) | (haystack[i] == needle[j]):
                i += 1
                j += 1
            else:
                j = next[j]

            if (j == len(needle)):
                return i - j

        return -1

    def KMP(self, str):
        length = len(str)
        next = list(range(length))
        next[0] = -1
        i = 0
        j = -1
        while True:
            if (j == -1) | (str[i] == str[j]):
                i += 1
                j += 1
                if i == length:
                    break
                next[i] = j
            else:
                j = next[j]
        return next


s = Solution()
print(s.strStr("aaaaa", "bba"))
