#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-04-14   
    Author:       chenzikun         
-------------------------------------------------

"""
import functools
import random

import faker

fake = faker.Faker()

gcount = 0


def swap(items, i, j):
    temp = items[i]
    items[i] = items[j]
    items[j] = temp


# 冒泡排序法
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


class Solution:
    def sortArray(self, nums):

        def partition(arr, low, high):
            pivot_idx = random.randint(low, high)  # 随机选择pivot
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]  # pivot放置到最左边
            pivot = arr[low]  # 选取最左边为pivot

            left, right = low, high  # 双指针
            while left < right:

                while left < right and arr[right] >= pivot:  # 找到右边第一个<pivot的元素
                    right -= 1
                arr[left] = arr[right]  # 并将其移动到left处

                while left < right and arr[left] <= pivot:  # 找到左边第一个>pivot的元素
                    left += 1
                arr[right] = arr[left]  # 并将其移动到right处

            arr[left] = pivot  # pivot放置到中间left=right处
            return left

        def quickSort(arr, low, high):
            if low >= high:  # 递归结束
                return
            mid = partition(arr, low, high)  # 以mid为分割点，右边元素>左边元素
            quickSort(arr, low, mid - 1)  # 递归对mid两侧元素进行排序
            quickSort(arr, mid + 1, high)

        quickSort(nums, 0, len(nums) - 1)  # 调用快排函数对nums进行排序
        return nums


# 快排
def partition(items, low, high):
    pivot = items[low]
    while low < high:
        # 发现较小值
        while low < high and items[high] >= pivot:
            high -= 1
        items[low] = items[high]
        # 发现较大值
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
        pivot_index = partition(items, low, high)
        quick_sort(items, low, pivot_index - 1)
        quick_sort(items, pivot_index + 1, high)


if __name__ == '__main__':
    items = [fake.random_int() for _ in range(10)]
    print(items)
    quick_sort(items)
    print(items)


def partition(items, low, high):
    pivot = items[low]
    while low < high and items[high] >= pivot:
        high -= 1
    items[low]= items[high]
    while low < high and items[low] <= pivot:
        low += 1
    items[high] = items[low]
    items[low] = pivot
    return low










def _quick_sort(items, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    while low < high:
        pivot = partition(items, low, high)
        _quick_sort(items, low, pivot - 1)
        _quick_sort(items, pivot + 1, high)
