# -*- coding: utf-8 -*-
"""
Solve this pair of simultaneous nonlinear equations by first eliminating y and then solving the resulting
equation in x by Newton’s method. Start with the initial value x0 = 1:0.

Computer exercise 3.2.22
solved by linear systems 
"""


import numpy as np

def f(x):#x is matrix
    return np.matrix([[x.item(0,0)**3-2*x.item(0,0)*x.item(1,0)+x.item(1,0)**7-4*x.item(1,0)*x.item(0,0)**3-5],[x.item(1,0)*np.sin(x.item(0,0))+3*x.item(1,0)*x.item(0,0)**2+np.tan(x.item(0,0))-4]])
def J(x):
    return np.matrix([[3*x.item(0,0)**2-2*x.item(1,0)-12*x.item(1,0)*x.item(0,0)**2,-2*x.item(0,0)+7*x.item(1,0)**6-4*x.item(0,0)**3],[x.item(1,0)*np.cos(x.item(0,0))+6*x.item(0,0)*x.item(1,0)+1/((np.cos(x.item(0,0)))**2),np.sin(x.item(0,0))+3*x.item(0,0)**2]])

def newton(x0):
    tolerance=1.0e-8
    err=[1,1]
    j=1
    x=np.matrix([[x0],[x0]])
    
    while(max(err)>tolerance):
        new=x
        x=x-np.linalg.inv(J(x))*f(x)
        
        
        err=(abs(x-new))
        
        print(j,"번째시도",(x))
        j=j+1
    return x   

k=newton(1)
print("Anwser for x,y is ",k, "respectively")
print(f(k),"==0?")
