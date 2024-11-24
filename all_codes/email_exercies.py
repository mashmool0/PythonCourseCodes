# example@example.com       part 1 - > everything (@)  part 2 - > len(3-5) , part 3 - > only com 
example_email = 'amirmahdi@gmail.com'
parts_list = []

age = eval(input(''))
print(age)
if example_email.count('@') == 0 : 
    print('gheyr mojaz ')
else : 
    print('mojaz')

parts_list.append((example_email.split('@'))[0])
parts_list.append((((example_email.split('@'))[1]).split('.'))[0])
parts_list.append(example_email.split('@')[1].split('.')[1])
print(parts_list)

print('username is : ',parts_list[0])
print('service is : ',parts_list[1])
print('com : ',parts_list[2])

# for letter in example_email : 
#     if letter == '@' : 
#         parts_list.append(example_email[:example_email.index('@')])

# print(parts_list)
        