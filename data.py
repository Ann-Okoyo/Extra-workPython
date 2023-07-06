def get_even_numbers(numbers):
    even_numbers=[]
    for number in numbers:
        if number%2==0:
            even_numbers.append(number)
            return even_numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=get_even_numbers(numbers)
print(even_numbers)


# def get_vowels(array):
#     vowels="aeiouAEIOU"
#     newString=[]
#     newchar=''
#     for char in array:
#         if char not in vowels:
#             newchar+=char
#             newString.append(char)
# Write a function that uses the range function 
# and a for loop and returns a list containing all
# the numbers between 100 and 200 that are divisible by 7
def workit(numetics):
    for i in range(100,200):
        if i%7==0:
            return(i)

numetics=range(100,200)
working=workit(numetics)
print(working)


# nombers=int(input("Enter a number:"))
# for i in nomber:
#     if i%7==0:
#         print(i)


# Write a program that takes two inputs(integers) 
# from a user and adds the 2 numbers , checks if the 
# sum is greater than 10, less than 10 and equal to 10 
# and prints a statement after each check.
def enter_number(integers):
    sum=0
    for i in integers:
        sum+=i
        print(sum)
    if sum>=10:
        return sum
    elif sum<10:
        return 10
    else:
        print("equal to")
    
integers=[6,8]
answer=enter_number(integers)
print(answer)

# Write a function that uses while, if and continue
# statements to print all the even numbers between 0 and 50. 
# def evens(numbers):
#     num=0
#     while num<50:
#         print(num)
#         num+=1
#     if num%2==0:
#         print(num)
#            continue
     
# 
# Write a function that takes a list of integers 
# as input and prints the sum of all the even 
# numbers in the list.
def not_odd(digit):
    sum=0
    for i in digit:
        if i%2==0:
            print(i)
        sum+=i
        print(sum)

digit=[10,57,48,32,93,21]
numetical=not_odd(digit)
print(numetical)

# Write a function that takes any two integers as input
# , and prints the sum of all the numbers between the 
# two integers (inclusive) that are divisible by 3.
