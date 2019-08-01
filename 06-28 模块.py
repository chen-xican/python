#!/usr/bin/env python3  直接在linux Max 等环节直接运行
# -*- coding: utf-8 -*-  表示标准UTF-8编码

' a test module '  # 模块的注释文档

__author__ = 'Michael Liao'  # 作者

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
