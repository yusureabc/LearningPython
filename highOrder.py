#!/usr/bin/env python3

def add( x, y, f ):
    return f( x ) + f( y )

print( add( -5, 6, abs ) )