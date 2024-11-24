def prime_numbers(num:int): 
    if num==1 or num == 0 : 
         return False
    elif num == 2  :
        return True
    
    for i in range(1,num//2,2):  
        if num%i==0:
            return False
  
    return True 


