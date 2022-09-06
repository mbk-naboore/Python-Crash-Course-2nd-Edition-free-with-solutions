import imports_part1
imports_part1.make_pizza("large", "ice", "milk", "chess")


import imports_part1 as pz_module
pz_module.make_pizza("small", "BBC sauce", "mushroom", "chess")


from imports_part1 import make_pizza
make_pizza(13, "meat", "chess")


from imports_part1 import make_pizza as mp
mp(15, "chicken", "chess")


from imports_part1 import *
make_pizza("medium", "ice", "milk", "chess")
# this is the least favorite way of doing this...
