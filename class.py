class Giant:
    def __init__(self,name,health,heigh,color):
        self.name = name 
        self.health = health  
        self.heigh = heigh 
        self.color = color 
        self.company = 'xyz'
        
        
    def damage(self,value):
        self.health -= value 
    
    
giant1 = Giant('rado',200,'300cm','pink')
giant2 = Giant('xman',300,'350','blue')

print(giant1.health)
giant1.damage(100)
print(giant1.health)

name= 'amir'
