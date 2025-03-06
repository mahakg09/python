def show(*args):
    for i in args:
        print(f"hello ,{i}") 
show(4,7,2,1)  

def me(*nums,names):
    for i in nums:
        print(f"{i}->{names}") 
me(1,2,3,4,names="mahak") 

def me(name,*nums):
    for i in nums:
        print(f"{i}->{name}") 
me("mahak garg",1,2,3,4) 

def display(**dicts):
    print(dicts)
display(name="mahak",age=21)

def keywordargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}->{value}") 
keywordargs(name="sakshi",age=12,address="mumbai",marks=45) 

def show2(lang,*args,**kwargs):
    print("normal arguments",lang)
    print("positional arguments",args)
    print("keyword arguments",kwargs) 
show2("java",1,2,3,4,5,6,"mahak",age=98,classs="6A2")
    