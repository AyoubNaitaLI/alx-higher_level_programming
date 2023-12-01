#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

resultat_add = add(a, b)
resultat_sub = sub(a, b)
resultat_mul = mul(a, b)
resultat_div = div(a, b)

print("{} + {} = {}".format(a, b, resultat_add))
print("{} - {} = {}".format(a, b, resultat_sub))
print("{} * {} = {}".format(a, b, resultat_mul))
print("{} / {} = {}".format(a, b, resultat_div))

