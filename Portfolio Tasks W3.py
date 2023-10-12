# Task 1
Name = input("Please enter your name: ")
if len(Name) > 1:
    print("hello", Name)
else:
    print("Hello stranger ")

# Task 2, 3 ,4, 5
i = 1
while i == 1:
    BadPasswords = ["Password", "password"]
    NewPassword = input("Please enter your new password")
    if NewPassword not in BadPasswords:
        if 13 > len(NewPassword) > 7:
            PasswordCheck = input("Please re enter your password ")
            if NewPassword == PasswordCheck:
                i = i + 1
print("Your new password is set! ")

# Task 6, 7, 8
temp = 14
Multiplication = int(input("Please enter the times table you would like to see: "))
if Multiplication < 0:
    a = 12
    while a >= 1:
        print(Multiplication, "X", a, "=", Multiplication * a)
        a = a - 1
else:
    for i in range(13):
        maths = i * Multiplication
        print(maths)



        maths = i * Multiplication
        print(i, " x ", Multiplication, " = ", maths)
