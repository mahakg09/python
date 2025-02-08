a=input()
b=input()
#if a.sort() == b.sort():
#sort()-works on list and also sort(),doest not return a new lost ,it sorts the list in place and returns NONE
#if u want to use sort() with strings ,first u need to convert
if sorted(a) == sorted(b):
    
    print("is anagram")
else:
    print("not anagram")