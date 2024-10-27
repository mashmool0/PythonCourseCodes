
def login(username,password) :
    with open('relational_database/Students.txt','r') as file :
        for line in file : 
            if line.startswith("*") : 
                continue 
            splited_data = line.split(',')
            if splited_data[0].strip() == username  and splited_data[1].strip() == password : 
                return True
        
    
    return False

def find_course(username):
    with open('relational_database/Students.txt','r') as file :
        for line in file : 
            if line.startswith('*') : 
                continue 
            splited_data = line.split(',')
            if splited_data[0].strip() == username : 
                code_id = splited_data[4]
            
    
    course_list = []
    with open('relational_database/Course_select_st.txt','r') as file : 
        for line in file : 
            if line.startswith('*') : 
                continue 
            splited_data = line.split(',')
            if splited_data[1] == code_id : 
                course_offer_id = splited_data[2]
            
        

while True : 
    print("enter your choice:")
    print('1.login')
    print('2.exit')
    user_input = int(input('enter your choice : '))
     
    if user_input == 1 : 
        username = input("enter your username please : ")
        password  = input('enter your password please : ')
        if login(username,password) : 
             print('what do you want to do (select please)')
             print("1.my course")
             print("2.my teacher course")
             
             
             user_input = input('enter your choice : ') 
             if user_input == 1 : 
                pass 
             elif user_input == 2  : 
                pass
             
             
        else : 
            print("Incorrect Passwrod or username")
        
    elif user_input == 2 : 
        break 
    
    else : 
        print("Please Enter Correct number ")
        continue





with open('relational_database/Students.txt','r') as f :    
    for line in f : 
        print(line.strip())