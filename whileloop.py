# While loop -a programming control structure that
#  repeats a block of code as long as a specific condition remains true
name = input ("WHat is your name: ")
height = int(input("WHat is your height: "))

while name =="":
 name = input("What is your name: ")

while height <0:
 print("Height must be valid")
 height= int(input("What is your height: "))
 

print (f"My name is {name}")
print(f"You are {height} meters tall")