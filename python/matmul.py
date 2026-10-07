import numpy as np
def mtx_mtpl_0(a,b):
    ans=np.zeros((a.shape[0],b.shape[1]))
    for i in range(0,ans.shape[0]):
        for j in range(0,ans.shape[1]):
            ans[i,j]=(a[i,:]*b[:,j]).sum()
    return ans        
def mtx_mtpl_1(a,b):#三重循环
    ans=np.zeros((a.shape[0],b.shape[1]))
    for i in range(0,ans.shape[0]):
        for j in range(0,ans.shape[1]):
            total=0
            for k in range (b.shape[0]):
                total+=a[i,k]*b[k,j]
            ans[i,j]=total    
    return ans 
a=np.arange(12).reshape(4,3)
b=np.arange(15).reshape(3,5)
print(a@b)            
print(mtx_mtpl_0(a,b))
print(mtx_mtpl_1(a,b))