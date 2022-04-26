#!/usr/local/bin/python3
import sys, getopt


def quadraticforX(x):
  print ("when X is %f, y is %f" % (x, (x*x)-(45*x)+324) )
  return (x*x)-(45*x)+324

highx=float(10)
lowx=float(5)
y=5 

count=0
while (abs(y) > float(0.00001)):
  x=(highx+lowx)/2
  print ("x is %f" % x)
  y=quadraticforX(x)
  if y < 0:
    highx=x
  else:
    lowx=x
  count+=1

print ("It took %d cycles" % count)


  
