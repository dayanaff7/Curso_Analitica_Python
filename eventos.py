import numpy as np
from numpy.random import seed 
from numpy.random import randint 


eventos=[]
for i in range(1,1000000): 
    eventos.append(sum(randint(0,2,10))/10)

print(eventos[1:10])


print(np.mean(eventos))