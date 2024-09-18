list_items = ['medad','khodkar','khodkar','daftar','pakkon','khodkar','khodkar']
list_items.pop(list_items.index('khodkar'))
print(list_items)


def clear_exc_one(list_items:list,word):
    count_word = 0 
    
    for item in list_items : 
        if item == word : 
            count_word += 1 

    for item in list_items : 
        if count_word == 1 : 
            break 
        elif item == word  : 
            list_items.pop(list_items.index(word))
            count_word -= 1 
    
    
    return list_items


    
new_list_items = clear_exc_one(list_items,'khodkar')
print(new_list_items)