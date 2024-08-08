
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
num3 = int(input("Enter Third Number:"))

if num1 >= num2 and num1 >= num3:
    print(num1, "is greater")

elif num2 >= num3 and num2 >= num1:
    print(num2, "is greater")

else:
    print(num3, "is greater")


print()
num1 = float(input("Enter First Number:"))
num2 = float(input("Enter Second Number:"))
num3 = float(input("Enter Third Number:"))

if num1 > num2:
    if num1 > num3:
        print(num1, "is greater")
    else:
        print(num3, "is greater")

elif num2 > num3:
    print(num2, "is greater")

else:
    print(num3, "is greater")

