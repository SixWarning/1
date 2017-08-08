#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '08/07'
from random import randint

class Die():
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面熟之间的数字"""
        return randint(1, self.num_sides)