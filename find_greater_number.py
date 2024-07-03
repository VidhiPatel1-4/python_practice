
A=int(input("Enter First Number:"))
B=int(input("Enter Second Number:"))
C=int(input("Enter Third Number:"))

if A>B and A>C:
    print(A, "A is greater")
elif A==B or B==C or C==A:
    print("Any Numbers are Same")
elif B>C and B>A:
    print(B, "B is greater")
else:
    print(C, "C is greater")


