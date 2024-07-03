
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
num3 = int(input("Enter Third Number:"))

if num1 > num2 and num1 > num3:
    print(num1, "Num1 is greater")

elif num2 > num3 and num2 > num1:
    print(num2, "Num2 is greater")

elif num1 == num2 or num2 == num3 or num3 == num1:
    print("Any Two or Three Numbers are same")
else:
    print(num3, "Num3 is greater")


