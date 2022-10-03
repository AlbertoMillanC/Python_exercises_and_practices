

import pandas as pd
import numpy as np
cols = 4
rows = 3
np.random.seed(0)
pd.DataFrame(np.random.rand(rows, cols))



#  0         1         2         3

# 0  0.548814  0.715189  0.602763  0.544883

# 1  0.423655  0.645894  0.437587  0.891773

# 2  0.963663  0.383442  0.791725  0.528895

 



 

# pd.DataFrame(np.random.randint(0, 1000, (rows, cols)), columns=['A', 'B', 'C', 'D'])

 

# A    B    C    D

# 0   91  896  398  611

# 1  565  908  633  938

# 2   84  203  324  774

