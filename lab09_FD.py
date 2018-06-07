import numpy as np
import matplotlib.pyplot as plt

def Gauss(A,B) :
    n = A.shape[0] # row:0 col:1
    
    l = np.zeros(n,dtype=np.int) # index vector
    s = np.zeros(n) # scale vector
    X = np.matrix(np.zeros(n))
    X = X.T  # transpose
    
    # taking it as basic row vector
    
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
    
    print(A)
    
    return X
a=1
b=2
n=10

A= np.matrix(np.zeros((n,n)))
B= np.matrix(np.zeros((n,1)))

A[0,0]=1
A[n-1,n-1]=1

B[0]= 1.09737491
B[n-1]= 8.63749661

h=(b-a) / (n-1)

for i in range(1,n-1):
    t= a +i*h
    
    A[i,i-1]= -(1+h/2)
    A[i,i]= (2-h**2)
    A[i,i+1]= -(1-h/2)

    B[i]= -h**2*(np.exp(t)-3 * np.sin(t))


    
x=Gauss(A,B)
t= np.linspace(a,b,n)
ti= np.linspace(a,b,100)
xi=np.exp(ti)-3 * np.cos(ti)

plt.plot(t,x,'o',ti,xi)
plt.show()
