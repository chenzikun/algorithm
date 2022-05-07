#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-04-14   
    Author:       chenzikun         
-------------------------------------------------

"""
import functools

import faker

fake = faker.Faker()

gcount = 0


def swap(items, i, j):
    temp = items[i]
    items[i] = items[j]
    items[j] = temp


def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1, -1, -1):
            if j > i and items[i] > items[j]:
                swap(items, i, j)


# def partition(items, low, high):
#     pivot = items[low]
#     while low < high:
#         while low < high and items[high] >= pivot:
#             high -= 1
#         items[low] = items[high]
#         while low < high and items[low] <= pivot:
#             low += 1
#         items[high] = items[low]
#     items[high] = pivot
#     return low
#
#
# def quick_sort(items, low=None, high=None):
#     if low is None:
#         low = 0
#     if high is None:
#         high = len(items) - 1
#     if low < high:
#         pivot = partition(items, low, high)
#         quick_sort(items, low, pivot - 1)
#         quick_sort(items, pivot + 1, high)


def partition(items, low, high):
    pivot = items[low]
    while low < high:
        while low < high and items[high] >= pivot:
            high -= 1
        items[low] = items[high]
        while low < high and items[low] <= pivot:
            low += 1
        items[high] = items[low]
    items[low] = pivot
    return low


def quick_sort(items, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    if low < high:
        pivot = partition(items, low, high)
        quick_sort(items, low, pivot - 1)
        quick_sort(items, pivot + 1)


def _quick_sort(lists, i=None, j=None):
    if i is None:
        i = 0
    if j is None:
        j = len(lists) - 1
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= pivot:
            i += 1
        lists[j] = lists[i]
    lists[j] = pivot
    _quick_sort(lists, low, i - 1)
    _quick_sort(lists, i + 1, high)
    return lists


items = [3311, 8228, 5726, 126, 2689, 5642, 420, 4908, 1909, 6526]  # [fake.random_int() for _ in range(10)]
# print(items)
quick_sort(items)
print(gcount)
print(items)
