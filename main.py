import functions as f
import findN0 as fn

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