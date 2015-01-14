#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys
from pylab import rcParams
rcParams['figure.figsize'] = 12,12


# Prints the 2D histogram as a png
def pngPrint(torsions, first, second, gqdIndex):
    H, xedges, yedges = np.histogram2d(torsions[int(first)-1], torsions[int(second)-1], bins=100)
    extent=[-20,25,-20,25]
    plt.imshow(H.T, extent=extent,interpolation='nearest',origin='lower', cmap=cm.BuGn)
    plt.savefig('gra%sTor%s%sCorr.png' % (gqdIndex, first, second))

# Creates a list of torsion arrays to be used by 
def loadTor(infile):
    tor1 = np.loadtxt(infile, usecols=[1])
    tor2 = np.loadtxt(infile, usecols=[2])
    tor3 = np.loadtxt(infile, usecols=[3])
    return [tor1, tor2, tor3]

def main():
    noGQDs = sys.argv[1]
    for x in range(1,int(noGQDs)+1):
        infile = 'internalTorsions.gra%s' % x
        tors = loadTor(infile)
        pngPrint(tors, 1, 2, x)
        pngPrint(tors, 2, 3, x)
        pngPrint(tors,1, 3, x)


if __name__ == '__main__':
  main()
