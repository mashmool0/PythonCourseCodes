check_entry = lambda entry :  entry * 10  if isinstance(entry,int) else entry * 0 


print("1.login")
print("2.signup")
print("3.exit")
entry = check_entry(input('enter your choice : '))

print(entry)
if entry == 0 : 
    print("please enter corret answer")

