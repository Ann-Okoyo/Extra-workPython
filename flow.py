language = input("Please enter your favorite language:")
if language == "Python":
    print("Yes ofcourse its Python")
else:
    print("Hmmm! are you sure its not Python")

age =int(input("Enter your age:"))
if age < 18:
    print("You need to be over 18 years old to continue.")
elif age <21:
    print("You need to be over 21 years to continue.")
else:
    print("You are over 18 and 21 years so you can continue.")

for i in range(11):
    if i%2==0:
        print(i)

# Write a Python program to find the sum of all 
# even numbers from 1 to 50 using a for loop.
for i in range(1,50):
    sum=0
    if i%2==0:
        print(i)
        sum+=i
    print(sum)


# Write a Python program to find the largest 
# element in a given list of numbers using a for loop.
list =[89,57,89,47,80,30]
largest=list[0]
for i in list :
    if i >largest:
        largest = i

print("The largest number is:",largest)

# Write a Python program to check if a given number
# is prime or not using a for loop.
numeral =int(input("Enter a number:"))
is_prime=True
for i in range(2,numeral):
    if numeral%i ==0:
        is_prime=False
        break 
    if is_prime:
        print(numeral,"is a prime number")
    else:
        print(numeral,"is not a prime number")

enter =int(input("Enter a number:"))
is_prime=True
for i in range(2,enter):
    if numeral%i ==0:
        is_prime=False
        break
    if is_prime:
        print(enter,"is a prime number")
    else:
        print(enter,"is not a prime number")

# Write a Python program to find the sum of all 
# odd numbers from 1 to 100 using a for loop.
# python
numbers= range(1,100)
sum=0
for i in numbers:
    if i%2!=0:
        # print(i)
        sum+=i
    print(sum)


addition =0
for i in range(1.101,2):
    addition+=i
    print(addition)

secret_keyword="Python"
tackle=input("Enter the key_code:").capitalize()
while tackle!=secret_keyword:
    tackle=input("Enter the key_code:").capitalize()
      