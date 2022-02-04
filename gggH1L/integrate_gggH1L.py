from __future__ import print_function
from pySecDec.integral_interface import IntegralLibrary
from sympy import re,im, E, I
import sympy as sp
import math

scalef=1        # scale of topmass


topmass = 1.0                                # Actual top mass : 172.76 ± 0.3 GeV/c2  # topmass = 172.76
hmass = 0.012535                               # Actual Higgs Mass : 125.35 ± 0.15 GeV/c2
s1 = 0.0009*topmass*topmass                     # s1 = temporary variable for s12
s2 = -0.0003*topmass*topmass                    # s2 = temporary variable for s13
s3 = (hmass*hmass) - s1 - s2                 # s3 = temporary variable for s23


topmass = topmass*scalef
hmass = hmass*scalef
s1 = s1*scalef*scalef
s2 = s2*scalef*scalef
s3 = s3*scalef*scalef


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
    # amp.use_Qmc()  # Qmc doesnt work , try Vegas  # amp.use_Vegas()
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
    f212 = integral_with_prefactor.coeff('eps',0).coeff('value')
    f11 = re(f212)
    f12 = im(f212)
    f212_error = integral_with_prefactor_err.coeff('eps',0).coeff('error')
    f11_e = re(f212_error)
    f12_e = im(f212_error)

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
    f311 = integral_with_prefactor.coeff('eps',0).coeff('value')
    f21 = re(f311)
    f22 = im(f311)
    f311_error = integral_with_prefactor_err.coeff('eps',0).coeff('error')
    f21_e = re(f311_error)
    f22_e = im(f311_error)

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
    f332 = integral_with_prefactor.coeff('eps',0).coeff('value')
    f31 = re(f332)
    f32 = im(f332)
    f332_error = integral_with_prefactor_err.coeff('eps',0).coeff('error')
    f31_e = re(f332_error)
    f32_e = im(f332_error)

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
    f312 = integral_with_prefactor.coeff('eps',0).coeff('value')
    f41 = re(f312)
    f42 = im(f312)
    f312_error = integral_with_prefactor_err.coeff('eps',0).coeff('error')
    f41_e = re(f312_error)
    f42_e = im(f312_error)

    # examples how to access individual orders
    #print('Numerical Result')
    #print('eps^-2:', integral_with_prefactor.coeff('eps',-2).coeff('value'), '+/- (', integral_with_prefactor_err.coeff('eps',-2).coeff('error'), ')')
    #print('eps^-1:', integral_with_prefactor.coeff('eps',-1).coeff('value'), '+/- (', integral_with_prefactor_err.coeff('eps',-1).coeff('error'), ')')
    #print('eps^0 :', integral_with_prefactor.coeff('eps',0).coeff('value'), '+/- (', integral_with_prefactor_err.coeff('eps',0).coeff('error'), ')')
    
    # coefficients of eps^-1 and eps^-2 will be zero because we are dealing with non-divergent amplitude, so we only print and use the eps^0 coefficient    

    # print result
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Numerical Results For All Normalized Form Factors upto a phase factor :')
    print('Normalized F212 : ', f212 , ' +/- ', f212_error)
    print('Normalized F311 : ', f311 , ' +/- ', f311_error)
    print('Normalized F332 : ', f332 , ' +/- ', f332_error)
    print('Normalized F312 : ', f312 , ' +/- ', f312_error)

    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Analytic results of all Normalized Form Factors with heavy top quark limit')
    print('Analytic Result Normalized F212 :', output1)
    print('Analytic Result Normalized F311 :', output2)
    print('Analytic Result Normalized F332 :', output3)
    print('Analytic Result Normalized F312 :', output4)
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    


    ampsquared1 = ((1/2)*f11*f21*s1*s1*s2 + (1/2)*f12*f22*s1*s1*s2 + f21*f41*s1*s2*s2 + f22*f42*s1*s2*s2 + (f21*f21*s1*s2*s2*s2)/(2*s3) + (f22*f22*s1*s2*s2*s2)/(2*s3) + f11*f41*s1*s1*s3 + f12*f42*s1*s1*s3 + (f11*f11*s1*s1*s1*s3)/(2*s2) + (f12*f12*s1*s1*s1*s3)/(2*s2) + f41*f41*s1*s2*s3 + f42*f42*s1*s2*s3 + (1/2)*f21*f31*s2*s2*s3 + (1/2)*f22*f32*s2*s2*s3 + (1/2)*f11*f31*s1*s3*s3 + (1/2)*f12*f32*s1*s3*s3 + f31*f41*s2*s3*s3 + f32*f42*s2*s3*s3 +  (f31*f31*s2*s3*s3*s3)/(2*s1) + (f32*f32*s2*s3*s3*s3)/(2*s1))

    amp1re = (f11*s1*s1*(math.sqrt(-s3)))/(2*(math.sqrt(2))*(math.sqrt(s1*(-s2))))

    amp1im = (f12*s1*s1*(math.sqrt(-s3)))/(2*(math.sqrt(2))*(math.sqrt(s1*(-s2))))

    amp2re = (f21*s2*s2*(math.sqrt(s1)))/(2*(math.sqrt(2))*(math.sqrt(s2*(s3))))

    amp2im = (f22*s2*s2*(math.sqrt(s1)))/(2*(math.sqrt(2))*(math.sqrt(s2*(s3))))  

    amp3re = (f31*s3*s3*(math.sqrt(-s2)))/(2*(math.sqrt(2))*(math.sqrt((-s3)*(s1))))

    amp3im = (f32*s3*s3*(math.sqrt(-s2)))/(2*(math.sqrt(2))*(math.sqrt((-s3)*(s1))))

    amp4re = ((math.sqrt(s1*s2*s3))/(math.sqrt(2)))*((s1*f11)/(2*s2) + (s3*f31)/(2*s1) + (s2*f21)/(2*s3) + f41)

    amp4im = ((math.sqrt(s1*s2*s3))/(math.sqrt(2)))*((s1*f12)/(2*s2) + (s3*f32)/(2*s1) + (s2*f22)/(2*s3) + f42)

    ampsquared2 = 2*( ( (amp1re*amp1re) + (amp1im*amp1im)  ) + ((amp2re*amp2re) + (amp2im*amp2im)) + ((amp3re*amp3re) + (amp3im*amp3im)) + ((amp4re*amp4re) + (amp4im*amp4im))   )

    amp_analytic =  (4*( (hmass*hmass*hmass*hmass*hmass*hmass*hmass*hmass) + (s1*s1*s1*s1) + (s2*s2*s2*s2) + (s3*s3*s3*s3) ))/(9*s1*s2*s3*(topmass*topmass*topmass*topmass))
    
    
    
    
    amp1re_e = (f11_e*s1*s1*(math.sqrt(-s3)))/(2*(math.sqrt(2))*(math.sqrt(s1*(-s2)))) 
    
    amp1im_e = (f12_e*s1*s1*(math.sqrt(-s3)))/(2*(math.sqrt(2))*(math.sqrt(s1*(-s2))))
    
    amp2re_e = (f21_e*s2*s2*(math.sqrt(s1)))/(2*(math.sqrt(2))*(math.sqrt(s2*(s3))))

    amp2im_e = (f22_e*s2*s2*(math.sqrt(s1)))/(2*(math.sqrt(2))*(math.sqrt(s2*(s3))))  

    amp3re_e = (f31_e*s3*s3*(math.sqrt(-s2)))/(2*(math.sqrt(2))*(math.sqrt((-s3)*(s1))))

    amp3im_e = (f32_e*s3*s3*(math.sqrt(-s2)))/(2*(math.sqrt(2))*(math.sqrt((-s3)*(s1))))
    
  
    
  
    
    # ((s1*f11)/(2*s2) + (s3*f31)/(2*s1) + (s2*f21)/(2*s3) + f41)   
    
    sig1 =  (s1*f11_e)/(2*s2)
    
    sig2 =  (s3*f31_e)/(2*s1)
    
    sig3 =  (s2*f21_e)/(2*s3)
    
    sig4 =  f41_e
    
    amp4re_e = ((math.sqrt(s1*s2*s3))/(math.sqrt(2)))*(math.sqrt( (sig1)*(sig1) + (sig2)*(sig2) + (sig3)*(sig3) + (sig4)*(sig4)     ))    
    
    sig1 =  (s1*f12_e)/(2*s2)
    
    sig2 =  (s3*f32_e)/(2*s1)
    
    sig3 =  (s2*f22_e)/(2*s3)
    
    sig4 =  f42_e
    
    amp4im_e = ((math.sqrt(s1*s2*s3))/(math.sqrt(2)))*(math.sqrt( (sig1)*(sig1) + (sig2)*(sig2) + (sig3)*(sig3) + (sig4)*(sig4)     ))          
    
    
    
    ampsquared2_e = 2*math.sqrt(  ( (2*amp1re*amp1re_e)*(2*amp1re*amp1re_e)  ) +  ( (2*amp2re*amp2re_e)*(2*amp2re*amp2re_e)  ) + ( (2*amp3re*amp3re_e)*(2*amp3re*amp3re_e)  ) + ( (2*amp4re*amp4re_e)*(2*amp4re*amp4re_e)  ) + ( (2*amp1im*amp1im_e)*(2*amp1im*amp1im_e)  ) + ( (2*amp2im*amp2im_e)*(2*amp2im*amp2im_e)  ) + ( (2*amp3im*amp3im_e)*(2*amp3im*amp3im_e)  ) + ( (2*amp4im*amp4im_e)*(2*amp4im*amp4im_e)  )  )
    
    
    error_percent = (  (ampsquared2-amp_analytic)/(amp_analytic)  )*100

    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Numerical Result of The Helicity Amplitudes upto a phase factor, with the above Form Factors : ')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' M++-  : ', amp1re,'+I*(',amp1im,')   Re_e',amp1re_e,'  Im_e', amp1im_e)
    print(' M+-+  : ', amp2re,'+I*(',amp2im,')   Re_e',amp2re_e,'  Im_e', amp2im_e)
    print(' M-++  : ', amp3re,'+I*(',amp3im,')   Re_e',amp3re_e,'  Im_e', amp3im_e)
    print(' M+++  : ', amp4re,'+I*(',amp4im,')   Re_e',amp4re_e,'  Im_e', amp4im_e)
    print('                                                                                                                                                                                             ')
    print(' The Other 4 Helicity Amplitudes are Identical to the above ones, upto a phase factor ')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Numerical Result of The Normalized Ampltiude Squared with full top-quark mass dependance : ')
    print('                                                                                                                                                                                             ')
    print('| M_(g g -> g H) |^2 : ', ampsquared2,'  +/-  ',ampsquared2_e) 
    print('                                                                                                                                                                                             ')
    print('   % Numerical uncertainty = ',((ampsquared2_e*100)/ampsquared2),'  ||  % Deviation w.r. to Analytic result in HTL :',error_percent)
    print('                                                                                                                                                                                             ')
    print('Multiply above amplitude with ((Nc*(Nc^2 -1))*(topmass^4)*(alpha_S^3)/pi*(v^2)) To Get The Final Ampltiude Squared, which can then be averaged over colors and gluon polraisations ')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Analytic Result of The Normalized Ampltiude Squared in the heavy top quark limit')
    print('                                                                                                                                                                                             ')
    print('| M_(g g -> g H) |^2 : ', amp_analytic)
    print('                                                                                                                                                                                             ')
    print('Multiply Above Number with ( ( Nc*(Nc^2 -1) )*(topmass^4)*(alpha_S^3) / pi*(v^2) )  To Get The Final Ampltiude Squared, which can then be averaged over colors and gluon polraisations ')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Both Numerical and Analytic Amplitudes have been evaluated at these conditions : ')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' [ s12, s13, s23, topmass^2, hmass^2 ]  = [ ',s1,', ',s2,', ',s3,', ',(topmass*topmass),', ',(hmass*hmass),' ]')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' topmass = ',topmass, '  |  hmass = ', hmass,' |  s1/(topmass^2) = ' , s1/(topmass*topmass),' |  s2/(topmass^2) = ' , s2/(topmass*topmass), ' |  s3/(topmass^2) = ' , s3/(topmass*topmass))
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
   
   # Print following for form factor errors 
   
 #   print('F212 errors :',f11_e,', Im error : ',f12_e)
 #   print('F311 errors :',f21_e,', Im error : ',f22_e)
 #   print('F332 errors :',f31_e,', Im error : ',f32_e)
 #   print('F312 errors :',f41_e,', Im error : ',f42_e)
   

    # 'F212 errors :',f11_e,' and Im error : ',f12_e
    
   















