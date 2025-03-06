s={}
print(type(s))
print("hi")

b=set()
print(type(b))

c={"mahak",4,False,3,4,5,6}
print(c)
for i in c:
    print(i)
    
s1={1,2,3,4}
s2={3,4,5,6,7}
# print(s1.union(s2))
# print(s1,s2)
# s1.update(s2)
# print(s1,s2)
# print(s1.intersection(s2))
# print(s1,s2)
# s1.intersection_update(s2)
# print(s1,s2)
# print(s1.symmetric_difference(s2))
# print(s1,s2)
# s1.symmetric_difference_update(s2)
# print(s1,s2)
# print(s1.difference(s2))
# print(s1,s2)
# s1.difference_update(s2)
# print(s1,s2)
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
s1.add(9)
print(s1)
s1.remove(9)
print(s1)
a=s1.pop()
print(a)
s1.clear()
print(s1)
del s1
print(s1)
