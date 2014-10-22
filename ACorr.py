#!/usr/bin/env python
##TODO
# Restructure as a class/function
# add integral as a function of time
# add outputs like mean, sigma
# improve input: add timestep maybe even read from command line 
# add a "time column" in the output
# chk spo.curve_fit


### Imports
import argparse
import scipy as sp
import scipy.integrate as spi
import scipy.fftpack as spf
import scipy.optimize as spo
import sys

### Parser
parser = argparse.ArgumentParser(
  description = "Computes the autocorrelation of a column in a text file.",
  epilog = """
The code will output:
""",
  formatter_class = argparse.RawDescriptionHelpFormatter
  )

parser.add_argument(
  "inputfile",
  type = argparse.FileType('r'),
  help = 'Input file name.'
  )
parser.add_argument(
  "-c", "--column",
  type = int,
  default = 1,
  metavar = 'int',
  help = 'Column to process (default 1).'
)
parser.add_argument(
  "-l", "--lag",
  type = int,
  default = sp.inf,
  metavar = 'int',
  help = 'Maximum time lag (maximum possible value and default half of the data\
          lenght).'
)
parser.add_argument(
  "-s", "--skip",
  type = int,
  default = 0,
  metavar = 'int',
  help = 'Number of initial data lines to discard. Lines that start with a # are\
          already discarded (default 0).'
)

args = parser.parse_args()

###  Load the data (w/ error checks)
try:
  data = sp.loadtxt(args.inputfile.name, dtype=sp.float64, usecols=(args.column-1,))
except IndexError:
  sys.stderr.write("Column {} does not exist in file {}.\n"
                  .format(args.column,args.inputfile.name) )
  sys.exit(1)

data = data[args.skip:]
ndata = len(data)
if ndata == 0:
  sys.stderr.write("No point on running on an empty set.\n")
  sys.exit(2)

maxlag = args.lag  if (args.lag <= ndata//2)  else  ndata//2

### Compute autocorrelation
data -= data.mean()             # centering
FT = spf.rfft(data, n=2*ndata)   # zero-pad the array and FT
acf_raw = spf.irfft(FT * FT)[:maxlag]
inputdomain = sp.ones_like(data)
FT_mask = spf.rfft(inputdomain, n=2*ndata)
mask = spf.irfft(FT_mask * FT_mask)[:maxlag]
acf = acf_raw / mask
acf = acf / acf[0] if acf[0] != 0 else sp.zeros_like(acf)

### 
#x_acf    = sp.arange(maxlag)
#ExpFit   = lambda tau,x,y: (sp.exp(-x/tau) - y)
#t0,out = spo.leastsq(ExpFit, 1., args=(x_acf,acf), maxfev=int(1e5))

### Save
sp.savetxt(args.inputfile.name+".acf",acf)

### Print extra info to screen
NPoints  = "{:12d}".format(ndata)
#StrInteg = "{:12.4e}".format(spi.simps(acf))
#StrSum   = "{:12.4e}".format(sum(acf))
#StrTau   = "{:12.4e}".format(t0[0])
sys.stdout.write("Number of points  :"+NPoints+"\n")
#sys.stdout.write("Integral (Simpson):"+StrInteg+"\n")
#sys.stdout.write("Integral (Sum)    :"+StrSum+"\n")
#sys.stdout.write("Tau               :"+StrTau+"\n")

