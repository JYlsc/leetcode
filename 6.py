#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 18:25
# @Author  : Leishichi
# @File    : 6.py
# @Software: PyCharm
# @Tag:

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ""

        str_list = ["" for _ in range(numRows)]

        index = 0
        rows = 0
        while index < len(s):
            if (numRows % 2 == 1) and (rows % 2 == 1):
                str_list[int(numRows / 2)] += s[index]
                index += 1
                rows += 1
            else:
                for j in range(numRows):
                    str_list[j] += s[index]
                    index += 1
                    if index >= len(s):
                        break
                rows += 1

        for x in str_list:
            result += x
        return result


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print("PAHNAPLSIIGYIR")

print(s.convert("ABCD", 2))
print("ACBD")


print(s.convert("ABCDE", 4))
print("ABCED")

