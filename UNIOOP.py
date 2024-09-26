class Person:
    university = "SBU"
    
    # Constructor
    def __init__(self,full_name,age,sex,codeID) : 
        self.full_name = full_name
        self.age = age 
        self.sex = sex 
        self.codeID = codeID
    
    def check_age(self):
        if self.age < 18 : 
            return 'genius'
                

# Inheritance 
class Teacher(Person):
    
    def __init__(self, full_name, age, sex, codeID,role):
        super().__init__(full_name, age, sex, codeID)
        self.role = role
        
class Student(Person):
    def __init__(self, full_name, age, sex, codeID,paye):
        super().__init__(full_name, age, sex, codeID)
        self.paye = paye

t1 = Teacher('AmirMashayekhi',20,'Man','3020','Fizik1')
print(t1.full_name)



