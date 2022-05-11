#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-05-11   
    Author:       chenzikun         
-------------------------------------------------
序列化和反序列二叉树
两种解题思路：
    1. 使用中序遍历
    2. 使用双端队列实现层序遍历
"""

import itertools

data = itertools.combinations('ABCD', 1)
print(list(data))