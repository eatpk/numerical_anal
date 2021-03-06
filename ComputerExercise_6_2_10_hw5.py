'''
[Computer Exercises 6.2.10]Using the Runge function f(x) = 1/(1+x^2) from Section 4.2 with an increasing 
number of equally spaced nodes, watch the natural cubic spline curve get better with regard to curve fitting
while the interpolating polynomial gets worse.

Exercise From <Computer Exercises 6.2.10>

W. Cheney, D. Kincaid [Numerical Mathematics and Computing, 7th edition]
'''

import numpy as np
import matplotlib.pyplot as plt

def Gauss(A,B) :
    n = A.shape[0] # Number of Rows index=0, number of columns index= 1   
    l = np.zeros(n,dtype=np.int) # index vector
    s = np.zeros(n) # scale vector
    X = np.matrix(np.zeros(n))
    X = X.T  # transpose
    for i in range(n) :
        l[i] = i        
        smax = 0        
        for j in range(n):
            smax = max(smax,abs(A[i,j]))        
        s[i]= smax    
    for k in range(n) :
        rmax=0        
        for i in range(k,n):
            r = abs(A[l[i],k]/s[l[i]])
            
            if (r>rmax):
                rmax =r
                j = i                
        tmp = l[j]
        l[j] = l[k]
        l[k] = tmp        
        for i in range(k+1,n) :
            alpha = A[l[i],k]/A[l[k],k]            
            for j in range(k,n):
                A[l[i],j]=A[l[i],j]-alpha*A[l[k],j]                
            B[l[i]]=B[l[i]] - alpha*B[l[k]]        
    #Back substitution    
    X[n-1] = B[l[n-1]]/ A[l[n-1],n-1]    
    for i in range(n-2,-1,-1):
        sum = B[l[i]]
        for j in range(i+1,n) :
            sum = sum - A[l[i],j]*X[j]        
        X[i] = sum/A[l[i],i]        
    return X

def make_spline(t,y):
    
    n= len(t)  
    h=np.zeros(n-1)
    b=np.zeros(n-1)
    u=np.zeros(n-1)
    v=np.zeros(n-1)
    for i in range(n-1):
        h[i]= t[i+1]-t[i]
        b[i]=(y[i+1]-y[i])/h[i]
      
      
    for i in range(n-1):
        u[i]= 2*(h[i]+h[i-1])
        v[i]=6*(b[i]-b[i-1])

    A=np.matrix(np.zeros(shape=(n,n)))
    B=np.matrix(np.zeros(shape=(n,1)))
  
    A[0,0]=1
    A[n-1,n-1]=1

    for i in range(1,n-1):
        A[i,i-1]= h[i-1]
        A[i,i]= u[i]
        A[i,i+1]=h[i]
        B[i,0]=v[i]
    z=Gauss(A,B)
    z=z.A1
    return z

def spline(x,z,t,y):
    i= len(z)-2
    
    while(x<t[i] and i>0):
        i -=1
    h=t[i+1]-t[i]
    
    #see eq.(5) of p.267
    S= z[i+1]/(6*h) * (x-t[i])**3
    S +=z[i]/(6*h)*(t[i+1]-x)**3
    S += (y[i+1]/h - h/6*z[i+1]) *(x-t[i])
    S +=(y[i]/h - h/6*z[i]) *(t[i+1]-x)
    return S

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

def runge(x):
    return 1/(1+x**2)


yi= np.zeros(3000)
yj= np.zeros(3000)
ti= np.linspace(-5,5,3000)


for i in range(0,7):
    y=[]
    n=3000
    m= 2**(i+1)
    t=np.linspace(-5,5,m)
    for j in range(m):
        y.append(runge(t[j]))
    
    coeff=make_spline(t,y)
    for k in range(3000):
        yi[k]=spline(ti[k],coeff,t,y)
        yj[k]=Newton(ti[k],t,y)
    plt.plot(t,y,'o',ti,yi,ti,yj)
    plt.show()

    
