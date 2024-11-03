class User : 
    
    def __init__(self,first_name,last_name) -> None:
        self.first_name = first_name 
        self.last_name = last_name 
    
    @property
    def fullname(self) : 
        return f'{self.first_name} {self.last_name}' 

    @fullname.setter 
    def fullname(self,name) :
        f,l = name.split(' ')
        self.first_name = f  
        self.last_name = l 
        
    @fullname.deleter 
    def fullname(self) :
        self.first_name = None 
        self.last_name = None 
        
        

user = User("amir",'msh')
print(user.fullname)
user.fullname = 'diba khajeh'
print(user.fullname)
del user.fullname
print(user.fullname)
