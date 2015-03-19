#! /usr/bin/python
import sys


atom_types = {'C':'CG2R61', 'O':'OG311 ','H':'HGP1  '}
charges = {'C_inner':'0.000', 'O':'-0.529', 'H':'0.420', 'C_outer_up':'0.109', 'C_outer_down':'0.000', 'C_outer_corner_up':'0.105', 'C_outer_corner_down':'-0.004', 'C_inner_corner_charged':'0.008'}

def is_corner(index, ring_number):
  last_inner_index = sum([ 6+x*12 for x in range(0, ring_number)])
  ring_index = index - last_inner_index
  line_index = ring_index%(2*ring_number + 1)
  if line_index in [0,1,2,2*ring_number]:
    return True
  else:
    return False

def is_up(index, ring_number):
  last_inner_index = sum([ 6+x*12 for x in range(0, ring_number)])
  ring_index = index - last_inner_index
  line_index = ring_index%(2*ring_number + 1)
  if line_index%2 == 1 or line_index==0:
    return True
  else:
    return False

def is_outer_ring(index, number_of_rings):
  last_inner_index = sum([ 6+x*12 for x in range(0, number_of_rings)])
  if int(index) > last_inner_index:
    return True
  else:
    return False

def is_inner_charged(index, number_of_rings):
  second_to_last_inner_index = sum([ 6+x*12 for x in range(0, number_of_rings-1)])
  if int(index) > second_to_last_inner_index:
    if is_corner(index, number_of_rings-1) and is_up(index, number_of_rings-1):
      return True
  else:
    return False

def get_atomtype(index):
  character = index[0]
  if character == 'O' or character == 'H':
    return atom_types[character]
  else:
    return atom_types['C']

def get_charge(index, number_of_rings):
  if index[0] == 'O':
    return charges['O']
  elif index[0] == 'H':
    return charges['H']
  elif not is_outer_ring(int(index), number_of_rings):
    if is_inner_charged(int(index), number_of_rings):
      return charges['C_inner_corner_charged']
    else:
      return charges['C_inner']
  elif is_corner(int(index), number_of_rings):
    if is_up(int(index), number_of_rings):
      return charges['C_outer_corner_up']
    else:
      return charges['C_outer_corner_down']
  else:
    if is_up(int(index), number_of_rings):
      return charges['C_outer_up']
    else:
      return charges['C_outer_down']


def list_generator(number_of_rings):
  rings = index_generator(number_of_rings)
  atoms = {}
  counter = 0
  for x in range(0,len(rings)):
    for y in range(0,len(rings[x])):
      counter = counter + 1
      charge = get_charge(rings[x][y],number_of_rings)
      atomtype = get_atomtype(rings[x][y])
      name = str(rings[x][y])
      if len(name) == 1:
          name = name + '  '
      elif len(name) == 2:
          name = name + ' '        
      atoms[counter] = [name, atomtype, charge]
  return atoms
      

def index_generator(number_of_rings):
  counter = 0
  rings = []
  for x in range(0,number_of_rings+1):
    numbers = []
    for y in range(1,6+x*12+1):
      counter = counter + 1
      numbers.append(str(counter))
    rings.append(numbers)
  rings.append(['O%d' % x for x in range(1,(number_of_rings+1)*6)])
  rings.append(['H%d' % x for x in range(1,(number_of_rings+1)*6)])
  return rings

def get_bonds_list(number_of_rings):
  bonds = []
  rings = index_generator(number_of_rings)
  last_inner_index = sum([ 6+x*12 for x in range(0, number_of_rings)])
  # Find inner-ring carbon bonds
  for x in range(number_of_rings+1):
    for y in range(len(rings[x])-1):
      bonds.append((rings[x][y],rings[x][y+1]))
  # Find up-down carbon bonds
  for x in range(0,number_of_rings):
    current_ring = rings[x]
    next_ring = rings[x+1]
    ups = []
    downs = []
    for index in current_ring:
      if is_up(int(index), x):
        ups.append(index)
    for index in next_ring:
      if not is_up(int(index), x+1):
        downs.append(int(index))
    bonds += zip(ups,downs)
  # Outer carbon to oxygen bonds
  ups = []
  for index in rings[number_of_rings]:
    if is_up(int(index), number_of_rings):
      ups.append(index)
  bonds += zip(ups,rings[number_of_rings+1])
  # Oxygen to hydrogen bonds
  bonds += zip(rings[number_of_rings+1],rings[number_of_rings+2])
  return bonds

def print_file(number_of_rings, file_name):
  atoms = list_generator(number_of_rings)
  outfile = open(file_name, 'w')
  outfile.write('RESI GRAP\t0.00\n')
  outfile.write('GROUP\n')
  for atom in atoms:
    outfile.write('ATOM\t%s\t%s\t%s\n' % (atoms[atom][0], atoms[atom][1], atoms[atom][2]))
  bonds = get_bonds_list(number_of_rings)
  for bond in bonds:
    outfile.write('BOND\t%s\t%s\n' % (bond[0], bond[1]))
  outfile.close()


def main():
  print_file(int(sys.argv[1]), sys.argv[2])
  

if __name__ == '__main__':
  main()
