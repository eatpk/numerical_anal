import numpy as np
import matplotlib.pyplot as plt

def f(t,x):
    val=np.zeros(2)#vector type
    val[0]=x[1]
    val[1]=x[0]
    
    return val

def Runge_Kutta4(f,x,t,h):
    K=np.zeros((4,len(x)))#(time,order)
    
    K[0]=h*f(t,x)
    K[1]=h*f(t+0.5*h,x+0.5*K[0])
    K[2]=h*f(t+0.5*h,x+0.5*K[1])
    K[3]=h*f(t+h,x+K[2])
    
    x1= x+(K[0]+2*K[1]+2*K[2]+K[3])/6

    return x1

def varphi(z,f,xl,a,b,n):
    h=(b-a)/(n-1)
    x=np.zeros(2)
    x[0]=x1
    x[1]=z
    for i in range(n-1):
        t= a+i*h
        x=Runge_Kutta4(f,x,t,h) # all we need is final value after runge-kutta
        
    return x[0]
def shooting(f,a,b,n,xl,xr,z0,z1):
    tol=1.0e-8
    err=abs(z1-z0)
    
    while(err>tol and ~ err>10000):#boundary condition to initial value condition
        Z1=varphi(z1,f,xl,a,b,n)
        Z0=varphi(z0,f,xl,a,b,n)
        z2= z1+(xr-Z1)*(z1-z0)/(Z1-Z0)#secant method
        err=abs(z1-z2)
        
        z0=z1
        z1=z2
    
    x=np.zeros((n,2))
    
    x[0,0]=x1
    x[0,1]=z1
    h=(b-a)/(n-1)
    
    for i in range(n-1):
        t=a+i*h
        x[i+1,:]=Runge_Kutta4(f,x[i,:],t,h)
    return x[:,0]
    
a=0#Domain [a,b]
b=1
n=10
x1=1
xr=np.exp(1)#EXACT ROOT

z0=0#guessing value
z1=1

xf=shooting(f,a,b,n,x1,xr,z0,z1)


x=np.zeros((n,3))


#Exact Graph
xi=np.linspace(a,b,100)
yi=np.exp(xi)
t=np.linspace(a,b,n) #t= a + hi ->this is equivalent to linspace


plt.plot(t,xf,'o',xi,yi)
