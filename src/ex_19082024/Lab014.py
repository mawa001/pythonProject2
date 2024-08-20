#Task- 3
# - Explain the difference between the = operator and the == operator in Python.
#
# - What does the ** operator do in Python, and how is it used?
#
# - What does the ^ operator do in Python, and in what context is it commonly used?


"""
Question-Explain the difference between the = operator and the == operator in Python.
Answer- '=' is an assignment operator, which is used to assign a value to a variable.
# ex
"""
x = 10 #this assigns value 5 to variable x
print(x)
# """
   # '==' is an equality operator, which is used to compare two values. If values are equal then result is 'True', 
   # if values are not equal then result is 'False'.
# For e.g.
# """
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
print(num1==num2)  #True

num3 = int(input("Enter num3 : "))
num4 = int(input("Enter num4 : "))

print(num3==num4)  #False

"""
Q- What does the ** operator do in Python, and how is it used?
A- '**' indicates to the Power, the left side operand is the base and right side is the exponential power to which the 
base is raised.
For e.g.
"""
num5 = int(input("Enter num5 : "))
num6 = int(input("Enter num6 : "))
# num5 = 10 ** 2 # 10 is base and 2 is exponential power and ** indicates to the power
print(num5**num6)

"""
Q- What does the ^ operator do in Python, and in what context is it commonly used?
A- In python '^' operator operates on the binary representation, and perform XOR operation
For e.g.
"""
a = 2
b = 3
c = 2 ^ 3
print(c)