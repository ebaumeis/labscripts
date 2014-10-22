#! /usr/bin/env python

import sys
import numpy as np

def rowprint(infile, stepmin, stepmax, outfile):
  data = np.loadtxt(infile)
  outfile = open(outfile, 'w')
  for x in range(int(stepmin),int(stepmax)):
    for y in range((data.shape[1]-1)/2):
      outfile.write('0 0 ' + repr(data[x,2*y+1]) + ' ' + repr(data[x,2*y+2]) + ' ')
    outfile.write('\n')


def main():
  rowprint(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == '__main__':
  main()
