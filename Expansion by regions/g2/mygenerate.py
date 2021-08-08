#!/usr/bin/env python3

# in this example we try to expand the dotted loop using the mass of the particle
# in the loop as the small parameter
# here we do it both ways, expaning in the msq directly, or replacing it by
# z*msq, expanding in z and then using z=1, here we use 2 Feynman parameters
# (i.e. we have two propagators and a powerlist)

from pySecDec.loop_integral import loop_regions
from pySecDec.code_writer import sum_package
import pySecDec as psd
import numpy as np

# define the loop integral for the case where we expand in m
set1 = [       ('p1*p1', '0'),
                            ('p2*p2', '0'),
                            ('p3*p3', '0'),
                            ('p1*p2', '(s12)/2'),
                            ('p1*p3', '(s13)/2'),
                            ('p2*p3', '(s23)/2'),
                            ('mt**2','mtsq'),
                            ('(p1*p2)+(p2*p3)+(p1*p3)','(mhsq)/2')
                        ]

li_m =   psd.loop_integral.LoopIntegralFromPropagators(

    

    propagators = ['(k1)**2 - (mt)**2', '(k1-p1)**2 - (mt)**2', '(k1-p1-p2)**2 - (mt)**2 ', '(k1-p1-p2-p3)**2 - (mt)**2 '],
    loop_momenta = ['k1'],
    external_momenta = ['p1','p2','p3'],
    powerlist = ['2', '0', '1', '0'],

    regulators=['eps'],

    replacement_rules = set1,

    dimensionality= '4-2*eps'

    )

# define the loop integeral for the case where we expand in z
li_z = psd.loop_integral.LoopIntegralFromPropagators(
propagators=li_m.propagators, loop_momenta=li_m.loop_momenta, regulators=li_m.regulators, powerlist=li_m.powerlist,
replacement_rules = [       ('p1*p1', '0'),
                            ('p2*p2', '0'),
                            ('p3*p3', '0'),
                            ('p1*p2', '(s12*z)/2'),
                            ('p1*p3', '(s13*z)/2'),
                            ('p2*p3', '(s23*z)/2'),
                            ('mt**2','mtsq'),
                            ('(p1*p2)+(p2*p3)+(p1*p3)','((mhsq)*z)/2')
                        ])

order=1

# ['s12','s13','s23','mtsq','mhsq','z']

name = "g2_s12_z"
real_parameters = ['s12','s13','s23','mtsq','mhsq','z']
smallness_parameter = "z"
li = li_z

# find the regions and expand the integrals using expansion by regions
generators_args = loop_regions(
     name = name,
     loop_integral=li,
     smallness_parameter = smallness_parameter,
     expansion_by_regions_order=order)

# generate code that will calculate the sum of all regions and all orders in
# the smallness parameter
sum_package(name, generators_args, li.regulators,
     requested_orders = [1],
     real_parameters = real_parameters,
     complex_parameters = [])








