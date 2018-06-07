import numpy as np
import matplotlib.pyplot as plt
#Eplliptic PDE
left=0
right=1

bottom=0
top=1

n=20+1
N=n*n
h=(top-bottom)/(n-1)

A=np.matrix(np.zeros((N,N)))
B=np.matrix(np.zeros((N,1)))

u= np.zeros(N)

f=-1/25

#matrix Assemble

for i in range(1,n-1):
    for j in range(1,n-1):
        k=i+j*n
        A[k,k+1]=1
        A[k,k-1]=1
        A[k,k+n]=1
        A[k,k-n]=1
        A[k,k]= (h*h*f-4)
        B[k]=0
#setting boundary condition
#bottom
for i in range(n):
    x= left+i*h
    y=bottom
    
    k=i
    A[k,k]=1
    B[k]= np.cosh(x/5)+np.cosh(y/5)
#right
for i in range(n):
    x=right
    y= bottom+i*h
    
    k=(n-1)+i*n
    A[k,k]=1
    B[k]= np.cosh(x/5)+np.cosh(y/5)
#top
for i in range(n):
    x=left+i*h
    y=top
    
    k=(n-1)*n+i
    A[k,k]=1
    B[k]= np.cosh(x/5)+np.cosh(y/5)
    
#left
for i in range(n):
    x=left
    y=bottom+i*h
    k=i*n
    A[k,k]=1
    B[k]= np.cosh(x/5)+np.cosh(y/5)
    
#solve systems
u=np.linalg.solve(A,B).A1

x=np.zeros((n,n))
y=np.zeros((n,n))
uu=np.zeros((n,n))

for i in range(n):
    for j in range(n):
        k= i+j*n
        
        x[i,j]=left+i*h
        y[i,j]=bottom+j*h
        uu[i,j]=u[k]
plt.contourf(x,y,uu)
plt.show()
