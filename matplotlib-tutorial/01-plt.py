#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:42:07 2019

@author: xilong
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
# y = 8*x + 10
y = x**2
plt.plot(x, y)
plt.show()