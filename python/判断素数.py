def is_prime(n):
    if n>2:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    elif n==2:
        return True
    else:
        return False
a=int(input("请输入"))
print(is_prime(a))       