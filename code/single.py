#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-05-09   
    Author:       chenzikun         
-------------------------------------------------

单例模式
"""
"""通用型"""
# 元编程方式
class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super(Singleton).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton).__call__(*args, **kwargs)
        return cls.__instance

# 装饰器方式
class Singleton2ed(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]