import numpy as np
A=np.matrix([[1,3,-7],[-3,4,1],[2,-5,3]])
val, vec=np.linalg.eig(A)

val0=val[0]
vec0=vec[:,0]

print(A*vec0-val0*vec0)

A=np.matrix([[1,1],[0,1],[1,0]])
U,S,V= np.linalg.svd(A,full_matrices=True)#singular value decomposition, full_matrices->reduction form
print(U)
print(S)
print(V)
