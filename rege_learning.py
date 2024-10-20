import re 


pattern=r'^09[0-9]{9}$'

# \w -> har harfi mitone bashe 
# *  -> 0ta ela bishtar 
# ^  -> noghte shoro 
# $  -> noghte payan 

phone = '09162750548'
if phone.startswith('09') : 
    phone = '+98'+phone[1:]
print(phone)
print(re.match(pattern,'09162750548'))


