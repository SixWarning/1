#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '08/07'

import matplotlib.pyplot as plt
# plt.scatter(2,4)
# plt.show()
x_values = list(range(1, 5001))
y_value = [x**3 for x in x_values]
plt.scatter(x_values, y_value, c=y_value, edgecolors='none', s=20)
# plt.axis([0, 1100, 0, 11000001])
plt.show()
