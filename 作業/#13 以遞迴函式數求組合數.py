def C(n,k):
    if n==k or k==0:
        return 1
    else:
        return C(n-1,k)+C(n-1,k-1)
print(C(10,4))