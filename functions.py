import numpy as np



from decimal import Decimal, ROUND_FLOOR


def comprasion_k(k,mass):

    sum1=0

    for i in range(7):
        sum1+=np.e**-2*k*(i+1)


    sum2=0
    for i in range(7):
        sum2+=mass[i]*np.e**(k*-1.0*(i+1))

    sum3=0
    for i in range(7):
        sum3+=np.e**(-2*k*(i+1))

    sum4=0

    for i in range(7):
        sum4+=mass[i]*np.e**(-1*k*(i+1))

    d_sum1=Decimal(sum1*sum2/sum3)
    print(Decimal(sum1*sum2/sum3).quantize(Decimal("1.000"), ROUND_FLOOR) - Decimal(sum4).quantize(Decimal("1.000"), ROUND_FLOOR))
    print(Decimal(sum1*sum2/sum3).quantize(Decimal("1.000"), ROUND_FLOOR))
    print(Decimal(sum4).quantize(Decimal("1.000"), ROUND_FLOOR))
    print('\n')

    return Decimal(sum1*sum2/sum3).quantize(Decimal("1.000"), ROUND_FLOOR) == Decimal(sum4).quantize(Decimal("1.000"), ROUND_FLOOR)