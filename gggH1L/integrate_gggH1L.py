from __future__ import print_function
from pySecDec.integral_interface import IntegralLibrary
import sympy as sp
import math

topmass = 1.0                                # Actual top mass : 172.76 ± 0.3 GeV/c2  # topmass = 172.76
hmass = 0.012535                               # Actual Higgs Mass : 125.35 ± 0.15 GeV/c2
s1 = 0.0009*topmass*topmass                     # s1 = temporary variable for s12
s3 = -0.0003*topmass*topmass                    # s2 = temporary variable for s13
s2 = (hmass*hmass) - s1 - s3                 # s3 = temporary variable for s23
temp1 = 3*topmass*topmass*s1
temp2 = 3*topmass*topmass*s2
temp3 = 3*topmass*topmass*s3
temp4 = 3*topmass*topmass*s3*s1*s2
output1 = 4/temp3
output2 = 4/temp1
output3 = 4/temp2
output4 = (4*(s1*s2+s2*s3+s1*s3))/temp4

if __name__ == "__main__":

    # load c++ library
    amp1 = IntegralLibrary('F212/F212_pylink.so')
    amp2 = IntegralLibrary('F312/F312_pylink.so')

    # choose Qmc integrator
    # amp.use_Qmc()  # Qmc doesnt work as of now for new version, try Vegas  # amp.use_Vegas()
    amp1.use_Qmc()
    amp2.use_Qmc()

    # integrate
    str_integral_without_prefactor, str_prefactor, str_integral_with_prefactor = amp1([s1,s2,s3,topmass*topmass,hmass*hmass],verbose=True,epsrel=1e-4,epsabs=1e-14)  # [s12 , s13, s23, mtsq , mhsq] 

    # convert complex numbers from c++ to sympy notation
    str_integral_with_prefactor = str_integral_with_prefactor.replace(',','+I*')
    str_prefactor = str_prefactor.replace(',','+I*')
    str_integral_without_prefactor = str_integral_without_prefactor.replace(',','+I*')

    # convert result to sympy expressions
    integral_with_prefactor = sp.sympify(str_integral_with_prefactor.replace('+/-','*value+error*'))
    integral_with_prefactor_err = sp.sympify(str_integral_with_prefactor.replace('+/-','*value+error*'))
    prefactor = sp.sympify(str_prefactor)
    integral_without_prefactor = sp.sympify(str_integral_without_prefactor.replace('+/-','*value+error*'))
    integral_without_prefactor_err = sp.sympify(str_integral_without_prefactor.replace('+/-','*value+error*'))

    # Get Value F212
    f212 = (-1)*(integral_with_prefactor.coeff('eps',0).coeff('value').args[0])
    f212_error = (-1)*(integral_with_prefactor_err.coeff('eps',0).coeff('error').args[0])

    # integrate
    str_integral_without_prefactor, str_prefactor, str_integral_with_prefactor = amp1([s2,s3,s1,topmass*topmass,hmass*hmass],verbose=True,epsrel=1e-4,epsabs=1e-14)  # [s12 , s13, s23, mtsq , mhsq] 

    # convert complex numbers from c++ to sympy notation
    str_integral_with_prefactor = str_integral_with_prefactor.replace(',','+I*')
    str_prefactor = str_prefactor.replace(',','+I*')
    str_integral_without_prefactor = str_integral_without_prefactor.replace(',','+I*')

    # convert result to sympy expressions
    integral_with_prefactor = sp.sympify(str_integral_with_prefactor.replace('+/-','*value+error*'))
    integral_with_prefactor_err = sp.sympify(str_integral_with_prefactor.replace('+/-','*value+error*'))
    prefactor = sp.sympify(str_prefactor)
    integral_without_prefactor = sp.sympify(str_integral_without_prefactor.replace('+/-','*value+error*'))
    integral_without_prefactor_err = sp.sympify(str_integral_without_prefactor.replace('+/-','*value+error*'))

    # Get Value F311
    f311 = (-1)*(integral_with_prefactor.coeff('eps',0).coeff('value').args[0])
    f311_error = (-1)*(integral_with_prefactor_err.coeff('eps',0).coeff('error').args[0])

    # integrate
    str_integral_without_prefactor, str_prefactor, str_integral_with_prefactor = amp1([s3,s1,s2,topmass*topmass,hmass*hmass],verbose=True,epsrel=1e-4,epsabs=1e-14)  # [s12 , s13, s23, mtsq , mhsq] 

    # convert complex numbers from c++ to sympy notation
    str_integral_with_prefactor = str_integral_with_prefactor.replace(',','+I*')
    str_prefactor = str_prefactor.replace(',','+I*')
    str_integral_without_prefactor = str_integral_without_prefactor.replace(',','+I*')

    # convert result to sympy expressions
    integral_with_prefactor = sp.sympify(str_integral_with_prefactor.replace('+/-','*value+error*'))
    integral_with_prefactor_err = sp.sympify(str_integral_with_prefactor.replace('+/-','*value+error*'))
    prefactor = sp.sympify(str_prefactor)
    integral_without_prefactor = sp.sympify(str_integral_without_prefactor.replace('+/-','*value+error*'))
    integral_without_prefactor_err = sp.sympify(str_integral_without_prefactor.replace('+/-','*value+error*'))

    # Get Value F332
    f332 = (-1)*(integral_with_prefactor.coeff('eps',0).coeff('value').args[0])
    f332_error = (-1)*(integral_with_prefactor_err.coeff('eps',0).coeff('error').args[0])

    # integrate
    str_integral_without_prefactor, str_prefactor, str_integral_with_prefactor = amp2([s1,s2,s3,topmass*topmass,hmass*hmass],verbose=True,epsrel=1e-4,epsabs=1e-14)  # [s12 , s13, s23, mtsq , mhsq] 

    # convert complex numbers from c++ to sympy notation
    str_integral_with_prefactor = str_integral_with_prefactor.replace(',','+I*')
    str_prefactor = str_prefactor.replace(',','+I*')
    str_integral_without_prefactor = str_integral_without_prefactor.replace(',','+I*')

    # convert result to sympy expressions
    integral_with_prefactor = sp.sympify(str_integral_with_prefactor.replace('+/-','*value+error*'))
    integral_with_prefactor_err = sp.sympify(str_integral_with_prefactor.replace('+/-','*value+error*'))
    prefactor = sp.sympify(str_prefactor)
    integral_without_prefactor = sp.sympify(str_integral_without_prefactor.replace('+/-','*value+error*'))
    integral_without_prefactor_err = sp.sympify(str_integral_without_prefactor.replace('+/-','*value+error*'))

    # Get Value F212
    f312 = (-1)*(integral_with_prefactor.coeff('eps',0).coeff('value').args[0])
    f312_error = (-1)*(integral_with_prefactor_err.coeff('eps',0).coeff('error').args[0])

    # examples how to access individual orders
    #print('Numerical Result')
    #print('eps^-2:', integral_with_prefactor.coeff('eps',-2).coeff('value'), '+/- (', integral_with_prefactor_err.coeff('eps',-2).coeff('error'), ')')
    #print('eps^-1:', integral_with_prefactor.coeff('eps',-1).coeff('value'), '+/- (', integral_with_prefactor_err.coeff('eps',-1).coeff('error'), ')')
    #print('eps^0 :', integral_with_prefactor.coeff('eps',0).coeff('value'), '+/- (', integral_with_prefactor_err.coeff('eps',0).coeff('error'), ')')
    
    # coefficients of eps^-1 and eps^-2 will be zero because we are dealing with non-divergent amplitude, so we only print and use the eps^0 coefficient    

    # print result
    print('---------------------------------------------------------------')
    print('Numerical Results For All Normalized Form Factors :')
    print('Normalized F212 : ', f212 , ' +/- ', f212_error)
    print('Normalized F311 : ', f311 , ' +/- ', f311_error)
    print('Normalized F332 : ', f332 , ' +/- ', f332_error)
    print('Normalized F312 : ', f312 , ' +/- ', f312_error)

    print('---------------------------------------------------------------')
    print('Analytic results of all Normalized Form Factors with heavy top quark limit')
    print('Analytic Result Normalized F212 :', output1)
    print('Analytic Result Normalized F311 :', output2)
    print('Analytic Result Normalized F332 :', output3)
    print('Analytic Result Normalized F312 :', output4)
    print('---------------------------------------------------------------')

    # Use the form factor values to calculate the Mod Squared Amplitude

    # Set the dimesnions as 4 because Form Factors dont have divergent terms of epsilon -> we can safely substitute eps = 0 now
    dim = 4
    
    # Because we are dealing with normalised form factors, conjugate dont have effect
   
    k1 = ( (dim-2)*f212*f212*s1*s1*s1*s3)/(s2)

    k2 = (f212*f332*s1*s3*s3)

    k3 = (f212*f311*s1*s1*s2)

    k4 = ((dim-2)*f212*f312*s1*s1*s3)

    k5 = (f332*f212*s1*s3*s3)

    k6 = ( (dim-2)*f332*f332*s3*s3*s3*s2)/(s1)

    k7 = (f332*f311*s2*s2*s3)

    k8 = ((dim-2)*f332*f312*s2*s3*s3)

    k9 = (f311*f212*s1*s1*s2)

    k10 = (f311*f332*s2*s2*s3)

    k11 = ( (dim-2)*f311*f311*s1*s2*s2*s2)/(s3)

    k12 = ((dim-2)*f311*f312*s1*s2*s2)

    k13 = ((dim-2)*f312*f212*s1*s1*s3)

    k14 = ((dim-2)*f312*f332*s2*s3*s3)

    k15 = ((dim-2)*f312*f311*s1*s2*s2)

    k16 = ((3*dim - 8)*f312*f312*s1*s2*s3)

    # Numerically Evaluated Amplitude squared ( Normalised ) 

    amp_psd = (k1+k2+k3+k4+k5+k6+k7+k8+k9+k10+k11+k12+k13+k14+k15+k16)/(4)


    # Analytics expression for Amplitude Squared ( Normalised )  : We also substittue eps = 0 here

    amp_analytic =  (4*( (hmass*hmass*hmass*hmass*hmass*hmass*hmass*hmass) + (s1*s1*s1*s1) + (s2*s2*s2*s2) + (s3*s3*s3*s3) ))/(9*s1*s2*s3*(topmass*topmass*topmass*topmass))

    # Print Amplitude Squared ( Normalised ) results : 

    print('---------------------------------------------------------------')
    print('Numerical Result of The Normalized Ampltiude Squared with the above Form Factors in the heavy top quark limit')
    print('---------------------------------------------------------------')
    print('| M_(g g -> g H) |^2 : ', amp_psd)
    print('---------------------------------------------------------------')
    print('Multiply Above Number with ( ( Nc*(Nc^2 -1) )*(topmass^4)*(alpha_S^3) / pi*(v^2) )  To Get The Final Ampltiude Squared, which can then be averaged over colors and gluon polraisations ')
    print('---------------------------------------------------------------')
 
    print('---------------------------------------------------------------')
    print('Analytic Result of The Normalized Ampltiude Squared in the heavy top quark limit')
    print('---------------------------------------------------------------')
    print('| M_(g g -> g H) |^2 : ', amp_analytic)
    print('---------------------------------------------------------------')
    print('Multiply Above Number with ( ( Nc*(Nc^2 -1) )*(topmass^4)*(alpha_S^3) / pi*(v^2) )  To Get The Final Ampltiude Squared, which can then be averaged over colors and gluon polraisations ')
    print('---------------------------------------------------------------')
    print('Both Numerical and Analytic Amplitudes have been eveluated at these conditions :  [ s12, s13, s23, topmass^2, hmass^2 ]  = [ ',s1,', ',s2,', ',s3,', ',(topmass*topmass),', ',(hmass*hmass),' ]')
    print('---------------------------------------------------------------')
















