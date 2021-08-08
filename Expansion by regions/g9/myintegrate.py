#!/usr/bin/env python3

from pySecDec.integral_interface import IntegralLibrary
import sympy as sp
import math

# g5

EulerGamma = 0.57721566490153286060651209008240243104215933593992

def g9_0(s12,mh2,mt2):
    analytic0 = (1)/(6*mt2**2)
    return analytic0

def g9_eps(s12,mh2,mt2):
    analytic1 =  -(s12 + (6*mt2 + s12)*math.log(1/mt2))/(12*mt2**2)
    analytic2 = (1 + math.log(1/mt2) - EulerGamma)/(6*mt2**2)
    return analytic2

# load c++ library
#s1, s2, s3, mtsq, mhsq =  0.0009 , -0.000442873775 , -0.0003 , 1.0 , 0.000157126225
s1, s2, s3, mtsq, mhsq =  0.00383,-0.000966,-0.000966,1.0,0.000157126225
names = ["g9"]
real_parameters = [[s1,s2,s3,mtsq,mhsq,1]] # z set to 1

#names = ["g7_s12_z", "g7_s12_m"]
#real_parameters = [[s1,s2,s3,mtsq,mhsq,1], [s1,s2,s3,mtsq,mhsq]] # z set to 1

#EulerGamma = 0.57721566490153286060651209008240243104215933593992

print('Analytic Result :')
#print('EulerGamma :', EulerGamma)
print('eps^0 : ',g9_0(s1,mhsq,mtsq))
print('eps : ',g9_eps(s1,mhsq,mtsq))
    


for name, realp in zip(names, real_parameters):
    intlib = IntegralLibrary("{0}/{0}_pylink.so".format(name))
    intlib.use_Qmc(transform="korobov3", fitfunction="polysingular")

    # integrate
    str_integral_without_prefactor, str_prefactor, str_integral_with_prefactor = intlib(real_parameters=realp)

    # convert complex numbers from c++ to sympy notation
    str_integral_with_prefactor = str_integral_with_prefactor.replace(',','+I*')

    # convert result to sympy expressions
    integral_result = sp.sympify(str_integral_with_prefactor.replace('+/-','*value+error*'))
    integral_result_err = sp.sympify(str_integral_with_prefactor.replace('+/-','*value+error*'))

    # examples how to access individual orders
    print('Numerical Result')
    for power in [0, 1]:
        valreal, valimg = integral_result.coeff('eps',power).coeff('value').as_real_imag()
        errreal, errimg = integral_result.coeff('eps',power).coeff('error').as_real_imag()
        print("eps^{:<2} {: .5f}{:+.5f}*I +/- {: .5e}{:+.5e}*I".format(power,float(valreal),float(valimg),float(errreal),float(errimg)))
