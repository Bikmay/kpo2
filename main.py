import functions as f


input_mass=[]

print("input values")


input_mass=input().split(' ');


K = 0.01
check = f.comprasion_k(K, input_mass)
while not check:
    K += 0.01
    check = f.comprasion_k(K, input_mass)
