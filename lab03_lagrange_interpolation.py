import numpy as np
import matplotlib.pyplot as plt

def l(t,x,i):#t is x, x is value in the node(array), i is index
    
    n=len(x)
    val = float(1)
    
    for j in range(0,n):
        if(i!=j):
            val*= (t-x[j])/(x[i]-x[j])
            
    return val

def lagrange(t,x,y):
    n=len(x)
    val=0
    for i in range(0,n):
        val+= y[i]*l(t,x,i)
        
    return val

xi=np.linspace(-1,1,100)#array

yi=[]

x=[1/3,1/4,1]
y=[2,-1,7]

for i in range(0,100):
    yi.append(lagrange(xi[i],x,y))

plt.plot(x,y,'o',xi,yi)

plt.show()


    
