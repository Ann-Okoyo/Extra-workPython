def student_attributes(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}:{values}")


def total_fruits(**kwargs):
    print(kwargs, type(kwargs))


total_fruits(banana=5,mango=7,apple=8)

# 
def fruits(**fruits):
    total=0
    for amount in fruits.values():
        total+=amount
    return total


# Write a Python function that accepts any number
# of keyword arguments and returns their sum
def addition(**kwargs):
    sum=0
    for key,value in kwargs.items():
        sum+=value
    return sum

result=addition(a=81,b=64,c=71)
print(result)

# Write a Python function that accepts a mandatory 
# argument and any number of optional keyword arguments.
# The function should return a string that includes the 
# mandatory argument and the optional keyword arguments.


# Write a Python function that accepts a dictionary
# and unpacks its key-value pairs as keyword arguments
# to another function.


def names(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}={values}")


names(title ="Ann",age=20,school="AkiraChix")


# def print_args_kwargs(*args,**kwargs):
#     print("")

# Write a function called add_numbers that takes 
# two numbers as arguments and returns their sum.
def add_numbers(num1,num2):
      return num1+num2

add_numbers(6,8)


# Write a function called multiply_numbers that
# takes two numbers as arguments and returns their product.
def multiply_numbers(num3,num4):
    return num3*num4

multiply_numbers(9,9)

# Write a function called reverse_string that takes 
# a string as an argument and returns the string in 
# reverse order.
# def reverse_string(string1):
#     string1.reverse()

#     return string1


# reverse_string()

# def is_prime(n):
#     if n <2:
#         return False
#     if n%2==0 or n%3==0:
#         return False
    

# Write a function called count_vowels that takes
# a string as an argument and returns the number 
# of vowels in the string.
def count_vowels(string):
    vowels ="aeiouAEIOU"
    count=0
    for char in string:
        if char in vowels:
            count+=1
        return count

string=("Hello")   
answers=count_vowels("Hello")
print(answers)


# Write a function called find_max that takes a list of 
# numbers as an argument and returns the maximum number 
# in the list.
def find_max(list):
    largest=[]



#     emptyArray=[]
#     for i in string:
#         if i in vowels:
#             print(i)
#             emptyArray.append(i)
#         emptyArray.count()

#     return results

# string="Hello"
# results=count_vowels(string)
# print(results)
    
def find_largest(arr):
    largest=arr[0]
    for num in arr:
        if num>largest:
            largest=num

    return largest

arr=[1,7,45,89]
resutz=find_largest(arr)
print=resutz


# Write a function named smallest that accepts a list 
# of unsorted integers and returns the smallest number
# in the list.
def smallest_number(array):
    smallest=[0]
    for i in array:
        if i<smallest:
            smallest=i


            return smallest
        

def get_even_numbers(numbers):
    even_numbers=[]
    for number in numbers:
        if number%2==0:
            even_numbers.append(number)

            return even_numbers
        
numbers=[1,2,3,4,5,6,7,8,9,10] 
even_numbers=get_even_numbers(numbers)
print(even_numbers)      

# Write a program that takes two inputs(integers) from a 
# user and adds the 2 numbers , checks if the sum is greater
# than 10, less than 10 and equal to 10 and prints a statement
# after each check.
num1=int(input("Enter a number:"))
num2=int(input("Enter a number"))

sum=num1+num2

if sum>10:
    "The sum is greter than 10"

elif sum<10:
    "The sum is less than 10"

else:
    "The sum is equal to 10."


# Write a function that takes one argument which is a 
# list of integers and returns True if 4 is present and
# False if not.


