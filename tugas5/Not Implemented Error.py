class BaseClass(object): 
    def __init__(self): 
        super(BaseClass, self).__init__() 
    def do_something(self): 
        raise NotImplementedError(self.__class__.__name__ + '.try_something') 
  
class SubClass(BaseClass): 
    def do_something(self): 
        print (self.__class__.__name__ + ' trying something!')
  
SubClass().do_something() 
BaseClass().do_something() 