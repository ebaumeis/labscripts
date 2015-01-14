#! /usr/bin/python

import numpy as np
import sys

def makeList(infile, low, high):
  data1 = np.loadtxt(infile, usecols=([1]))
  data3 = np.loadtxt(infile, usecols=([3]))
  ts = np.loadtxt(infile, usecols=([0]))
  cutList = []
  for step in ts:
    if float(data1[step]) > float(low) and float(data1[step]) < float(high):
      cutList.append(data3[step])
  return cutList



def main():
  cutList = makeList(sys.argv[1], sys.argv[2], sys.argv[3])
  out = open(sys.argv[4], 'w')
  for item in cutList:
    out.write(str(item) + '\n')

  

if __name__ == '__main__':
  main()
