import numpy as np
import matplotlib.pyplot as plt
#high Order-> making system, rendering equations to first order to solve
highest_order=3
def f(t,x):
    v=np.zeros(highest_order)#vector type
    
    v[0]=x[1]
    v[1]=x[2]
    v[2]= np.cos(x[0])+np.sin(x[1])-np.exp(x[2])+t**2
    return v

def Runge_Kutta4(f,x,t,h):
    K=np.zeros((4,len(x)))#(time,order)
    
    K[0]=h*f(t,x)
    K[1]=h*f(t+0.5*h,x+0.5*K[0])
    K[2]=h*f(t+0.5*h,x+0.5*K[1])
    K[3]=h*f(t+h,x+K[2])
    
    x1= x+(K[0]+2*K[1]+2*K[2]+K[3])/6
    return x1
a=0#Domain [a,b]
b=1

n=101
x=np.zeros((n,highest_order))
t=np.linspace(a,b,n) #t= a + hi ->this is equivalent to linspace
h=(b-a)/(n-1)

x[0,0]=3#initial value(boundary problem)
x[0,1]=7
x[0,2]=13#x[time,order]
#x[0,3]....x[0,highest_order-1]=k


for i in range(n-1):
    x[i+1]= Runge_Kutta4(f,x[i],t[i],h)

x=x[:,0]
plt.plot(t,x)
plt.show()
