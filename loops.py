days=0
week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
while days<7:
    days+=1
print(days)

# Write a Python program that uses a 
# for loop to iterate from 0 to 10, 
# and prints out each number in the
# sequence.
def numbers(numerals):
    for i in range(1,10):
        print(i)
    
numerals=range(1,10)
print(numbers(numerals))


# Write a Python program that uses a while loop 
# to print out the numbers from 1 to 10.
def digits(figures):
    figures=1
    while figures<10:
        print(figures)
        figures+=1
# figures=range(1,10)
# print(digits(figures))

# Write a Python program that uses a for loop to 
# iterate over a list of numbers and prints out 
# the sum of all the numbers in the list.
def work_it(several):
    sum=0
    for i in several:
        sum+=i
        print(sum)

several=[29,80,70,50,78]
print(work_it(several))

# Write a Python program that uses a while
# loop to find the first 5 multiples of 3.
# 
i =1
count=0
while count<5:
    if i%3==0:
        print(i)
        count+=1
    i+=1

# Write a Python program that uses a for loop to 
# iterate over a list of strings and prints out 
# each string in uppercase.
def words(strings):
    for i in strings:
        print(i.upper())

strings=["akirachix","ann","software developer"]
print(words(strings))


# Write a Python program that uses a for loop to
# iterate over a list of numbers and prints out
# only the even numbers in the list.
def lists(numbers):
    for i in numbers:
        if i%2==0:
            print(i)

numbers=[80,63,28,90,72]
print(lists(numbers))

# Write a Python program that uses a while loop 
# to find the sum of all the numbers from 1 to 100
# def addition(digits):
sum=0
digits=1
while digits<100:
        digits+=1
        # print(num)
        sum+=digits
        print(sum)

# digits=range(1,100)
# print(addition(digits))

# Write a Python program that uses a for loop to
# iterate over a list of strings and prints out 
# only the strings that start with the letter "a".



strings=["apple","student","aeroplane","cow"]
for i in strings:
        if strings[0]=='a':
            print(i)

# Write a Python program that uses a while loop to
#  print out the numbers from 10 to 1 in descending order.
# def descending_order(works):
num=10
while num>10:
        print(num)
        num-=1
        

# Write a Python program that uses a for loop to iterate over
# a list of numbers and prints out the largest number in the list.
numbers=[70,90,80,50,43]
largest=numbers[0]
for i in numbers:
     if i >largest:
          largest=i
          print(largest)


# Write a function that uses while, if and continue statements
#  to print all the even numbers between 0 and 50. 
num=0
while num<50:
     if num%2!=0:
          num+=1
          continue
     print(num)
     num+=2


# Write a function that takes a list of integers as
# input and prints the sum of all the even numbers 
# in the list.
def sum_of_numbers(digits):
     sum=0
     for i in digits:
        if i%2==0:
             sum+=i
        print(sum)
digits=[50,80,11,31,63,75]
print(sum_of_numbers(digits))              


# Write a function that takes any two integers as input,
# and prints the sum of all the numbers between the two 
# integers (inclusive) that are divisible by 3.


# Print numbers from 0 to 10 except 5:
def take_numbers():
     num=0
     while num<10:
          num+=1
          if num==5:
               continue
          print(num)
        
take_numbers() 

# Print numbers from 0 to 10 except 5 and 7:
def except_numbers():
     numeral=0
     while numeral<10:
          numeral+=1
          if numeral==5 or numeral==7:
               continue
          print(numeral)

except_numbers()


# Print numbers from 0 to 10 until 5:
def print_numbers():
     numerate=0
     while numerate<10:
          numerate+=1
          if numerate==6:
               break
          print(numerate)


print_numbers()
# Sum numbers from 0 to 10 except 5 and 7:
def addition_of_nos():
    figure=0
    sum=0
    while figure<10:
         figure+=1
         if figure==5 or figure==7:
              continue
         sum+=figure
         print(sum)


addition_of_nos()


# Sum numbers from 0 to 10 until reaching 5:
def sum_nos():
     sum=0
     for x in range(6):
        if x==5:
               break
        sum+=x
        print(sum)

sum_nos()

# Print numbers from 0 to 10 except
# when n is multiple of 3:
def multiple_of():
     for x in range(0,10):
          if x%3==0:
               continue
          print(x)

multiple_of()

# Sum numbers from 0 to 100 except multiples of 3 and 5:
# python
def sum_of_integers():
     num=0
     while num<100:
          num+=1
          if num%3==0 or num%5==0:
               continue
          print(num)

sum_of_integers()


# Write a function that takes any two integers as 
# input, and prints the sum of all the numbers between 
# the two integers (inclusive) that are divisible by 3.
def two_numbers():
     sum=0
     for num in range(0,20):
          if num%3==0:
               num+=1
               sum+=num
               print(sum)
          
two_numbers() 

def my_function(*kids):
     print("The youngest child is"+kids[2])

my_function("Emil","Tobias","Linus")


def name(title="Ann"):
     print("My name is " + title)

name()  
name("muyale") 
name("Okoyo") 
name("Karen")

def work(**kid):
     print("His last name is" + kid["lname"])


work(fname="Tobias",lname ="Charles")

 