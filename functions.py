import numpy as np

def comprasion_k(k,mass):

    sum1=0

    for i in range(7):
        sum1+=np.e**k*i


    sum2=0
    for i in range(7):
        sum2+=mass[i]*np.e**k*-1*i

    sum3=0
    for i in range(7):
        sum3+=np.e**-2*k*i

    sum4=0

    for i in range(7):
        sum4+=mass[i]*np.e**-1*k*i


    return round(sum1*sum2/sum3,4) == round(sum4,4)