import time 
import numpy as np

star = time.time()

vector = np.arange(0,1_000_000_000)
np.sum(vector)

print (time.time() - star)