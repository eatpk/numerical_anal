def Newton_Systems(F,DF,X0):
    X= X0
    
    tol = 1.0e-8
    err=2.0*tol
    
    while err>tol:
        X0=X
        X= X - DF(X).I*F(X)
        err= np.linalg.norm(X-X0,np.inf)
        
    return X

def F(x):
    n=x.shape[0]
    y=np.matrix(np.zeros(n)).T
    #Linear Systems Input
    y[0]=x[0]+x[1]+x[2]-3.0
    y[1]=x[0]**2+x[1]**2+x[2]**2-5.0
    y[2]=np.exp(x[0])+x[0]*x[1]-x[0]*x[2]-1.0
    return y    
    
def DF(x):
    n=x.shape[0]
    y=np.matrix(np.zeros(shape=(n,n)))
    #Linear Systems Jacobian Input(Derivative Matrix)
    y[0,0]=1.0
    y[0,1]=1.0
    y[0,2]=1.0
    
    y[1,0]= 2.0*x[0]
    y[1,1]=2.0*x[1]
    y[1,2]=2.0*x[2]
    
    y[2,0]= np.exp(x[0])+x[1]-x[2]
    y[2,1]=x[0]
    y[2,2]=-x[0]
    
    return y
