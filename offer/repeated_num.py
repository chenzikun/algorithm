#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-05-09   
    Author:       chenzikun         
-------------------------------------------------
# 数组中重复的数字?

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

# 解题思路：
1. 排序， 时间复杂度 nlog(n)
2. hash表
3. 推荐算法：
    **重点**在于， 长度为n, 数字范围是0~n-1， 解题思路是假设数字m的下标等于m

# 其他
"""




class Solution:
    def findRepeatNumber(self, nums) -> int:
        """"""
