
# Task 1
Name = input("Please enter your name: ")
if len(Name) > 1:
    print("hello", Name)
else:
    print("Hello stranger ")

# Task 2, 3 ,4
i = 1
while i == 1:
    BadPasswords = ["Password", "password"]
    NewPassword = input("Please enter your new password")
    if NewPassword not in BadPasswords:
        if 13 > len(NewPassword) > 7:
            PasswordCheck = input("Please re enter your password ")
            if NewPassword == PasswordCheck:
                print("Your new password is set! ")
                i = i + 1

# Task 5
