import numpy as np
import matplotlib.pyplot as plt

def Doolittle(A):
    n=len(A)
    
    L=np.matrix(np.zeros((n,n)))
    U=np.matrix(np.zeros((n,n)))
    
    for k in range(n):
        L[k,k]=1.0
        
        for j in range(k,n):
            S=0.0;
            
            for s in range(k):
                S+=L[k,s]*U[s,j]
            U[k,j]=A[k,j] -S
        for i in range(k,n):
            S=0.0
            
            for s in range(k):
                S+= L[i,s]*U[s,k]
            L[i,k]=(A[i,k]-S)/U[k,k]
    return L,U
       
        

def LDLT(A):
    n=len(A)
    
    L=np.matrix(np.zeros((n,n)))
    D=np.matrix(np.zeros((n,n)))
    
    for j in range(n):
        L[j,j]=1.0
        S=0.0
        for s in range(j):
            S+= D[s,s]*L[j,s]**2
        D[j,j] = A[j,j] -S
        
        for i in range(j,n):
            L[j,i]=0.0
            S=0.0
            
            for s in range(j):
                S+=L[i,s]*D[s,s]*L[j,s]
            L[i,j]=(A[i,j]-S)/D[j,j]
    return L,D
               
def cholesky(A):
    n=len(A)
    
    L=np.matrix(np.zeros((n,n)))
    
    for k in range(n):
        S=0.0
        for s in range(k):
            S +=L[k,s]**2
            
        L[k,k]=np.sqrt((A[k,k]-S))
        for i in range(k,n):
            S=0.0
            
            for s in range(k):
                S+=L[i,s]*L[k,s]
            L[i,k]=(A[i,k]-S)/L[k,k]
    return L

A= np.matrix([[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]])
L, U = Doolittle(A)
print(L*U-A)

B=np.matrix([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]])
L,D = LDLT(B)
print(L*D*L.T-B)

L=cholesky(B)
print(L*L.T-B)