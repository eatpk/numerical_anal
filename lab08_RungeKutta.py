import numpy as np
import matplotlib.pyplot as plt
#Solving ODE with Runge-Kutta Method

#For example, Runge-kutta 2 is...
#x(t+h)=x(t)+0.5(K1+K2)
#K1=hf(t,x)
#K2=hf(t+h,x+K1)
def f(t,x):
    return 1+x**2+t**3



def Runge_Kutta2(f,x,t,h):
    K=np.zeros(2)
    
    K[0]=h*f(t,x)
    K[1]= h*f(t+h,x+K[0])
    
    x1=x+0.5*(K[0]+K[1])
    
    return x1

def Runge_Kutta4(f,x,t,h):
    
    K=np.zeros(4)
    
    K[0]=h*f(t,x)
    K[1]=h*f(t+0.5*h,x+0.5*K[0])
    K[2]=h*f(t+0.5*h,x+0.5*K[1])
    K[3]=h*f(t+h,x+K[2])
    
    x1= x+(K[0]+2*K[1]+2*K[2]+K[3])/6
    return x1
a=1
b=2#Domain [a,b]
n=101
x=np.zeros(n)
t=np.linspace(a,b,n) #t= a + hi ->this is equivalent to linspace
h=(b-a)/(n-1)

x[0]=-4.0#initial value(boundary problem)

for i in range(n-1):
    x[i+1]= Runge_Kutta4(f,x[i],t[i],h)
    
plt.plot(t,x)
plt.show()
print("Value:",x[n-1])
