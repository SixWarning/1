#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '08/07'
import matplotlib.pyplot as plt
from random import choice
class RandomWalk():
    def __init__(self, num_points=5000):
        """输出化随机漫步属性"""
        self.num_points = num_points

        """所有随机漫步从（0，0）开始"""
        self.x_value = [0]
        self.y_value = [0]

    """选择方向"""
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        #不断漫步，直到列表达到指定长度
        while len(self.x_value) < self.num_points:
            # 决定前进的方向以及沿这个方向前几你的距离
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance
            if x_step == 0 and y_step == 0:
                continue
            #计算下一个点的x和y值
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)

if __name__ == '__main__':
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_value, rw.y_value, linewidth=1) #edgecolor为删除点的轮廓

    #突出终点和起点
    plt.plot(0, 0)
    plt.plot(rw.x_value[-1], rw.y_value[-1])
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()
