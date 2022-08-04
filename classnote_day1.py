# <-- commenting (python ignores it, only for notes)

## Python 4 primitive data types 

# integer			 # -87, 0, 31, 17  
# float 			 # 0.3, 3.0, -9.983818483
# string 			 # "apple", "orange", "31", "Happy"
# boolean			 # True, False 

## Operators 

# x = 7 
# y = 2 

# print(x, y)
# print(x + y)			# 9 
# print(x - y)			# 5 
# print(x * y)			# 14
# print(x ** y)			# 49 exponent
# print(x / y)			# 3.5 division (exact value)
# print(x // y)			# 3 quotient (whole number)
# print(x % y)			# 1 remainder 
# print(x > y)			# True 
# print(x < y)			# False 
# print(x == y)			# equal? 


# # Exercise 
# number = 56 
# firstDigit = number // 10 
# secondDigit = number % 10 
# print(firstDigit + secondDigit)


# Conditionals 
# x = 10 
# if x <  5:
# 	print("A")
# 	print("B")

# print("C")

# Only C will get printed, because A and B are applied to the if statement
# C is not 


# Exercise 2 
# Given a number, print "Odd" if number is odd. "Even" otherwise.

# number = 13 
# if number % 2 == 1:
# 	print("Odd")
# if number % 2 == 0: 
# 	print("Even")


# Exercise 3 
# A full carton contains 12 eggs. Given a random number of eggs 
# print the number of eggs needed to make it a full carton 

eggs = 40
extraEggs = eggs % 12 
eggsNeeded = 12 - extraEggs
print(eggsNeeded)


## Typecasting ## 
# changing data type. NOT possible for all cases 

x = 3 
y = "3" 
z = True 
zz = 3.3
# print(x + y)			# type error. cannot add string to int 
print(x * y)			# 333 
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(zz, type(zz))

x = str(x)				# converted int 3 to string 
print(x, type(x))
z = x + y 
print(z)
zz = 33 

print(z == zz)
print(z != zz )			# ! represents not 



# Exercise 
# given a number, print the absolute value of the number 

number = -81 

