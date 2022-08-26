from turtle import width
import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch

a = patch.Rectangle((0,1), width=12, height=2, facecolor='red',edgecolor='grey')
b = patch.Rectangle((0,3), width=12, height=2, facecolor='green',edgecolor='grey')
c = patch.Rectangle((0,5), width=12, height=2, facecolor='black',edgecolor='grey')
m,n = py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)
py.axis('equal')
py.show()