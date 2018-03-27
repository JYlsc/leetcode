#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 22:05
# @Author  : Leishichi
# @File    : 1.py
# @Software: PyCharm
# @Tag:

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i

        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in dic.keys():
                if i!= dic[tmp]:
                    return [i, dic[tmp]]


if __name__ =="__main__":
    s = Solution()
    print(s.twoSum([3,2,4],6))