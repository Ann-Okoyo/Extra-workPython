import apt


def my_func():
    print("Hello I am a software developer")

my_func()

def resident(name,area):
    print(f"Hello {name}, are you from  {area} ?")

resident("Ann",'Kakamega')

def volume_of_cuboid(length,width,height):

    return(length*width*height)

volume=volume_of_cuboid(30,50,60)
print(f"Volume of the cuboid=",volume)

# Write a Python function to calculate the area 
# of a rectangle given its length and width.
def area(length,width):
    return(length*width) 

zone=area(70,50)
print(f"The area of the rectangle is",zone)


# Write a Python function to check if 
# apt given number is even or odd.
# def check(number):
#     for num in number:
#         if num%2==0:
#             print("Its an even")
#         else:
#             print("Its an odd")

        

# check(6)
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
 
num=10
if is_even(num):
    print(num ,"is even")
else:
    print(num,"is odd")


# Write a Python function to find the 
# maximum of three given numbers.
# 
def max_of_three(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
    
num1=80
num2=70
num3=27

max_num=max_of_three(num1,num2,num3)
print("The maximum of",num1,num2 ,"and", num3 ,"is:",max_num )

# def rating_value(rating=5.5):
#     if  rating<5.5:
#         return f"Should not watch movie with rating "


# Write a function named smallest that accepts a 
# list of unsorted integers and returns the smallest 
# number in the list.
# def smallest(content):

#     return content.min()
#     # content =[40,60,80,90]
#     # content.min()

# figures=smallest[40,60,80,90]
# print("The minimum number", figures)

# Write a function that takes two numbers
# as input and returns their sum.
def work_out(num1,num2):

    return num1+num2

num1=7
num2=9
add_numbers=work_out(num1,num2)
print(f"The sum of",num1 ,"and" ,num2,"is",add_numbers,".")


# multiplication 
def multiply(num3,num4):
     
     return num3*num4
num3=70
num4=80
product=multiply(num3,num4)
print(f"The product of",num3, "and",num4, "is",product,".")
