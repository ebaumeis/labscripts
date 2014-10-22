#! /usr/bin/env python
# Script to take plumed output and calculate the distance between GQDs projected onto the normal of the first GQD
# 

import numpy as np
import sys
from operator import sub

def distProj(c1, c2, dist):
  normal = np.cross(c1, c2)
  lengthnorm = np.linalg.norm(normal)
  proj = np.dot(dist,normal)/lengthnorm
  return proj

def vectorRead(data, line):
  vectors = []
  for x in range(0,data.shape[1]/3):
    vectors.append([data[line,3*x+1],data[line,3*x+2],data[line,3*x+3]])
  return vectors

def printdata(inputfile, distOut):
  data = np.loadtxt(inputfile)
  distOut = open(distOut,'w')
  numberqds = (data.shape[1]-1)/9
  #for z in range(1,numberqds+1):
  #  if z == numberqds:
  #    distOut.write("dist%s%s" % (z, z+1))
  #  else:    
  #    distOut.write("dist%s%s" % (z, z+1) + ' ')
  #distOut.write('\n')
  for y in range(0,data.shape[0]):
    
    vectors = vectorRead(data,y)
    distOut.write(repr(data[y,0]) + ' ')
  
    for x in range(0,numberqds):
      proj = distProj(vectors[3*x],vectors[3*x+1],vectors[3*x+2])
      if x == (numberqds-1):
        distOut.write(repr(abs(proj)))
      else:
        distOut.write(repr(abs(proj)) + ' ')
    distOut.write('\n')
   
  distOut.close()

def main():
  printdata(sys.argv[1], sys.argv[2]+ ".dist")

if __name__ == '__main__':
  main()
