def sort_list(lst):

    for i in range(len(lst)) : 
        count = 1 
        for j in range(len(lst)-1)  : # len - 2 = 2 
            if lst[j] > lst[j+1] : 
                lst[j+1] , lst[j] = lst[j] , lst[j+1]
            else :
                count += 1 
        
        if count == len(lst) : 
            break 
    
    return lst 



list_numbers =[]
# list = [5,10,15,20]
# i = 1 
# [15,20,10,5] j =1  
# [15,10,20,5] j = 2 
# [15,10,5,20] j = 3 
# [15,10,5,20] j = 4 
# i = 2
# [10,15,5,20] j = 1 
# [10,5,15,20] j =2



# [8,12,19,10] 1 
# [8,12,19,10] 2 
# [8,12,10,19] 3



 
while True:
    new_numbers =input("enter your number or type exit : ")
    if new_numbers.isdigit() : 
        list_numbers.append(int(new_numbers))
    else  :
        break
    
print ("sorted list = ",sort_list(list_numbers))

