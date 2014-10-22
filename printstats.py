#! /usr/bin/env python

import numpy as np
import scipy.stats
import sys

def stats(infile, column, minstep, maxstep):
  x = [int(column)]
  data = np.loadtxt(infile, usecols=(x),skiprows=1)
  a = int(minstep)
  b = int(maxstep)  
  segment = data[a:b]
  return repr(np.mean(segment)) + ' ' + repr(2*1.96*scipy.stats.sem(segment))

def rows(infile, outfile):
  out = open(outfile,'w')
  data = np.loadtxt(infile,skiprows=1)
  for x in range(1,data.shape[1]):
    out.write(stats(infile,x,0,-1) + ' ' + repr(x) + '-' + repr(x+1) + '\n')

def main():
  rows(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
  main()
