import random

########### Normal distribution ############
a = random.normalvariate(0, 1)
print(a)

arr = list('ABCDH')
a = random.choice(arr)
print(a)

########### Tokens / secret keys ############
import secrets
s = secrets.randbelow(3)
b = secrets.randbits(4)
print(f's: {s} and b: {b}')

import numpy as np
######### 3x3 array #########
n = np.random.rand(3, 3)
print(n)

######### 3x4 array #########
n = np.random.randint(0, 10, (3, 4))
print(n)

