import numpy as np
a=np.arange(5).reshape(5,1)
b=np.arange(4).reshape(1,4)
print(a.shape, b.shape, (a+b).shape)