#!/usr/bin/env python3

import urllib2

response = urllib2.urlopen( 'http://yusure.cn' )

print( response.read() )