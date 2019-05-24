# a = "Arslan Arshad"

# String Functions

# a.capitalize()  # capitalize the string
# a.upper()   # upper case the string
# a.title()     # Upper case the First letter of each word
# a.lower()       #lower case the string

# Multi-Line Variable (It can store multi line strings value in a single Variable)
# Hard coded (Means the string will be printed as it is written like the <pre> in html)

# info = """Arslan Arshad
# 21
# Karachi"""
# print(info)

# Taking Input

# Name = input("Enter Your Name : ")
# Age = input("Enter Your Age : ")
# Profession = input("Enter Profession : ")

# information = """
# *************************
#    Student Information
# *************************
# Name : {}
# Age : {}
# Profession : {}
# *************************"""

#By this you can print the input values where you want to print

# print(temp.format(Name,Age,Profession))

# Operator
# Solve via PEMDAS
#PEMDAS (Paranthesis Exponent Multiplication Division Addition Substraction)


#   Normal Operators
#   + , - , * , / , % , // , **

# a = 10 / 2      # Normal division   Ans will be 5.0
# b = 10 // 2     # FLoat Division (Remove Float answer) Ans will be 5
# c = 2 ** 3      # Power Funtions Ans will be 8

#   Assignment Operator
#   =, += , -= , *=, %= ,/=

# a = "Hello"
# a += " Arslan"

#Result will be "Hello Arslan"

# a = 10
# a %= 3 
# print(a)
#Answer will be 1

#   If, else, elif

a = 4
b = 4
if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("both are equal")
#The result will be both are equal