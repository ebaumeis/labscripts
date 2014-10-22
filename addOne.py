#!/usr/bin/python

numbers = open('numbersIn.txt', 'r')
input = numbers.read()
output = open('numbersOut.txt','w')

for x in input.split('\n'):
  for no in x.split():
    num = int(no)
    newnum = (num + 1)
    newstr = str(newnum)
    output.write(newstr + " ")
  output.write('\n'+ '\n')
