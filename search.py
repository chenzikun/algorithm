#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-04-13   
    Author:       chenzikun         
-------------------------------------------------

"""
# 二分查找
def binary_search(order_list, a):
    """order_list是从小到大顺序队列"""
    low = 0
    high = len(order_list)
    mid = low + high / 2
    while(low <= high):
        if order_list[mid] == a:
            return mid
        if order_list[mid] < a:
            low = mid + 1
        else:
            high = mid - 1
    return None

# 二叉排序树查找

class BiTreeNode:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value




