class data:
        def __init__(self,name,rno):
                self.__name=name
                self.__rno=rno
        def m(self): 
                print(self.__name)
                print(self.__rno)
st1=data('a',1001)
print(st1.__name)
st1.m()

     
