#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-05-09   
    Author:       chenzikun         
-------------------------------------------------
链表翻转
1. 方法一递归
2. 方法二循环
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def recurse(head, newhead):  # 递归，head为原链表的头结点，newhead为反转后链表的头结点
    if head is None:
        return
    if head.next is None:
        newhead = head
    else:
        newhead = recurse(head.next, newhead)
        head.next.next = head
        head.next = None


def reverse_link(head):
    """循环的方法反转链表"""
    if head is None or head.next is None:
        return head
    pre = None
    new_head, current = head
    while current:
        new_head = current

        # 现将next节点缓存下来，next节点作为下一次循环的current
        next_ =  current.next

        # 更改当前的next
        current.next = pre
        # 用于下一次循环
        pre = current

        # 变更下次循环
        current = next_
    return new_head
