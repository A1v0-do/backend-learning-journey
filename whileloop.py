# While loop -a programming control structure that
#  repeats a block of code as long as a specific condition remains true
# name = input ("WHat is your name: ")
# height = int(input("WHat is your height: "))

# while name =="":
#  name = input("What is your name: ")

# while height <0:
#  print("Height must be valid")
#  height= int(input("What is your height: "))
 

# print (f"My name is {name}")
# print(f"You are {height} meters tall")

# max_attempts=3
# attempts =0
# correct_password ="Ali234"

# while attempts < max_attempts:
#     entered=input("Enter your pasword: ")
#     if entered == correct_password:
#         print("Successful Login, Welcome")
#         break
#     else:
#         attempts +=1
#         print(f"Wrong password. {max_attempts-attempts} attempts remaining.")
# else:
#     print("Account Locked. Contact support")


for number in range(1,21):
    if number % 3 ==0 and number %5 ==0:
        print("FizzBuzz")
    elif number %3 ==0:
        print("Fizz")
    elif number %5 ==0:
        print("Buzz")
    else:
        print(number)



