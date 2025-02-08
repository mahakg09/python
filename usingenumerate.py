a=input()
b="aeiouAEIOU" 
for index,i in enumerate(a):
    if i in b:
        print(i,"at",index)