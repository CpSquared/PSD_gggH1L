# PSD_gggH1L
Numerical Evaluation of the Amplitude for gg->gH process at 1-Loop using pySecDec

Project_Report.pdf = Full report about this project 

gggH1L = Contains all the files Necessary for the Numerical Evaluation of the gg -> gH Amplitude at 1-loop with pySecDec

Output_Summary_MgggH1L.txt  =  Sample Terminal Output for the amplitude 

Expansion by regions = Contains all the files to evaluate the master integrals using the expansion by regions method

Mathematica_Notebooks = Mathematica Notebooks which has my calculations for : 

F212_Factors.nb =  Calculation of P & T Coefficients for the Superposition of the Integrals in the Normalized F212 Form Factor 

F312_Factors.nb =  Calculation of M & N Coefficients for the Superposition of the Integrals in the Normalized F312 Form Factor 

Amplitude.nb = Calculation and Verififcation of the Normalized Amplitude Squared with the Evaluated Form Factors in the HTL-Heavy Top Limit 

# Calculation & Verification

In the gggH1L folder, Execute the following commands to Numerically Evaluate the required Normalized Amplitude and also verify our results with the Analytic results in the HTL-Heavy Top Limit OR directly execute script ./run_gggH1L.py 

$ python3 generate_F212.py

$ make -C F212/

$ python3 generate_F312.py

$ make -C F312/

$ python3 integrate_gggH1L.py

# Sample Terminal Output

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Numerical Results For All Normalized Form Factors upto a phase factor :

Normalized F212 :  3010.66721600844903 + 1.32733513865677428e-6*I  +/-  1.81975525712834469e-6 + 2.94094139706788525e-6*I

Normalized F311 :  -1481.49506135726369 - 1.53560514504725522e-6*I  +/-  4.14531956058173858e-6 + 4.16007884980495492e-6*I

Normalized F332 :  4444.4851822935434 + 2.84241443612274307e-6*I  +/-  4.46680050836521339e-6 + 4.87315651056906319e-6*I

Normalized F312 :  5973.69066566558831 - 9.4516467510339291e-7*I  +/-  3.08912201195222142e-6 + 4.21541207120105658e-6*I

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Analytic results of all Normalized Form Factors with heavy top quark limit

Analytic Result Normalized F212 : -3010.63961923086

Analytic Result Normalized F311 : 1481.4814814814813

Analytic Result Normalized F332 : -4444.444444444444

Analytic Result Normalized F312 : -5973.602582193824

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Numerical Result of The Helicity Amplitudes upto a phase factor, with the above Form Factors : 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 M++-  :  0.0349189260900273943 +I*( 1.53949653940504103e-11 )   Re_e 2.11062514607144603e-11   Im_e 3.41102180716831490e-11
 
 M+-+  :  -0.00387988067666719301 +I*( -4.02158932868882498e-12 )   Re_e 1.08561585395883516e-11   Im_e 1.08948115749930306e-11
 
 M-++  :  0.00845543174016138640 +I*( 5.40756471359922207e-12 )   Re_e 8.49788563720893589e-12   Im_e 9.27095952494016765e-12
 
 M+++  :  -0.00106406472966938725 +I*( -3.21323854706024750e-11 )   Re_e 3.472867900168732e-11   Im_e 4.9300797446312726e-11
                                                                                                                                                                                         
 The Other 4 Helicity Amplitudes are Identical to the above ones, upto a phase factor 
 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Numerical Result of The Normalized Ampltiude Squared with full top-quark mass dependance : 
                                                                                                                                                                                             
| M_(g g -> g H) |^2 :  0.00261402286601485264   +/-   2.9704756790973277e-12
                                                                                                                                                                                             
   % Numerical uncertainty =  1.13636178080794568e-7   ||  % Deviation w.r. to Analytic result in HTL : 0.00179132239375237961
                                                                                                                                                                                             
Multiply above amplitude with ((Nc*(Nc^2 -1))*(topmass^4)*(alpha_S^3)/pi*(v^2)) To Get The Final Ampltiude Squared, which can then be averaged over colors and gluon polraisations 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Analytic Result of The Normalized Ampltiude Squared in the heavy top quark limit
                                                                                                                                                                                             
| M_(g g -> g H) |^2 :  0.002613976041276658
                                                                                                                                                                                             
Multiply Above Number with ( ( Nc*(Nc^2 -1) )*(topmass^4)*(alpha_S^3) / pi*(v^2) )  To Get The Final Ampltiude Squared, which can then be averaged over colors and gluon polraisations 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Both Numerical and Analytic Amplitudes have been evaluated at these conditions : 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 [ s12, s13, s23, topmass^2, hmass^2 ]  = [  0.0009 ,  -0.0003 ,  -0.000442873775 ,  1.0 ,  0.000157126225  ]
 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 topmass =  1.0   |  hmass =  0.012535  |  s1/(topmass^2) =  0.0009  |  s2/(topmass^2) =  -0.0003  |  s3/(topmass^2) =  -0.000442873775
 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


