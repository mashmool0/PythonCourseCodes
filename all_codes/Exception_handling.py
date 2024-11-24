import random 

#### Signup 
username = input('enter your username :')
password = input('eneter your password : ')
phone = input('enter you phone number please : ')

usernames_list = []

try : 
    with open('info.txt','r+') as f : 
        for line in f : 
            if line.startswith("*")  : 
                continue  
            # info.object.find(username=username)
except Exception as e : 
    print('doesent exist ')

# ==try : 
#     # every thing cheked : 
#     # username add database 
#     # phone add database 
#     # passwrd error 
# except : 
#     # pasho boro tooye databse chizia neveshti pak kon 
    
otp_code = random.randint(1000,9999)
print(otp_code)
check_otp = input('enter you otp code  :')

if otp_code == check_otp : 
    print(True)
     