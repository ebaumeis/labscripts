#!/usr/bin/python
import sys
import numpy as np


# ARGUMENTS: <numbersfile> <plumedfile>
# Takes an input of the carbon indices of a GQD assembly (space delimited, with one newline character between the different GQDs) as the first argument and prints out a plumed input file that calculates the in plane vectors (for the 1.5 nm GQD) and the distance between the GQDs.
# input file should be in VMD indices, this automatically adds one to the VMD indices to get the correct plumed ones
# EBau 8/11/14

def printComments(output):
  output.write('### Prints a plumed driver file that calculates the torsion between the COMs of the GQDs ###' + 2*'\n')


def printlist(gqds,output):
  y=0
  for x in gqds:
    numlist = x.split()
    output.write('cgra%s: COM ATOMS={' % repr(y+1) )
    z=0
    for no in numlist:
      num=int(no)
      if z < len(numlist)-1:
        output.write(repr(num+1) + ' ')
      else:
        output.write(repr(num+1))
      z=z+1
    output.write('}')
    output.write('\n' + '\n')
    y=y+1

def printCarbons(gqds,output):
  for y in range(1,len(gqds)-2):    
    output.write('t%s: TORSION ATOMS=cgra%s,cgra%s,cgra%s,cgra%s' % (repr(y),repr(y), repr(y+1), repr(y+2), repr(y+3)) + '\n')
  output.write('\n')

def printPlumed(gqds,output):
  output.write('PRINT ARG=')
  for x in range(1,len(gqds)-2):
    output.write('t%s,' % (x))
  output.write(' FILE=COMtorsions')

def main():
  numbers = open(sys.argv[1], 'r')
  input = numbers.read()
  output = open(sys.argv[2],'w')
  gqds = input.split('\n')
  del gqds[-1]
  printComments(output)
  printlist(gqds,output)
  printCarbons(gqds,output)
  printPlumed(gqds,output)

if __name__ == '__main__':
  main()
