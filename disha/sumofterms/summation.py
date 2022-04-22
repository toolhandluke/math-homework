#!/usr/bin/python

import argparse

parser=argparse.ArgumentParser(description='parse our three args')
parser.add_argument('--firstterm', type=int, default=None)
parser.add_argument('--lastterm', type=int, default=None) 
parser.add_argument('--common_difference', type=int, default=None)
parser.add_argument('--number_of_terms', type=int, default=None)
args = parser.parse_args()

if not common_difference in args::
  args.common_difference =1

sum = 0
for i in range(args.firstterm,args.lassterm,args.common_difference):
  print i
  if not i % 3:
    sum += i
  elif not i % 5:
    sum += i


print("total sum of numbers that are multiples of three or multiples of five: %d" % sum)
