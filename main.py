import functions as f
import findN0 as fn
import numpy as np

input_mass=[]

print("input values")


input_mass=(input().split(' '));

for i in range(7):
    input_mass[i]=int(input_mass[i])

K = 0.001
check = f.comprasion_k(K, input_mass)
while not check:
    K += 0.001
    print(K)
    check = f.comprasion_k(K, input_mass)
    if(K>0.999):
        break

n=fn.findN(K,input_mass)
print(n)

o=n*K*1
op=0

for i in range(7):
    op=o*np.exp(-1*K*(i+1))
    print(op)
    n-=op

print(n)
