import numpy as np
import matplotlib.pyplot as plt
def MLS(x,y):#method of least squares
    n=len(x)
    m=2
    A=np.matrix(np.zeros(shape=(n,m)))
    B=np.matrix(np.zeros(shape=(n,1)))
    for i in range(n):
        A[i,0]=x[i]
        A[i,1]=1
        B[i,0]=y[i]   
    AT=A.T
    A=AT*A
    B=AT*B
    c=np.linalg.solve(A,B)
    c=c.A1#A1->transfers matrix to array
    return c
hlog=[]
errlog=[]
h=[1/10,1/20,1/40,1/80]
err=[0.00339499529209,0.00088212104465,0.000222447054605,5.5727253629e-05]
for i in range(4):
    hlog.append(np.log(h[i]))
    errlog.append(np.log(err[i]))   
plt.loglog(h,err,'o',h,err)
print(MLS(hlog,errlog))


