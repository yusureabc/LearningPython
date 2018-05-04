#!/usr/bin/env python3

height = input( 'Please enter your height (m):' )
weight = input( 'Please enter your weight (kg):' )

height = float( height )
weight = float( weight )

bmi = weight / pow( height, 2 )

if bmi <= 18.5:
    print( '过轻' )
elif bmi <= 25:
    print( '正常' )
elif bmi <= 28:
    print( '过重' )
elif bmi <= 32:
    print( '肥胖' )
elif bmi > 32:
    print( '严重肥胖' )