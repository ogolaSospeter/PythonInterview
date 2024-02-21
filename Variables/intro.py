# Python Comments
##

#Printing to a new line in python
print("This is the beginning of python deep dive.")

#Passing variables to print
name  =  'Developer'
age = 54

print("Good afternoon, " + name + str(age))

#Comparing variables
x = 56
y = 454

if x > y:
    print(x, " is greater than ", y)

print(y, " is greater than ", x)

fruits = ['lemon', 'apple','orange', 'avocado']

#Handling python loops.
[print(fruit) for fruit in fruits]

#printing in a single line
[print(fruit,end=" ") for fruit in fruits]


# *************************  LISTS   *************************

"""
Lists are ordered collections of data elements of different data types.
Lists are mutable meaning a list can be modified anytime.
Elements can be accessed using indices.
They are defined using square bracket '[]'.

"""
#Handling lists
fruits = ['lemon', 'apple','orange', 'avocado', 'melon']

#printing the list
print("\nFruits list \n" ,fruits, end=" ")

#adding an element to the list
fruit = "guava"
fruits.append(fruit)
print("\nFruits list with added fruit \n", fruits, end = " ")

#deleting an element from the list

fruits.__delitem__(0)

print("\nFruits list with a deleted fruit\n", fruits, end=" ")

#popping the last item in the list
fruits.pop()
print("\nFruits list with a popped fruit\n", fruits, end=" ")



# ******************** TUPLES  ************************
"""
Tuples are also ordered collections of data elements of different data types, similar to Lists.
Elements can be accessed using indices.
Tuples are immutable meaning Tuples can't be modified once created.
They are defined using open bracket '()'.
"""

numbers = (1,2,3,4,5,6,7,8,9)

print("\nThe tuple: \n", numbers)

#The total items in thee tuple

print(numbers.__sizeof__)

