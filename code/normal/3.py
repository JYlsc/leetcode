#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 22:13
# @Author  : Leishichi
# @File    : 3.py
# @Software: PyCharm
# @Tag:


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        tmp = -1
        map = {}
        for i in range(len(s)):
            c = s[i]
            if c in map.keys():
                # 获取上次该元素存在的位置
                tmp = max(map[c],tmp)
            map[c] = i
            result = max(result, i - tmp)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abba"))
