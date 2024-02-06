# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_Team355_maarabrn.py 
# Date:    29 10 2023
# By:      Rania Maaraba
# Section: 21
# Team:    355
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A program in python based on a flow diagram chart that allows
# for user input of P(principal sum), x(annual interest factor), 
# n(compounding frequency), and t(time interest is applied)
# this will then calculate for P, A, and I and output
# r, P, A, and I.

import math , decimal , sys

P1 = float(input('P ='))
X1 = float(input('X ='))
N1 = float(input('N ='))
T1 = float(input('T ='))

r = ((1/(N1**2))*(abs(math.sin(X1))/X1))

r1= 1 + r

print(r1)

exp = N1 * T1

print(exp)

P2= r1**exp

print(P2)

A = P1*P2

I = A - P1

print("The interest rate is {0:.4f}".format(r))
print("The principal amount is ${0:.2f}".format(P1))
print("The final amount is ${0:.2f}".format(A))
print("The Interest Earnings are ${0:.2f}".format(I))
