#! /usr/bin/env python

import numpy as np
import sys
from operator import sub

# Takes plumed distance and vectors input to calculate the cross product of the vector between the COMs of the GQDs and project that onto the GQD plane between them. 
# Inputs: plumed output file in format of vectors file (x y z from first plane vector, x y z from second plane vector, x y z from COM distance between GQD and the next)

# vectorRead takes a specified line in the data file and turns it to a list of vectors
def vectorRead(data, line):
  vectors = []
  for x in range(0,data.shape[1]/3):
    vectors.append([data[line,3*x+1],data[line,3*x+2],data[line,3*x+3]])
  return vectors

# arguments passed to calculations should be in the form of three element lists
def calculations(cA, cB, dist1, dist2):
  
  # calculate the cross product of the two distances 
  cross = np.cross(dist1,dist2)
  # calculate the three new axes based on the plane
  normal = np.cross(cA,cB)
  axis1 = cA
  axis2 = np.cross(normal, cA)
  # calculate the projection of the cross product of the two distances onto the plane normal
  s = np.dot(normal, cross)
  t1 = np.dot(axis1, cross)
  t2 = np.dot(axis2, cross) 
  # subtract the projection from the original distance cross product to get the projection on the plane
  rejection = (t1,t2)
  return rejection

def printdata(inputfile, distOut):
  data = np.loadtxt(inputfile)
  distOut = open(distOut,'w')
  numberqds = (data.shape[1]-1)/9 + 1 
  print numberqds
  for y in range(0,data.shape[0]):
    
    vectors = vectorRead(data,y)
    distOut.write(repr(data[y,0]) + ' ')
  
    for x in range(0,numberqds-2):
      proj = calculations(vectors[3*x],vectors[3*x+1],vectors[3*x+2],vectors[3*(x+1)+2])
      if x == (numberqds-1):
        distOut.write(repr(proj[0]) + ' ' + repr(proj[1]))
      else:
        distOut.write(repr(proj[0]) + ' ' + repr(proj[1]) + ' ')
    distOut.write('\n')
   
  distOut.close()

def main():
  printdata(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
  main()

