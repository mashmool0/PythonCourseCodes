import os 

def check_user(username,password) : 
    with open('test.txt','r') as f : 
        for line in f : 
            if line.startswith('*') : 
                continue  
            else : 
                file_splited = line.split(',') 
                if file_splited[0] == username : 
                    if file_splited[1] == password : 
                        return True,"Successfully"  
                    else : 
                        return False , "Password Incorrect"
                else : 
                    return False , "User Doesn't Exist "

        
username = input('enter your username please:') 
password = input('enter your password please:')
check , message = check_user(username,password) 

if check : 
    print(message) 
else : 
    print(message)
    print('failed try again please (maybe you should signup) ')

