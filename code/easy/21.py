#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 17:29
# @Author  : Leishichi
# @File    : 21.py
# @Software: PyCharm
# @Tag:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        curr=head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

            curr.next = l1 if l1 else l2

        return head.next
