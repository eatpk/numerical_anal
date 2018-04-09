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
        print(A)
        for j in range(i+1,n) :
            sum = sum - A[l[i],j]*X[j]        
        X[i] = sum/A[l[i],i]        
    return X
def MLS(x,y):#method of least squares
    n=len(x)
    m=3
    
    A=np.matrix(np.zeros(shape=(n,m)))
    B=np.matrix(np.zeros(shape=(n,1)))
    
    for i in range(n):
        A[i,0]=np.log(x[i])
        A[i,1]=np.cos(x[i])
        A[i,2]=np.exp(x[i])
        B[i,0]=y[i]
        
    AT=A.transpose()
    
    A=AT*A
    B=AT*B
    
    c=Gauss(A,B)
    c=c.A1#A1->transfers matrix to array
    
    return c

#x=[,] #data set
#y=[,] #data set

c=MLS(x,y)

xi=np.linspace(0.2,3,100)
yi=c[0]*np.log(xi)+c[1]*np.cos(xi)+c[2]*np.exp(xi)

plt.plot(x,y,'o',xi,yi)