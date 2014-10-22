#!/usr/bin/python
import sys
import numpy as np


# ARGUMENTS: <numbersfile> <plumedfile>
# Takes an input of the carbon indices of a GQD assembly (space delimited, with one newline character between the different GQDs) as the first argument and prints out a plumed input file that calculates the in plane vectors (for the 1.5 nm GQD) and the distance between the GQDs.
# input file should be in VMD indices, this automatically adds one to the VMD indices to get the correct plumed ones
# EBau 8/11/14

def printComments(output):
  output.write('# plumed input file to print carbon vectors and distance between GQDs' + 2*'\n')


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

def distancePrint(gqds,output):
  for x in range(1,len(gqds)):
    output.write('cdist%s%s: DISTANCE ATOMS=cgra%s,cgra%s COMPONENTS' % (x, repr(x+1), x, repr(x+1)) + '\n')
  output.write('\n')

def printCarbons(gqds,output):
  y=1
  for x in gqds:
    z=0
    numlist = x.split()
    if y==len(gqds):    
      output.write('c%sa: DISTANCE ATOMS=%s,%s COMPONENTS' % (repr(y),repr(int(numlist[0])+1),repr(int(numlist[40])+1)) + '\n')
      output.write('#c%sb: DISTANCE ATOMS=%s,%s COMPONENTS' % (repr(y),repr(int(numlist[0])+1),repr(int(numlist[52])+1)) + '\n')
    else:
      output.write('c%sa: DISTANCE ATOMS=%s,%s COMPONENTS' % (repr(y),repr(int(numlist[0])+1),repr(int(numlist[40])+1)) + '\n')
      output.write('c%sb: DISTANCE ATOMS=%s,%s COMPONENTS' % (repr(y),repr(int(numlist[0])+1),repr(int(numlist[52])+1)) + '\n')
    y=y+1
  output.write('\n')

def printPlumed(gqds,output):
  output.write('PRINT ARG=')
  for x in range(1,len(gqds)):
    y=x+1
    if x < len(gqds)-1:
      output.write('c%sa.x,c%sa.y,c%sa.z,' % (x,x,x))
      output.write('c%sb.x,c%sb.y,c%sb.z,' % (x,x,x))
      output.write('cdist%s%s.x,cdist%s%s.y,cdist%s%s.z' % (x,y,x,y,x,y))
      output.write(',')
    else:
      output.write('c%sa.x,c%sa.y,c%sa.z,' % (x,x,x))
      output.write('c%sb.x,c%sb.y,c%sb.z,' % (x,x,x))
      output.write('cdist%s%s.x,cdist%s%s.y,cdist%s%s.z,' % (x,y,x,y,x,y))
      output.write('c%sa.x,c%sa.y,c%sa.z' % (x+1,x+1,x+1))
      output.write(' FILE=vectors')

def main():
  numbers = open(sys.argv[1], 'r')
  input = numbers.read()
  output = open(sys.argv[2],'w')
  gqds = input.split('\n')
  del gqds[-1]
  printComments(output)
  printlist(gqds,output)
  distancePrint(gqds,output)
  printCarbons(gqds,output)
  printPlumed(gqds,output)

if __name__ == '__main__':
  main()
