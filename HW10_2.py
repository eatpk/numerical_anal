from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
def analytic_sol(x,y,n):#n is big number
    V=1;a=1;b=1
    f=0
    for i in range(1,n,2):
        f= f+ 4*V*np.sinh(i*np.pi*y/a)*np.sin(i*np.pi*x/a)/(i*np.pi*np.sinh(i*np.pi*b/a))
    return f
left=0
right=1
bottom=0
top=1
n=81
N=n*n
h=(top-bottom)/(n-1)
A=np.matrix(np.zeros((N,N)))
B=np.matrix(np.zeros((N,1)))
u= np.zeros(N)
f=0
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
    B[k]= 0
#right
for i in range(n):
    x=right
    y= bottom+i*h
    k=(n-1)+i*n
    A[k,k]=1
    B[k]= 0
#top
for i in range(n):
    x=left+i*h
    y=top
    k=(n-1)*n+i
    A[k,k]=1
    B[k]= 1    
#left
for i in range(n):
    x=left
    y=bottom+i*h
    k=i*n
    A[k,k]=1
    B[k]= 0
#solve systems
u=np.linalg.solve(A,B).A1
x=np.zeros((n,n))
y=np.zeros((n,n))
uu=np.zeros((n,n))
analytic=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        k= i+j*n
        
        x[i,j]=left+i*h
        y[i,j]=bottom+j*h
        uu[i,j]=u[k]
        analytic[i,j]=analytic_sol(x[i,j],y[i,j],n)        
plt.contourf(x,y,uu)
plt.show()
plt.contourf(x,y,analytic)
plt.show()
plt.contourf(x,y,abs(analytic-uu))
plt.show()
au=abs(analytic-uu)
fig = plt.figure()
surf=fig.add_subplot(111,projection='3d')
surf.plot_surface(x,y,uu)
surf.set_xlabel('x')
surf.set_ylabel('y')
surf.set_zlabel('au')

abs(analytic_sol(0.5,0.8,100)-uu[40,64])