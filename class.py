class Giant:
    type_of_giant = 'dragon'
    
    # Constructor 
    def __init__(self,name,power,health,heigh,color):
        self.name = name 
        self.power = power
        self.health = health  
        self.heigh = heigh 
        self.color = color 
        
    def damage(self,value):
        self.health = self.health - value

    def __str__(self) -> str:
        return f'name of giant  : {self.name} - power of giant {self.power}' 
    
    
# print(dir(Giant))   
giant1 = Giant("x",100,200,300,'red')
giant2 = Giant('y',300,200,350,'yellow')

print(giant1)
print(giant2)