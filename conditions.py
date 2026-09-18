# login_attempts =4
# max_attempts= 6
# is_locked= False

# if is_locked:
#     print("Your account is locked, Kindly contact the support")
# elif login_attempts >=max_attempts:
#     print("You have reached the maximum number of attempts. Your account is locked")
# elif login_attempts>0:
#     rem_attempts= max_attempts-login_attempts
#     print(f"You have {rem_attempts} remaining attempts")
# else:
#     print("Welcome")


# role=input("What is your role?(Editor/admin): ") .strip() .lower()
# is_logged=True

# if not is_logged:
#         print(f"Hello {role}. Access denied")
# elif role== "editor":
#         print("Can edit content")
# elif role =="admin":
#         print("Full access granted")
# else:
#         print("Read-only access")


number = int (input("Input your number: "))

if number %3 ==0 and number %5 ==0 :
    print("FizzBuzz")
elif number %3 ==0:
    print("It is divisible by 3. It is not divisible by 5")
elif number %5== 0:
    print("It is divisible by 5. It is not divisible by 3")
else:
    print("It is not divisible any of the numbers")





# response= input("Are you tired (Y/N): ")

# if response == "Y":
#     print("Have a seat")
# else:
#     print("Keep on soldier")


# name = input("What is your name: ")

# if name == "":
#     print("Kindly input your name")
# else:
#     print(f"Hello {name} how are you")


#     is_tired= True

#     if is_tired:
#         print("You may have a massage")
#     else:
#         ("End of the line please")
