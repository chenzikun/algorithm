#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-05-10   
    Author:       chenzikun         
-------------------------------------------------

实现对二叉树的广度优先遍历

解题思路：
    1. 使用双端队列辅助遍历
"""

class Solution:
    def levelOrder(self, root):
        if not root: return []
        #跟结点入queue
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue])
            #存储当前层的孩子节点列表
            ll = []
            #对当前层的每个节点遍历
            for node in queue:
                #如果左子节点存在，入队列
                if node.left:
                    ll.append(node.left)
                #如果右子节点存在，入队列
                if node.right:
                    ll.append(node.right)
            #后把queue更新成下一层的结点，继续遍历下一层
            queue = ll
        return res
