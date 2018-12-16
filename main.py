import functions as f


input_mass=[]

print("input values")


input_mass=input().split(' ');


i=1
while(i<101):
    if(f.comprasion_k(i/100,input_mass)):
        k=i/100
