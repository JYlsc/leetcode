#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 10:38
# @Author  : Leishichi
# @File    : 12.py
# @Software: PyCharm
# @Tag:
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        symbols = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

        position = 1

        romans = []

        while num > 0:
            digit = num % 10

            if digit < 4:
                for _ in range(digit): romans.append(symbols[position])
            elif digit == 4 or digit == 9:
                romans.append(symbols[(digit + 1) * position]);
                romans.append(symbols[position])
            elif digit == 5:
                romans.append(symbols[digit * position])
            else:
                for _ in range(digit - 5):
                    romans.append(symbols[position])
                romans.append(symbols[5 * position])

            position *= 10
            num = num // 10
        return "".join(romans[::-1])
