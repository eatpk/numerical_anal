import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3-2*np.sin(x)

def secant(g,x0,x1):
    
    tolerance= 1.0e-8
    err=10
    i=0
        
    while err>tolerance:
        i+=1
        x= x1 - (x1-x0)/(g(x1)-g(x0)) *g(x1)
        x0=x1
        x1=x
        print(i,"번째 Trial & Value : ",x)
        err=abs(x1-x0)
        
    return x

k1=secant(f,1,2)
print(k1)
print(f)
print("검산:",f(k1),"==0?")

