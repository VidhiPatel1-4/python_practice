# User Validation

first_name=input("Enter First Name: ")
if first_name.isalpha():
    if len(first_name)>=3 and len(first_name)<=10:
        print("First Name:", first_name)
    else:
        print("invalid name")
elif first_name.isalnum():
    print("Number are not allow")
elif first_name.isalpha() == False or first_name.isalnum() == False:
    print("NNot valid")

else:
    print("not valid")

















