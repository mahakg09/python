
x=4
def hello():
    
    y=5
    global x
    x=9
    print("this is global ",x)
    print("this is local",y)
    print(y+5)
hello()
print(x+2)
#print(y+2)