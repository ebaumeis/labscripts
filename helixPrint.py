#! /usr/bin/env python

import sys
import numpy as np

def rowprint(infile, stepmin, stepmax, outfile):
  data = np.loadtxt(infile)
  outfile = open(outfile, 'w')
  for x in range(int(stepmin),int(stepmax)):
    sum1 = sum2 = 0 
    for y in range((data.shape[1]-1)/2):
      outfile.write(repr(sum1) + ' ' + repr(sum2)+ ' ' + repr(data[x,2*y+1]) + ' ' + repr(data[x,2*y+2]) + ' ')
      sum1 = sum1 + data[x,2*y+1]
      sum2 = sum2 + data[x,2*y+2]
    outfile.write('\n')


def main():
  rowprint(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == '__main__':
  main()
