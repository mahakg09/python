# def say():
#     print("this is the say function") 
def myfunc(fuc):
    def display():
        print("this is  begining of say function")
        fuc()
        print("the end after say function")
    return display 
#a=myfunc(say)
@myfunc
def say():
    print("this is the say function")
say()
