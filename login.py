list_users = ['amir','aylar','diba']
# define a function -> inputs - > username password       username ->unique (list_users)  and len of password more than 8 


def login(username,passwrod) : 
    if username in list_users or len(passwrod) < 8 :
        print("your password or username is wrong") 
        return 'your password or username is wrong'
    
    
    return 'welcome'

while True  : 
    user = input('enter your username : ')
    pass_user = input('enter your password : ')
    
    res = login(passwrod=pass_user,username=user)
    print(login(passwrod=pass_user,username=user))
    if res == 'welcome' : 
        break

