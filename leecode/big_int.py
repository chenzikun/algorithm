#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-04-14   
    Author:       chenzikun         
-------------------------------------------------
大数除法
"""

MAX_DECIMAL = 5
def big_int_division(v, m, max_decimal=None):
    """
    # todo 边界条件
    1. 首部去0
    2. 尾部去0
    3. 尾部四舍五入
    :return:
    """
    data = []
    remain = 0
    # 整数部分
    for item in v:
        i = int(item)
        s = str(int((i + 10 *remain) / m))
        remain = (i + 10*remain) % m
        data.append(s)
    # 小数部分
    if remain != 0:
        max_decimal = MAX_DECIMAL if max_decimal is None else max_decimal
        data.append('.')
        for _ in range(max_decimal):
            s = str(int(10 * remain / m))
            remain = 10 * remain % m
            data.append(s)
            # 尾部去0
            if remain == 0:
                break
    # 尾部四舍五入
    if remain > 0:
        i = remain * 10 / m
        if i >= 5:
            data[-1] = str(int(data[-1]) + 1)
    # 头部去0
    if len(data) >= 2 and data[0] == '0' and data[1] != '.':
        data = data[1:]
    return ''.join(data)

value = '2222'
n = 3
print(big_int_division(value, n))