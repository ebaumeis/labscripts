#!/usr/bin/python
import sys
import numpy as np

# ARGUMENTS: <numbersfile> <plumedfile>
# Takes an input of the carbon indices of a GQD assembly (space delimited, with one newline character between the different GQDs) as the first argument and prints out a plumed input file that calculates the torsion between the selected carbons in the GQD
# input file should be in VMD indices, this automatically adds one to the VMD indices to get the correct plumed ones. The input file should have the indices of all the carbons, in order from the middle out (use the normal numbers.txt file for the stack - this script extracts the indices needed to calculate the torsion)
# EBau 10/20/14

def printComments(output):
  output.write('# plumed input file to print 6 internal torsions in GQDs' + 2*'\n')

# Takes input carbon indices and assigns the right carbons the right torsion numbers, then prints torsion indices
def printTorsionCarbons(gqds,output):
  y=0
  for x in gqds:
    nums = x.split()
    torslist = [[42,37,51,46],[39,52,48,43],[36,48,45,39],[37,42,46,51],[52,39,43,48],[45,39,36,48]]
    for t in range(len(torslist)):
      cList = [int(nums[x]) for x in torslist[t]]
      output.write('gra%dtors%d: TORSION ATOMS=%d,%d,%d,%d \n' % ((y+1),(t+1),cList[0],cList[1],cList[2],cList[3]))
    output.write('\n')
    y = y+1

def printPlumed(gqds,output):
  for y in range(1,len(gqds)+1):
    output.write('PRINT ARG=')
    for x in range(1,7):
      if x < 6:
        output.write('gra%stors%s,' % (y,x))
      else:
        output.write('gra%stors%s' % (y,x))
        output.write(' FILE=internalTorsions.gra%s' % y)
    output.write('\n')

def main():
  numbers = open(sys.argv[1], 'r')
  input = numbers.read()
  output = open(sys.argv[2],'w')
  gqds = input.split('\n')
  del gqds[-1]
  printComments(output)
  printTorsionCarbons(gqds,output)
  printPlumed(gqds,output)

if __name__ == '__main__':
  main()
