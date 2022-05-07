#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-05-07   
    Author:       chenzikun         
-------------------------------------------------
链表中是否有环
"""

# 链表中是否有环
class Node:
    def __init__(self, node=None):
        self.next = node
        self.value = None

def has_linked_circle(node):
    slow, fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False