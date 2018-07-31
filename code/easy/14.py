#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 11:25
# @Author  : Leishichi
# @File    : 14.py
# @Software: PyCharm
# @Tag:

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            str2 = strs[i]
            tmp = ""
            for j in range(min(len(prefix), len(str2))):
                if prefix[j] == str2[j]:
                    tmp += prefix[j]
                else:
                    break
            prefix = tmp

        return prefix


s = Solution()
print(s.longestCommonPrefix([]))
