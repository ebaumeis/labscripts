#! /usr/bin/python

import sys
import numpy as np

# ARGUMENTS: <ALLnumbersfile> <plumedfile>
# Takes an input of all the atom indices of a GQD assembly (space delimited, with one newline character between the different GQDs) as the first argument and prints out a plumed input file that calculates the torsion between the cysteine residues on the GQD *MAKE SURE TO ADJUST SCRIPT FOR DIFFERENT CYSTEINE LOCATIONS*
# input file should be in VMD indices, this automatically adds one to the VMD indices to get the correct plumed ones. The input file should have the indices of all the carbons, in order from the middle out (use the normal numbers.txt file for the stack - this script extracts the indices needed to calculate the torsion)
# EBau 10/29/14

def printComments(output):
  output.write('# plumed input file to print the torsion between the cysteine edge groups' + 2*'\n')

# Takes input carbon indices and assigns the right carbons the right torsion numbers, then prints torsion indices
def printTorsionCarbons(gqds,output):
  y=0
  for x in gqds:
    nums = x.split()
    # ortho - 66, 102, 91, 69
    # para 
    torList = [66,102,91,69]
    cList = [int(nums[x]) for x in torList]
    output.write('gra%dcystor: TORSION ATOMS=%d,%d,%d,%d \n' % ((y+1),cList[0],cList[1],cList[2],cList[3]))
    output.write('\n')
    y = y+1

def printPlumed(gqds,output):
  output.write('PRINT ARG=')
  for x in range(1,len(gqds)+1):
    if x < len(gqds):
      output.write('gra%scystor,' % (x))
    else:
      output.write('gra%scystor' % (x))
  output.write(' FILE=cysteineTorsions')
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
