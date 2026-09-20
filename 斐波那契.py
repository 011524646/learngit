def a(n):
    a=1
    b=1
    for i in range(1,n-1):
        temp=a
        a=a+b
        b=temp
    return a