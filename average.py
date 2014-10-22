#! /usr/bin/env python

import numpy as np
import scipy.stats
import sys

def average(infile, minstep, maxstep):
  data = np.loadtxt(infile)
  for x in range(1,data.shape[1])
  a = int(minstep)
  b = int(maxstep)  
  segment = data[a:b]
  print repr(np.mean(segment)) + '\n'
  print repr(np.std(segment)) + '\n'
  print repr(scipy.stats.sem(segment))

def main():
  average(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


if __name__ == '__main__':
  main()
