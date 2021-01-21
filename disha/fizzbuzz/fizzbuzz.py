#!/usr/bin/python

sum = 0
for i in range(1,1000):
  print i
  if not i % 3:
    sum += i
  elif not i % 5:
    sum += i


print("total sum of numbers that are multiples of three or multiples of ffive: %d" % sum)
