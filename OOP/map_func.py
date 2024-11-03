# map(function, iterable)

list_fullnames = []
with open('OOP/students_list','r') as f  : 
    for line in f : 
        if line.startswith("*") : 
            continue 
        else : 
            list_fullnames.append(line.strip())    



print(list(map(lambda str:str.split()[1],list_fullnames)))