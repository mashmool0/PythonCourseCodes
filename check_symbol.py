str1 = 'P@#yn26at^&i5ve'
digit_count = 0
char_count = 0
symbol_count = 0 

 
for letter in str1 : 
    if letter.isdigit()  : 
        digit_count += 1 
    elif letter.isalpha() : 
        char_count += 1  
    else :  
        symbol_count += 1  

print("Chars :",char_count)
print("Digits : ",digit_count)
print('Symbol : ',symbol_count)
