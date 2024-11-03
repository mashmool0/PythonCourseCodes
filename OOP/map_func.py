# map(function, iterable)

list_fullnames = []
with open('OOP/students_list','r') as f  : 
    for line in f : 
        if line.startswith("*") : 
            continue 
        else : 
            list_fullnames.append(line.strip())    



print(list_fullnames)
def remove_firsname(fname) : 
    return fname.split()[1]



print(list(map(remove_firsname,list_fullnames)))