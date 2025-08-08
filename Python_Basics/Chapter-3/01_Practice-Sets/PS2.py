# Write a program to fill in a letter template given below with name and date. letter = ''' Dear <|Name|>, You are selected! <|Date|> '''

name = input("Enter Your Name : ")
date = input("Enter Date : ")
print("Method 1")
print(f'''
Dear {name},
You are selected!
{date}''')
      

# Can also be done with another method 
print("Method 2")
letter = letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))