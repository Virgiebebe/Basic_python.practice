# Declare three variables and assign values to each
# num1 (an integer) num2 (a float) num3 (a string)

num1 = 7
num2 = 10.1
name = "Virginia"

# print values and data types of variables
print(num1)       
print(num2)
print (name)
print(type(num1))
print(type(name))
print(type(num2))

# User input
# prompt the user to enter their age

age = int(input("Enter your age: "))
# print a message based on the age

if age < 18:
     print("You are a minor.")
elif age >= 18 and age < 65:
     print("You are an adult.")     
else: 
    print("You are a senior citizen")
          
# Conditional Statements:

def check_number(num): 
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

check_number(30)
check_number(-3)
check_number(0)

#Loops:
#Loop that prints all even numbers from 0 to 20 (inclusive)
for i in range(0, 21, 2):
    print(i)

# Functions:
# write a function named calculate_circle_area that takes a single parameter radius that takes a single parameter radius 

def calculate_circle_area(radius):
    pi = 3.14
    area = pi * radius**2
    return area

# Call the function with a radius of 5.5 and print results
radius = 5.5
area = calculate_circle_area(radius)
print("The area of the circle with radius", radius, "is:", area)
