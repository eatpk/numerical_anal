import numpy as np
import matplotlib.pyplot as plt

a=0
b=1

for n in [10,100,1000]:
    A= np.matrix(np.zeros((n,n)))
    B= np.matrix(np.zeros((n,1)))

    A[0,0]=1
    A[n-1,n-1]=1
    B[0]= 0
    B[n-1]= 1
    h=(b-a) / (n-1)
    for i in range(1,n-1):
        t= a+i*h
    
        A[i,i-1]= (1/h**2 +np.cos(t)/(2*h))
        A[i,i]= -(2/h**2 +np.sin(t))
        A[i,i+1]= (1/h**2 -np.cos(t)/(2*h))
        B[i]= -np.exp(t)
 
    x=np.linalg.solve(A,B)
    
    t= np.linspace(a,b,n)


    plt.plot(t,x,'o')
    plt.show()
