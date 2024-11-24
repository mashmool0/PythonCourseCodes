lst = []
tpl = ()
sets = {}
dictionary = {}



dictionary = {
    "amir":"amir1234",
    "aylar":"aylar1234",
    "diba":"diba1234",
}

# print(dictionary.get('diba'))

username = input('enter you username please :')
password = input('enter your password please : ')
for item in dictionary : 
    if item == username : 
        if password == dictionary.get(username) : 
            print('welcome')
        else : 
            print('your password is wrong !!!!')
