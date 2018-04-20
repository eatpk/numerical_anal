'''
[Computer Exercises 1.4.3] Alter and test the pseudocode in the text for computing x-sin x by using nested
multiplication to evaluate the series.
'''

import numpy as np

def f(x):
    n=10
    if abs(x)>=1.9:
        return x-np.sin(x)
    else:
        t= float((x**3)/6)
        s=t
        
        for i in range(2,n):
            t= float((-t*(x**2))/((2*i+2)*(2*i+3)))
            s=s+t
        return s
        
x=float(input("Calculating the value of x - sin(x), insert x:"))
print(f(x))
