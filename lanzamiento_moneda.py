from numpy.random import seed 
from numpy.random import randint 

seed(1234)

lanzamientos=randint(0,2,1000000)

print(sum(lanzamientos/100000))
