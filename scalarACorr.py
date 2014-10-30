#! /usr/bin/env python

import numpy as np
import sys

# Uses scalar multiplication to calculate the autocorrelation of a list of scalars (use the other script for faster - this is just to compare my brute force method with the FFT method)
# column number should be in numpy column style (starting with TS as 0 column)


def list_prep(infile, column):
  infile = np.loadtxt(infile)
  numbers = []
  for x in range(1,infile.shape[0]):
    numbers.append(infile[x][int(column)])
  return numbers

def autocorrelation(lag, numbers, mean, variance):
  r_lag=0
  for x in range(0,len(numbers)-lag):
    r_lag = r_lag + numbers[x] * numbers[x+lag]
  r_normalized = r_lag/variance
  return r_normalized

def calc_mean(numbers):
  mean = sum(numbers)/len(numbers)
  return mean

def calc_variance(n_numbers):
  variance = 0
  for x in range(0,len(n_numbers)):
    variance = variance + n_numbers[x] * n_numbers[x]
  return variance

def main():
  numbers = list_prep(sys.argv[1], sys.argv[2])
  mean = calc_mean(numbers)
  n_numbers = [ (x - mean) for x in numbers]

  variance = calc_variance(n_numbers)

  output_name = sys.argv[1] + '.col' + sys.argv[2] + '.acf'
  output = open(output_name, 'w')
  for k in range(0,len(n_numbers)):
    output.write(repr(autocorrelation(k,n_numbers,mean,variance)) + '\n')

if __name__ == '__main__':
  main()
