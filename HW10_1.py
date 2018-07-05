import numpy as np
import matplotlib.pyplot as plt
import lab6_spline as spl
#THIS IS SOLVED BY EXPLICIT METHOD
np.set_printoptions(threshold=np.nan)
L=100        #   Length of modeled domain    [meters]     
Tmagma=1200       #   Temperature of magma        
Trock=300        #   Temperature of country rock 
kappa=1e-6      #   Thermal diffusivity of rock [metersquare/sec]
W =5         #   Width of dike
dt=1*3600*24 #timestep[sec]      
nx=201        #   Number of gridpoints in x-direction
nt=500        #   Number of timesteps to compute
dx=L/(nx-1)   #   Spacing of grid
x=np.linspace(-L/2,L/2,nx)#   Grid
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
#Setup initial temperature profile
T=np.ones(nx)*Trock
for i in range(nx):
    if abs(x[i])<=W/2:
        T[i]=Tmagma
Tospline_T=[1200]
Tospline_time=[0]
time=0
for t in range(nt):#timestep loop
    #Compute new temperature 
    Tnew=np.zeros(nx)
    for i in range(1,nx-2):
        Tnew[i]= T[i] + kappa*dt*(T[i+1]-2*T[i]+T[i-1])/(dx)**2
    Tnew[0]=T[0]
    Tnew[nx-1]=T[nx-1]
    T=Tnew
    time=time+dt
    Tospline_time.append(time)
    Tospline_T.append(max(T))

n=201
ti= np.linspace(0,nt*dt,n)
yi= np.zeros(n)
z_value = spl.make_spline(Tospline_time,Tospline_T)
for i in range(n):
    yi[i]=(spl.spline(ti[i],z_value,Tospline_time,Tospline_T))
    
plt.plot(ti,yi)
plt.show()
def f(x):
    return spl.spline(x,z_value,Tospline_time,Tospline_T)-600
WhenReach600=bisection(0,43200000,f)
print("It reaches 600℃ after",WhenReach600,"Seconds")
print("which is equivalent to",WhenReach600/(3600*24),"Days")