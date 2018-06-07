from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

x1=0
xr=1

t0=0
t1=0.5

nx=10
nt=100

dx=(xr-x1)/(nx-1)
dt=(t1-t0)/(nt-1)

x= np.zeros((nt,nx))
t= np.zeros((nt,nx))
u=np.zeros((nt,nx))

sig= dt/dx**2

for j in range(nx):
    for i in range(nt):
        x[i,j]= x1+j*dx
        t[i,j]= t0+i*dt
        
        
#initial condition setting
for i in range(nx):
    u[0,i]= np.sin(np.pi*x[0,i])

for i in range(0,nt-1):
    #matrix assemble
    A= np.matrix(np.zeros((nx,nx)))
    B= np.matrix(np.zeros((nx,1)))
    
    A[0,0]=1
    A[nx-1,nx-1]=1
    
    B[0]=0
    B[nx-1]=0
    
    for j in range(1,nx-1):
        A[j,j-1]=-sig
        A[j,j]=1+2*sig
        A[j,j+1]=-sig
        
        B[j]=u[i,j]
        
    #u[i+1,:]=Gauss(A,B).A1
    u[i+1,:]=np.linalg.solve(A,B).A1
fig = plt.figure()
surf=fig.add_subplot(111,projection='3d')

surf.plot_surface(t,x,u)
surf.set_xlabel('t')
surf.set_ylabel('x')
surf.set_zlabel('u')

#plt.contourf(t,x,u)
#plt.xlabel('t')
#plt.ylabel('x')

plt.show()
