#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 17:52
# @Author  : Leishichi
# @File    : 27.py
# @Software: PyCharm
# @Tag:

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        length = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[length] = nums[i]
                length += 1
        return length