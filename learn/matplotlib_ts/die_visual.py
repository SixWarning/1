#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '08/07'
from die import Die
import pygal

#创建一个D6
die = Die()

#投掷骰子，并将结果存储在一个列表里
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    #统计骰子每个面出现的次数
    frequency = results.count(value)
    print(frequency)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
