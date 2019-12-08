# Assignment 2  -- Problem 1
# Using recursive function to add input string of numbers
# Sum of an array Given an array of numbers return it’s sum (all the numbers added together)
# how it works:
#  select individual (one) array elements using recurisve call
#  sum up the numbers and return the value once all the array elements are added-up
def SumInteger(arr): 
     if len(arr)== 1: 
        return arr[0] 
     else: 
        return arr[0]+SumInteger(arr[1:]) 
# Input and function output values
Input = [1,5]
print("---------------------------------------------------------------------")
print("Assignment 2 - Problem 1 - Sum of an array of integers")
print("   Input Integer Array :" +  str(Input))
print("   Output value from the function :" + str(SumInteger(Input)) )


# Assignment 2  -- Problem 2
# Using recursive function to multiply input string of numbers
# Product of an array Given an array of numbers return it’s product (all the numbers multiplied together)
# how it works:
#  select individual (one) array elements using recurisve call
#  Multiply the numbers and return the value once all the array elements are multiplied
def MultiplyInteger(arr): 
     if len(arr)== 1: 
        return arr[0] 
     else: 
        return arr[0]*MultiplyInteger(arr[1:]) 

# input output values
Input = [5,5,2]
print("---------------------------------------------------------------------")
print("Assignment 2 - Problem 2 - multiply input string of numbers")
print("   Input Integer Array :" +  str(Input))
print("   Output value from the function :" + str(MultiplyInteger(Input)) )



# Assignment 2  -- Problem 3
# Remove all even numbers Given an array of numbers return an array with all the even numbers removed.
# how it works:
#  select individual (one) array elements using recurisve call
#  check if the number is odd
#  construct a odd elements array and return it at the end of the final recursive call
def OddOnly(numbers):
  if not numbers:
    return []
  if numbers[0] % 2 == 1:
    return [numbers[0]] + OddOnly(numbers[1:])
  return OddOnly(numbers[1:])

# Input and function output values
Input = [5,5,2]
print("---------------------------------------------------------------------")
print("Assignment 2 - Problem 3 - Remove even numbers")
print("   Input Integer Array :" +  str(Input))
print("   Output value from the function :" + str(OddOnly(Input)) )

# Assignment 2  -- Problem 4
# Remove all odd numbers 
# how it works:
#  select individual (one) array elements using recurisve call
#  check if the number is even
#  construct a even elements array and return it at the end of the final recursive call
def EvenOnly(numbers):
  if not numbers:
    return []
  if numbers[0] % 2 == 0:
    return [numbers[0]] + EvenOnly(numbers[1:])
  return EvenOnly(numbers[1:])

# Input and function output values
Input = [5,5,2,4]
print("---------------------------------------------------------------------")
print("Assignment 2 - Problem 4 - Remove odd numbers")
print("   Input Integer Array :" +  str(Input))
print("   Output value from the function :" + str(EvenOnly(Input)) )

# Assignment 2  -- Problem 5
#  Replace a given character with ’*’ Given a string, and a character to replace, return a string where each occurance of the character is replaced with ’*’.
# how it works:
#  select individual (one)  elements of a string using recurisve call
#  check if the individual string element matches with the input search string; replace the element with "*"
#  recursively loop until all the elements are checked in the input string
def Rstring(str, cha):
  if not str:
    return []
  if str[0] == cha:
    str[0]="*"
  return [str[0]] + Rstring(str[1:], cha)

# Input and function output values
print("---------------------------------------------------------------------")
Input1 = "cbbcaac"
Input2 = 'c'
print("Assignment 2 - Problem 5 - Replace a given character with * in a string")
print("   Input string value :" +  str(Input1))
print("   Input replace string value :" +  str(Input2))
print("   Function output :" + "".join(Rstring(list(Input1),Input2)) )

# Assignment 2  -- Problem 6
# Given an array, and an element to search for return the index of the element in the array or -1 if the element is not present in the array.
# how it works:
#  select individual (one)  elements of a string using recurisve call
#  define 2 global variables - counter for the number of recusive calls and length of the array
#  check 
#     if the search string matches with the array element recursively. 
#     if matches, send the global variable counter position which represents the array element position
#     if no match found , then return -1 
def iarray(arr, cha):
  global counter , inputlen
  counter= counter + 1
  if not arr:
    return -1
  if arr[0] == cha:
    arr.index(cha)
    return(counter-1)
  elif inputlen == counter-1:
    return -1
  return iarray(arr[1:], cha)

