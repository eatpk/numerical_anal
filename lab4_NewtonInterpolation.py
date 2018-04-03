# Interpolation Newton's form

import numpy as np
import matplotlib.pyplot as plt

def Newton(t,x,y):
    n = len(x)
    a = y.copy()
    
    for j in range(1,n) :
        for i in range(n-1,j-1,-1):
            a[i] = ( a[i]-a[i-1])/(x[i]-x[i-j])
    
    val = a[n-1]
    
    for i in range(n-1,0,-1) :
        val = val*(t-x[i-1])+a[i-1]
    
    return val

x = [ 0., 1., -1., 2., -2.]
y = [-5., -3., -15., 39., -9.]

n = len(x)
m = 100

xi = np.linspace(-2,2,m)
yi = xi.copy()

for i in range(0,m) :
    yi[i]=Newton(xi[i],x,y)
    
plt.plot(x,y,'o',xi,yi)
