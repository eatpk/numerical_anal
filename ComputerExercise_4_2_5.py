# Interpolation Newton's form
'''
[Computer Exercises 4.2.5] Approximate arcsin x on the interval [-sqrt(1/2),sqrt(1/2)]by an interpolating polynomial
of degree 15. Determine how accurate the approximation is by numerical test. Use equally spaced
nodes.

'''
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

x= np.linspace(-np.sqrt(1/2),np.sqrt(1/2),16)
y = []
np.arcsin(x)
for i in range(0,16):
    y.append(np.arcsin(x[i]))
m = 10000
xi = np.linspace(-np.sqrt(1/2),np.sqrt(1/2),m)
yi = xi.copy()

to_compare=[]

for i in range(0,m) :
    yi[i]=Newton(xi[i],x,y)#yi represents the interpolated function's value    
    to_compare.append(np.arcsin(xi[i])-yi[i])
    
print("Maximum Error : ",max(to_compare))
plt.plot(x,y,'o',xi,yi)
plt.show()
