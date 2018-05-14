import numpy as np
import matplotlib.pyplot as plt
'''
Solving ODE with Taylor Method
    x'=1+x^2+t^3
    x''=2xx'+3t^2
    x```=2xx``+2x`x`+6t
    x````=2xx```+6x`x``+6
    x(1)=4
'''
def taylor4(f0,t,h):
    f=np.zeros(5)
    
    f[0]=f0
    f[1]=1+f[0]**2 + t**3
    f[2]=2*f[0]*f[1]+ 3*t**2
    f[3]=2*f[0]*f[2]+2*f[1]**2+6*t
    f[4]=2*f[0]*f[3]+6*f[1]*f[2]+6

    taylor_expansion=f[0]+h*f[1]+h**2/2*f[2] + h**3/6 * f[3]+h**4/24 * f[4]#taylor expansion
    
    return taylor_expansion;

a=1
b=2#Domain [a,b]
n=101
x=np.zeros(n)
t=np.linspace(a,b,n) #t= a + hi ->this is equivalent to linspace
h=(b-a)/(n-1)

x[0]=-4.0#initial value(boundary problem)

for i in range(n-1):
    x[i+1]= taylor4(x[i],t[i],h)
    
plt.plot(t,x)
plt.show()
print("Value:",x[n-1])
