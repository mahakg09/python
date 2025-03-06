class Sample:
    show1="i am public ! i am accessible from everywhere"
    _show2="i am protected ! oops but actually not protected"
    __show3="i am fully private ! i lead to name mangling in python" 
    
    def display(self):
        print(f"{self.show1}")
        print(f"{self._show2}")
        print(f"{self.__show3}") 
        
obj1=Sample()
# obj1.display()
print(obj1._show2)
print(obj1.show1) 
# print(obj1.__show3)#will give AttributeError
print(obj1._Sample__show3) # now will give correct output 