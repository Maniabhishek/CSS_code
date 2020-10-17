class MyClass:
    
    def __init__(self,a,b):
        self.var1=a
        self.var2=b
    
    # def __str__(self):
    #     return "".join("abh")
    def __repr__(self):
        return '{var1:'+str(self.var1)+'}'


myobject=MyClass(1,2)
myobject=MyClass(2,3)
print(myobject)