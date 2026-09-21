# Logical operators- a symbol or word used in programming and 
# logic to combine or modify conditional statements and return a Boolean value
# or - at least one condition must be true
# and - both conditions must be true
# not - inverts the condition (not False, not True)

# NOT operator
# age =20
# looks_young=True
# if age < 18 or age > 70 or looks_young:
#     print("You are not allowed to enter")
# else:
#     # print("Welcome and have fun!!!")

# AND & NOT operator
height = 2
looks_short= False
if height < 5 and looks_short:
    print("You are too short to enter")
elif height >= 10 and looks_short:
    print("You are just the perfect height")
elif height <= 3 and not looks_short:
        print("You are a child")
else:
    print("Just the right height")
