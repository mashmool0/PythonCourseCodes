users = {
    "user1": {"username": "alice", "is_admin": True},
    "user2": {"username": "bob", "is_admin": False},
    "user3": {"username": "charlie", "is_admin": True},
    "user4": {"username": "dave", "is_admin": False}
}

    

def checker(func) :
     
    def wrapper() : 
        if users["user2"]['is_admin'] : 
            func() 
        else : 
            print("you dont have access")

        
    
    
    return wrapper




def download_details() : 
    print("shoma mitavanid mohtava zir ra danlod konid  ")
    print("mohtava")
    
func_test = checker(download_details)
func_test()