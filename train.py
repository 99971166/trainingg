
from sympy import  *
i=symbols('i')
n=symbols('n')
m=symbols('m')
n=int(input('n='))
s=summation(i,(i,1,n))
m=summation(i**2,(i,1,n))
n=summation(i**3,(i,1,n))
print("s=",s)
print("n=",n)
print("m",m)