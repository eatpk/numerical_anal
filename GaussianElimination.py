import numpy as np

def Gauss(A,B) :
    n = A.shape[0] # 행은 0 열은 1
    
    l = np.zeros(n,dtype=np.int) # index vector
    s = np.zeros(n) # scale vector
    X = np.matrix(np.zeros(n))
    X = X.T  # transpose
    
    # 기본 행 벡터로 잡는다
    
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
    
    print(A)
    
    return X

A = np.matrix([[3.,-13.,9.,3.],[-6.,4.,1.,-18.],[6.,-2.,2.,4.],[12.,-8.,6.,10.]])
B = np.matrix([-19.,-34.,16.,26.])
B = B.T

Gauss(A,B)
