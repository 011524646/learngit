import torch
def f(a):
    b=a*3
    while(b.sum()<1000.0):
        b=b*2
    if(b.sum()>500):
        c=b*1
    else:
        c=b*2
    return c    

x=torch.arange(1,8.0,requires_grad=True)
y = x**2 + 2*x + 1
# y.sum().backward()
u = y.detach()
z = u*x
z.sum().backward()
print(x.grad)
y.sum().backward()
print(x.grad)
y1=f(x)
x.grad.zero_()
y1.sum().backward()
print(x.grad==y1/x)
#动手
x_=torch.arange(0,4.,requires_grad=True)
w_=torch.tensor([3.,5.,7.,9.],requires_grad=True)
b_=torch.tensor([1.,2.,3.,4.],requires_grad=True)
y_prd=x_*w_+b_
y_true=torch.tensor([0,8.,34.,88.])
loss=(y_prd-y_true)**2
loss.sum().backward()
a=0.01
while(loss.sum()>1):
    y_prd=x_*w_+b_
    loss=(y_prd-y_true)**2

    if w_.grad is not None:
        w_.grad.zero_()
    if b_.grad is not None:
        b_.grad.zero_()
    loss.sum().backward()    
    print("匹配:", torch.allclose(w_.grad, 2*(y_prd - y_true)*x_), torch.allclose(b_.grad, 2*(y_prd - y_true)))
    with torch.no_grad():          
        w_ -= a * w_.grad          
        b_ -= a * b_.grad
print(w_,b_)