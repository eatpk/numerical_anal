"""
[Computer Exercise 5.4.6]
Apply and compare the composite rules for trapezoid, two-point Gaussian, and Simpson’s rule for approximating the 

integral[0->2pi] e^(-x)cos(x) dx = 0.499066278634
using 32 applications of each basic rule.


Cheney, Kincaid, <Numerical Mathematics and Computing> 7th ed.
"""

import numpy as np
def f(x):
    return np.exp(-x) * np.cos(x)
#Trapezoid Rule
def Trapezoid(f,a,b,n):
    x=np.linspace(a,b,n+1)
    h=(b-a)/n
    T=0.5*h*(f(x[0])+f(x[n]))
    for i in range(1,n):
        T=T+h*f(x[i])
    return T
#Simpson's Rule
def Simpsons_rule(f,a,b,n):
    x=np.linspace(a,b,n+1)
    h=(b-a)/n
    
    S=  h/3 * (f(x[0])+f(x[n]))
    
    for i in range(1,n//2+1):
        S = S + 4/3 *h*f(x[2*i-1])
        
    for i in range(1,n//2-1 +1):
        S= S+ 2/3*h*f(x[2*i])
    return S
#Gaussian Quadrature
def Quadrature(f,a,b,n):
    m=2 #number of nodes(=weights)
    x=np.zeros(m) #node
    w=np.zeros(m) #weight
    xi=np.zeros(m)
    wi=np.zeros(m)

    x[0]=-np.sqrt(1/3)
    x[1]=np.sqrt(1/3)
    w[0]=1
    w[1]=1
    Q=0;
    t=np.linspace(a,b,n+1)    
    for i in range(n):
        for j in range(m):
            xi[j] = 0.5 *(t[i+1]-t[i])*x[j] + 0.5*(t[i]+t[i+1])
            wi[j]= 0.5*(t[i+1]-t[i])*w[j]
            Q= Q + wi[j]*f(xi[j])
    return Q
t1=Trapezoid(f,0,np.pi*2,32)
t2=Simpsons_rule(f,0,np.pi*2,32)
t3=Quadrature(f,0,np.pi*2,32)
value=0.499066278634
print("Trapezoid Rule =",t1,"Error =",abs(value-t1))
print("Simpson's Rule =",t2,"Error =",abs(value-t2))
print("two-point Gaussian =",t3," Error =",abs(value-t3))
