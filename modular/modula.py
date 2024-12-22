def inverse(a,b):
    for i in range(1,b+1):
        if (a*i)%b == 1:
            return i
    return None
print(inverse(3,13))