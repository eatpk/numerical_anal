import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2,2,100)

def f(x):
    return x**3 - 2*np.sin(x)
def df(x):
    return 3*x**2-2*np.cos(x)
#plt.plot(x,f(x))

def bisection(a,b):
    i=1
    err=1
    tolerance=1.0e-8
    while(err>tolerance):
        c=(a+b)/2
        a_sign=np.sign(f(a))
        b_sign=np.sign(f(b))
        c_sign=np.sign(f(c))
        if(a_sign==c_sign):
            a=c
        if(b_sign==c_sign):
            b=c
        err=abs(a-b)
        print(i,"trial:",c)
        i=i+1
    return (a+b)/2

def newton(x0):
    tolerance=1.0e-8
    err=1
    j=1
    x=x0
    while(err>tolerance):
        
        new=x
        x=x-f(x)/df(x)
        err=abs(x-new)
        j=j+1
        print(j,"trial",x)
    return x
    
#k=bisection(0.5,2)
k1=newton(1)
print(k1)
#print(k)
#print("검산:",k**3-2*np.sin(k),"==0?")
