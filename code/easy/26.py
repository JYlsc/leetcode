#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 17:40
# @Author  : Leishichi
# @File    : 26.py
# @Software: PyCharm
# @Tag:

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        length = 0
        curr = None
        for i in range(len(nums)):
            if curr != nums[i]:
                nums[length] = nums[i]
                length += 1
                curr = nums[i]
        print(nums)
        return length


s = Solution()
s.removeDuplicates([1,1,2])


