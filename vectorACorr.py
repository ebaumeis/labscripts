#! /usr/bin/env python

import numpy as np
import sys

# Uses a dot product to calculate the autocorrelation of a list of vectors
# column number index is based on numpy column numbers - 0 for first set of vectors, etc.


def vector_prep(infile, column):
  #convert the input file into a matrix and extract the vectors
  infile = np.loadtxt(infile)
  vectors = []
  for x in range(1,infile.shape[0]):
    vectors.append([infile[x][3*int(column)+1],infile[x][3*int(column)+2],infile[x][3*int(column)+3]])
  return vectors

def autocorrelation(lag, vectors, mean, variance):
  x=1
  r_lag=0
  while (x+lag)<=len(vectors)-1:
    r_lag = r_lag + np.dot(vectors[x],vectors[x+lag])
    x=x+1
  r_normalized = r_lag/variance
  return r_normalized

def calc_mean(vectors):
  mean = tuple(map(lambda y: sum(y) / float(len(y)), zip(*vectors)))
  return mean

def calc_variance(n_vectors):
  variance = 0
  for x in range(0,len(n_vectors):
    variance = variance + np.dot(n_vectors[x],n_vectors[x])
  return variance

def main():
  vectors = vector_prep(sys.argv[1], sys.argv[2])
  mean = calc_mean(vectors)
  n_vectors = [np.subtract(x,mean) for x in vectors]

  variance = calc_variance(n_vectors)

  output = open(sys.argv[3], 'w')
  for k in range(0,len(n_vectors)):
    output.write(repr(autocorrelation(k,n_vectors,mean,variance)) + '\n')

if __name__ == '__main__':
  main()
