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

while True:
    new_numbers =input("enter your number or type exit : ")
    if new_numbers.isdigit() : 
        list_numbers.append(int(new_numbers))
    else  :
        break
    
print ("sorted list = ",sort_list(list_numbers))

