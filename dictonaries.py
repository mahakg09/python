dict1={"name":"mahak garg",
       "age":22,
       "address":"teresa bhawan A"
       } 
print(dict1)
print("your name is", dict1["name"] , "and your age is", dict1["age"])
dict2={1:"anil",
       2:"sunil",
       3:"mohan",
       4:"neha",
       5:"hema"
       }
print("employee of the month goes to ",dict2[4])
print("employee of the month goes to ",dict2.get(4))

print("employee of the month goes to ",dict2.get(10))
# print("employee of the month goes to ",dict2[10])
print(dict1.keys())
print(dict1.values())

for i in dict2.keys():
    print(dict2[i])
for j in dict2.keys():
    print("the value corresponding to key ",j,"is ",dict2[j])
print(dict2.items())
print(dict1.items())

dict1.update(dict2)
print(dict1)
dict1.update({"age":21})
print(dict1)
dict2.clear()
print(dict2)
dict1.pop(5)
print(dict1)
dict1.popitem()
print(dict1)
del dict2
del dict1["address"]
print(dict1)