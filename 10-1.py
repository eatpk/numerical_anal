import numpy as np
import matplotlib.pyplot as plt
import lab6_spline as spl
#THIS IS SOLVED BY IMPLICIT METHOD
L=100        #   Length of modeled domain    [meters]     
Tmagma=1200       #   Temperature of magma        
Trock=300        #   Temperature of country rock 
W =5         #   Width of dike
x1=-L/2
xr=L/2
t0=0
t1=3600*24*500
nx=101
nt=51

dx=(xr-x1)/(nx-1)#h
dt=(t1-t0)/(nt-1)#k
x= np.zeros((nt,nx))
t= np.zeros((nt,nx))
u=np.zeros((nt,nx))
sig= 1e-6*dt/dx**2
def bisection(a,b,f):
    i=1
    err=1
    tolerance=1.0e-6
    while(err>tolerance):
        c=(a+b)/2
        a_sign=np.sign(f(a))
        b_sign=np.sign(f(b))
        c_sign=np.sign(f(c))
        if(a_sign==c_sign):
            a=c
        if(b_sign==c_sign):
            b=c
        err=abs(a-b)
        i=i+1
    return (a+b)/2
for j in range(nx):
    for i in range(nt):
        x[i,j]= x1+j*dx
        t[i,j]= t0+i*dt
#initial condition setting
for i in range(nx):
    u[0,i]=Trock
    if abs(x[0,i])<=W/2:
        u[0,i]=Tmagma
umax=[1200]
for i in range(0,nt-1):
    #matrix assemble
    A= np.matrix(np.zeros((nx,nx)))
    B= np.matrix(np.zeros((nx,1)))
    A[0,0]=1
    A[nx-1,nx-1]=1
    B[0]=300
    B[nx-1]=300
    
    for j in range(1,nx-1):
        A[j,j-1]=-sig
        A[j,j]=1+2*sig
        A[j,j+1]=-sig
        B[j]=u[i,j]    
    u[i+1,:]=np.linalg.solve(A,B).A1
    umax.append(max(u[i+1,:]))

t=np.linspace(0,t1,nt)
plt.plot(t,umax)
n=201
ti= np.linspace(0,nt*dt,n)
yi= np.zeros(n)
z_value = spl.make_spline(t,umax)

for i in range(n):
    yi[i]=(spl.spline(ti[i],z_value,t,umax))
def f(x):
    return spl.spline(x,z_value,t,umax)-600
WhenReach600=bisection(0,43200000,f)
print("It reaches 600℃ after",WhenReach600,"Seconds")
print("which is equivalent to",WhenReach600/(3600*24),"Days")