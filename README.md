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
