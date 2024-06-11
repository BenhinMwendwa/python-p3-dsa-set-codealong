class MySet:

    def __init__(self,enumarable=[]):
       self.dictionary={}
       for values in enumarable:
        self.dictionary[values]=True
        
    def has(self,value):
        return self.dictionary[value]    
    
    def add(self,value):
        self.dictionary[value]=True
        
        return self
    
    def remove(self,value):
        del self.dictionary[value]
        return self
    
    def size(self):
        return len(self.dictionary)
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

 
set1 =MySet([1,2,3,4,5])

print(set1.dictionary)

set1.add(6)

print(set1.dictionary)

set1.delete(4)

print(set1.dictionary)

    
