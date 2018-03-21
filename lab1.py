import os
import sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)


import numpy as np
import matplotlib.pyplot as plt


c=np.ones((2,2))
print(c)
x=np.matrix([[0,1],[2,3]])

y=np.linspace(0,2*np.pi,100)#0에서 2ㅠ까지 100등분
print(y)
z=np.sin(y)

print(z)

plt.plot(y,z,'o')# x and y must have same first dimension, but have shapes (100,) and (1,)
plt.show()
