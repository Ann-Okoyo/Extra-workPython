# multiplication 
def multiply(num3,num4):
     
     return num3*num4
num3=70
num4=80
product=multiply(num3,num4)
print(f"The product of",num3, "and",num4, "is",product,".")

# division
def division(num5,num6):
      
      return num5/num6
num5=90
num6=5
divide=division(num5,num6)
print(f"The division of",num5, "and",num6,"is",divide,)


# Write a function that takes an array of
# numbers as input and returns the largest
# number in the array.
def  digits(num1,num2,num3):
      
      if num1>=num2 and num1>=num3:
            return num1
      if num2>=num1 and num2>num3:
            return num2
      else:
            return num3
      
num1=90
num2=60
num3=71

largest=digits(90,60,71)
print(f"The largest number in the array is",largest,)
      

# Write a function named smallest that accepts a
# list of unsorted integers and returns the smallest
# number in the list.
def smallest(numbers):
      if len(numbers)==0:
            return None
      min_num=numbers[0]
      for num in numbers:
            
            if num<min_num:
                  min_num=num
                  return min_num

numbers=[71,32,62,12]  
min_num=smallest(numbers)  
print("The smallest number in the list is:",min_num,)         

# Write a function that takes a number as input
# and returns true if the number is even and
# false if the number is odd.
# def even_odd(digits):
#       for num in digits:
#             if num%2==0:
#                   print("true")
#             else:
#                   print("false")

#             return digits
# digits=[40,56,73,71,49]
# figures=even_odd(digits)
# print("The following is a seperate list of odd and even number",figures,)


# Write a function that takes an array of strings 
# as input and returns a new array that contains the
# same strings, but with all vowels removed from each string.
def string(words):
      vowels ="aeiouAEIOU"
      newStrings =[]
      for i in words:
         newString=""
      for char in i:
            if char not in vowels :
                  newString+=char
                  newStrings.append(newString)

      #             result.append(newString)

      return newStrings
input_arr=["hello","world","how","are","you"]
newStrings=string(input_arr)
print(newStrings)

# Write a function that takes an array of strings 
# as input and returns a new array that contains the
# same strings, but with all vowels removed from each string.

def remove_Vowels(array):
      vowels="aeiouAEIOU"
      emptyString=[]
      emptychar =""
      for char in array:
            if char not in vowels:
                  emptychar+=char
                  emptyString.append(emptychar)
                  return emptyString
            
array=["student","school"]
remove=remove_Vowels(array)
print(remove)

# Write a function that takes an array of numbers as
# input and returns a new array that contains only
# the even numbers from the input array.
def contain_numbers(numeras):
      for i in numeras:
            if i%2==0:
                  print(i)

            return numeras
      
numeras =range(1,100)
result=contain_numbers(numeras)
print(result)



      