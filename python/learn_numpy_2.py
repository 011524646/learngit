import numpy as np
a=np.arange(6).reshape(2,3)
b=np.arange(2,13,2).reshape(2,3)
try:
    print(a@b)
except ValueError as e:
    print("ValueError:", e)
try:
    print(a@b.T)
except ValueError as e:
    print("ValueError:", e)
try:
    print(np.dot(a,b))
except ValueError as e:
    print("ValueError:", e)
try:
    print(np.dot(a,b.T))
except ValueError as e:
    print("ValueError:", e)  
try:
    print(a*b)
except ValueError as e:
    print("ValueError:", e)
try:
    print(a*b.T)
except ValueError as e:
    print("ValueError:", e)   

print(np.concatenate([a, b], axis=0))
print(np.concatenate([a, b], axis=0).shape)
print(np.concatenate([a, b], axis=1))
print(np.concatenate([a, b], axis=1).shape)
print(np.stack([a, b], axis=0)) 
print(np.stack([a, b], axis=0).shape)
print(np.stack([a, b], axis=1))
print(np.stack([a, b], axis=1).shape)
print(np.vstack([a, b])) 
print(np.vstack([a, b]).shape) 
print(np.hstack([a, b]))
print(np.hstack([a, b]).shape)