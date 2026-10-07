import numpy as np
a=np.arange(10)
b=np.zeros((4,5))
e=np.eye(4)
t1=np.random.rand(1,2)
t2=np.linspace(0,1,4)
i=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(a.dtype)
print(b.dtype)
print(e.dtype)
print(t1.dtype)
print(t2.dtype)
print(i.dtype)
print(i.reshape(9).shape, i.reshape((3,3)).T.shape)
print(i[0:2, 1:3])
#动手:
test=np.random.rand(4,5)
print(test.sum(axis=0))#求列和
print(test.sum(axis=1))#求行和
print(test[test>0.5])
print(test.sum(axis=0)[test.sum(axis=0)>0.5])