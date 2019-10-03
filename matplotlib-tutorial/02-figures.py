#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:49:07 2019

@author: xilong
"""


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)

# two plots in the same figure
plt.figure(num=3, figsize=(8, 5),)
plt.plot(x, y2)
# plot the second curve in this figure with certain parameters
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.show()