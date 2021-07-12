# PSD_gggH1L
Numerical Evaluation of the Amplitude for gg->gH process at 1-Loop LO using pySecDec

gggH1L = Contains all the files Necessary for the Numerical Evaluation of the required Amplitude with pySecDec

Mathematica_Notebooks = Mathematica Notebooks which has my calculations for : 

F212_Factors.nb =  Calculation of P & T Coefficients for the Superposition of the Integrals in the Normalized F212 Form Factor 

F312_Factors.nb =  Calculation of M & N Coefficients for the Superposition of the Integrals in the Normalized F312 Form Factor 

Amplitude.nb = Calculation and Verififcation of the Normalized Amplitude Squared with the Evaluated Form Factors in the HTL-Heavy Top Limit 

# Calculation & Verification

In the gggH1L folder, Execute the following commands to Numerically Evaluate the required Normalized Amplitude and also verify our results with the Analytic results in the HTL-Heavy Top Limit

$ python3 generate_F212.py

$ make -C F212/

$ python3 generate_F312.py

$ make -C F312/

$ python3 integrate_gggH1L.py

# Sample Terminal Output

---------------------------------------------------------------

Numerical Results For All Normalized Form Factors :

Normalized F212 :  -4444.48518251155747  +/-  -2.11527169567566023e-8

Normalized F311 :  1481.49505980688878  +/-  -1.20887821577424775e-8

Normalized F332 :  -3010.66721212658194  +/-  -6.35160951246262322e-8

Normalized F312 :  -5973.69066900045254  +/-  -2.86999773502665581e-8

---------------------------------------------------------------

Analytic results of all Normalized Form Factors with heavy top quark limit

Analytic Result Normalized F212 : -4444.444444444444

Analytic Result Normalized F311 : 1481.4814814814813

Analytic Result Normalized F332 : -3010.63961923086

Analytic Result Normalized F312 : -5973.602582193822

---------------------------------------------------------------

---------------------------------------------------------------

Numerical Result of The Normalized Ampltiude Squared with the above Form Factors in the heavy top quark limit

---------------------------------------------------------------

| M_(g g -> g H) |^2 :  0.00261402286383048704

---------------------------------------------------------------

Multiply Above Number with ( ( Nc*(Nc^2 -1) )* (topmass^4)* (alpha_S^3) / pi*(v^2) )  To Get The Final Ampltiude Squared, which can then be averaged over colors and gluon polraisations 

---------------------------------------------------------------

---------------------------------------------------------------

Analytic Result of The Normalized Ampltiude Squared in the heavy top quark limit

---------------------------------------------------------------

| M_(g g -> g H) |^2 :  0.002613976041276658

---------------------------------------------------------------

Multiply Above Number with ( ( Nc*(Nc^2 -1) )* (topmass^4)* (alpha_S^3) / pi*(v^2) )  To Get The Final Ampltiude Squared, which can then be averaged over colors and gluon polraisations 

---------------------------------------------------------------

Both Numerical and Analytic Amplitudes have been eveluated at these conditions :  [ s12, s13, s23, topmass^2, hmass^2 ]  = [  0.0009 ,  -0.000442873775 ,  -0.0003 ,  1.0 ,  0.000157126225  ]

---------------------------------------------------------------

