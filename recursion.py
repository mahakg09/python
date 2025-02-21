def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
obj1=factorial(3)
obj2=factorial(7)
obj3=factorial(4)
obj4=factorial(5)
obj5=factorial(6)
print("factorial is",obj1)
print("factorial is",obj2)
print("factorial is",obj3)
print("factorial is",obj4)
print("factorial is",obj5)