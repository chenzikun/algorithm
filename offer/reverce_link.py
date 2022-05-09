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


def reverse_list(head):
    # 三要素
    # 1.明确函数功能，该函数可以将链表反转，并返回一个头节点
    # 2.结束条件：当链表为空或只有一个节点时返回
    if head == None or head.next == None:
        return head
    # 3.等价条件（缩小范围），对于数组来讲，缩小范围是n——>n-1，对于链表来讲则可以考虑head——>head.next
    reverse = reverse_list(head.next)  # 假设reverse是head以后的、已经反转过的链表

    # 接下来要做的是将head节点接到已经反转过的reverse上
    
    head.next.next = head
    head.next = None

    return reverse  # 返回新的列表

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
