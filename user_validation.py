# User Validation

first_name = input("Enter First Name: ")
num = ('0','1','2','3','4','5','6','7','8','9')

invalid_name = False

for i in first_name:
    if i in num:
        invalid_name = True
        break

if invalid_name:
    print("invalid name")
else:
    print("first name:", first_name)








