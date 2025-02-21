def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
obj1=fibonacci(4)
print("fibonaaci of 4 is",obj1)