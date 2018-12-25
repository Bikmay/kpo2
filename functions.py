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

    printFile(sum1, sum2, sum3, sum4)
    d_sum1=Decimal(sum1*sum2/sum3)
    print(d_sum1.quantize(Decimal("1.000"), ROUND_FLOOR) - Decimal(sum4).quantize(Decimal("1.000"), ROUND_FLOOR))
    print(d_sum1.quantize(Decimal("1.000"), ROUND_FLOOR))
    print(Decimal(sum4).quantize(Decimal("1.000"), ROUND_FLOOR))
    print('\n')

    return Decimal(sum1*sum2/sum3).quantize(Decimal("1.000"), ROUND_FLOOR) == Decimal(sum4).quantize(Decimal("1.000"), ROUND_FLOOR)

def printFile(sum1, sum2, sum3, sum4):
    f = open("output.txt", 'a')
    result = "\t\t\t\t\t\t" + str(sum2) + "\n" + "(" + str(sum1) + ") * --------------------- = " + str(
        sum4) + "\n\t\t\t\t\t\t" + str(sum3)
    f.write(result)
    f.write("\n\n")
    f.close()

def nevyzka(input, exper):
    result = input - exper
    return result