counter = 0
inputlen = 0
inputlen = len(Input1)
# input values to list 
print("---------------------------------------------------------------------")
Input1 = ['jo','anu','ajay']
Input2 = 'ajay'
print("Assignment 2 - Problem 6 - Replace the value in a given string")
print("   Input string value :" +  str(Input1))
print("   Input search string value :" +  str(Input2))
print("   Index of the Search string in a given String :" + str(iarray(Input1, Input2)))

# Assignment 2  -- Problem 7
# Sum of Digits Given a whole, number such as 23, return the sum of the digits in the number i.e. 2 + 3 = 5.
# For this would be useful to convert the number to a string then break it apart into digits.
# how it works:
#  convert the input integer as a list
#  select individual (one) list elements using recurisve call
#  Add the numbers and return the value once all the array elements are added
def Rsum(number):
     if len(number)== 1: 
        return int(number[0])
     else: 
        return int(number[0])+int(Rsum(number[1:]))

print("---------------------------------------------------------------------")
Input = 5555
print("Assignment 2 - Problem 7 - Return the sum of the digits in the number")
print("   Input Integer value :" +  str(Input))
print("   Output value from the function :" +  str(Rsum(list(str(Input)))))

# Assignment 2  -- Problem 8
# print an array Given an array of integers prints all the elements one per line. 
# This is a little bit diﬀerent as there is no need for a ’return’ statement just to print and recurs
# how it works:
#  select individual (one) array elements using recurisve call
#  print the array numbers recursively one by one 
def Pinteger(arr): 
     if len(arr)== 1: 
        return print(arr[0])
     else: 
        print(arr[0])
        return Pinteger(arr[1:])

# Input and function output values
print("---------------------------------------------------------------------")
Input = [9,9,0,0,1]
print("Assignment 2 - Problem 8 - Print the intergers one per line")
print("   Input Integer Array :" +  str(Input))
print("   Output value from the function :"  )
Pinteger(Input)

# Assignment 2  -- Problem 9
# Find the minimum element in an array of integers. You can carry some extra information through method arguments such as minimum value.
# how it works:
#  select individual (one) array elements using recurisve call
#  check the 2 elements in the array for a minimum value until all elements are exhausted recursively
def Minteger(arr): 

    if len(arr) == 1: 
      return (arr)
    elif len(arr) == 2:
      if arr[0]<arr[1]:
        return arr[0] 
      else:
        return arr[1]
    elif arr[0] < Minteger(arr[1:]):
        return arr[0]
    else:
        return Minteger(arr[1:])
  
# Input and function output values
Input = [9,9,0,0,1]
print("---------------------------------------------------------------------")
print("Assignment 2 - Problem 9 - Find minimum Value in an array of integers")
print("   Input Integer Array :" +  str(Input))
print("   Output value from the function :" + str(Minteger(Input)) )

# Assignment 2  -- Problem 10
# Nesting of paraenthesis or zeros ..0000 or "(())" or "((()))"
def Nesting(str):

  # Define 3 global variable to hold the zeros or opening or closing parenthesis
  global strv,opara,cpara
 
  # if there are more than 3 consecutive zeros return ture; otherwise don't return anything
  # if there are more than 2 consecutive matching parenthesis return true; otherwise don't return anything
  if len(strv) > 2:
    return True
  elif (len(opara) > 1) & (len(cpara) >1):
    return True

  # if the input is not string return empty
  # store the global variables if there are consecutive zeros or parenthesis otherwise clear the variable
  # call the function recursively
  if not str:
    return []
  if str[0] == "0":
    strv = strv + "0"
  elif str[0] == "(":
    opara = opara + "("
  elif str[0] == ")":
    cpara = cpara + ")"
  else:
    strv,opara,cpara='',"",""
  return Nesting(str[1:])

strv,opara,cpara='',"",""
Input = '099999000((8888(()))))'
check = Nesting(Input)
print("---------------------------------------------------------------------")
print("Assignment 2 - Problem 10 - Nesting of paraenthesis or zeros ..000 or '(())' or '((()))'")
print("   Input string :" +  Input)
print("   Output value from the function :" + str(check))
print("---------------------------------------------------------------------")