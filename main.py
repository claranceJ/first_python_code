#Variables

#character_name = "John"
#character_age = "56"  

#print("my name is " + character_name + ",")
#print("I am " + character_age + " years old")
#print("I hate the name " + character_name + ",")

#character_name = "Jack"
#print("But I love playing with " + character_name + ",")
#print("my friend " + character_name + " is also 56")

#string

# print("the world\nbeyond")

# phrase = "December"
# print(phrase + " is realy cold")

phrase = "December"
# print(phrase.upper().isupper())  /for caps
# print(len(phrase))   /for checking length of string
# print(phrase[0])       /grabbing a specific character
# print(phrase.index("em"))  /grabbing character and giving the number
#print(phrase.replace("December", "November"))  #/replacing string

#Practise before next lesson
#character_age = "30"
#character_name = "Jill"

#print("My name is " + character_name + ",")
#print("I am a " + character_age + " year old")

#phrase = "Today"
#print(len(phrase))
#print(phrase.upper())
#print(phrase.index("a"))
#print(phrase.replace("Today" , "Kesho"))

#Numbers
#print(10 % 3) #the modulo operator,ten mode 3, gives out the remainder of the calculation

# my_num = 5
#print(my_num)
#print(str(my_num)) #printing a number as a string
# print(str(my_num) + " is my favorite number")

# funtions in Number

# my_num = -8
# print(abs(my_num))
# print(pow(my_num, 2))  this translates to -8^2

# print(max(4, 9)) prints out the largest of the numbers
# print(min(4, 9))  prints out the smallest of the numbers
# print(round(4, 9))

# from math import * #used to import external code into our file

# print(floor(2.8))  #removes the decimal point and 8 to give you only 2
# print(ceil(2.8))  #rounds up the number
#print(sqrt(36))

# how to get Input from a user
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "!" " you are " + age )

# How to build a basic Calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = int(num1) + int(num2)  #int funtion is used to make the number a whole number, but gives an error when calculating decimals
# result = float(num1) + float(num2)  #float function allows us to calculate using decimal numbers without errors
# print(result)

# Mad Libs Game, my own practice exercise
# car=input("Enter favorite car: ")
# celeb=input("Enter favorite celebrity: ")
# movie=input("Enter favorite movie: ")

# print("my dream car is " + car)
# print("I have a Secret crash for " + celeb)
# print("my favorite movie is " + movie)  very proud of my self btw

# Lists in python
# friends = ["Run", "Clone", "Order"]  #square bracket is used to store a bunch of values inside a list
# friends = ["Run", "Clone", "Order"]  #you can store strings, numbers and booleans inside the list
# print(friends)
friends = ["Run", "Clone", "Order", "Never"]
# print(friends[0]) #used to access a specific value on the list
# print(friends[1:]) #used to access the elements from value 1 going forward
# print(friends[1:3]) #used to access the value 1 and the elements btwn 1 and 3, note:it doesn't capture the value 3.
# friends[1] = "Walk" #used to change a specific value
# print(friends[1])

#list fUnctions
pass_code = [7, 9, 12, 18, 22, 46, 96, 24]
cars = ["lexus", "Mazda", "Sienta", "Urus", "Lambo", "Lambo", "Ferrari"]
# cars.extend(pass_code) #the extend function is used append one list to the other
# cars.append("Range")  #the append function used to append a new value to the list
# cars.insert(1, "Ractis") #the insert function is used to add values in the list
# cars.remove("Mazda") #the remove function is used to remove values in the list
# cars.clear()      #the clear function is used to clear evrything 
# cars.pop()       #the pop function pops a value off the list
# cars.sort()  #the sort function is used to arrange the values in ascending order
# cars.reverse() #the reverse function is used to reverse the values
# cars2 = cars.copy() #the copy function is used to copy a new list
# print(cars2)
# print(cars.index("Lambo")) # index function identifies the position of the value
# print(cars.count("Lambo")) # count function used to count the number of time the value appears

# Tuples-a type of data stracture, a container we can store different values, Tuples are Immutable(they can't be changed)

# coordinates = (2, 9)
# print(coordinates[0])
# coordinates = [(4, 9), (7, 4), (9, 8)] #a list of tuples
# print(coordinates[0])

# FUNCTIONS
# def is a keyword used to declare a function
# def say_hi():
#   print("Jack is the guy")
# say_hi()  #this is used to call the function

# A paramiter is a piece of information that we give to the function
# def say_hi(name):
#   print( name + " is the guy")
# say_hi("Jack")

# def say_hi(name, age):
#   print( name + " is the guy who is " + age + " years old")
# say_hi("Jack", "29")
# say_hi("Mike", "89")
#my personal example
# def say_person(name, age):
#   print("hello " + name + " I'm " + age + " years old")
# say_person("Jack", "45")
# say_person("Will", "65")

# RETURN STATEMENTS
# def cube(num):
#    return num*num*num

# print(cube(3)) this can also work
# result = cube(4)
# print(result)

#If Statement
# is_male = True
# if is_male:
#   print("You are male")

# is_male = False
# if is_male:
#   print("You are male")
# else:
#   print("You are male")

#The use of or
# is_male = True
# is_tall = True
# if is_male or is_tall:
#   print("You are male or tall or both")
# else:
#   print("You are neither male nor tall")
#   print("You are male")

#The use of and
# is_male = False
# is_tall = True
# if is_male and is_tall:
#   print("You are male and tall")
# else:
#   print("You are neither male nor tall")

# The use of elseif(elif)
# 
# my personal Example
# has_paid = True
# has_balance = False
# if has_paid and has_balance:
#    print("The student has paid but has balance")
# elif has_paid and not(has_balance):
#    print("The student has cleared fees")
# elif not(has_paid) and has_balance:
#    print("the student has not paid and has balance")

# Another personal Example
# has_password = False
# has_username = False
# if has_password and has_username:
#   print("has both cridentials")
# elif has_password and not(has_username):
#   print("has no username")
# elif not(has_password) and has_username:
#   print("has no password")
# else:
#   print("Neither has password nor username")

# If statements and Comparisons
# def max_num(num1, num2, num3):
#   if num1 >= num2 and num1 >= num3:
#     return num1
#   elif num2 >= num1 and num2 >= num3:
#     return num2
#   else:
#     return num3

# print(max_num(3, 4, 5))

# !=  not equal
# == equal

# my personal Example
# def max_num(num1, num2, num3):
#   if num1 >= num2 and num1 >= num3:
#     return num1
#   elif num2 >= num1 and num2 >= num3:
#     return num2
#   else:
#     return num3

# print(max_num(7, 3, 2))

# my other personal example
# def min_num(num1 , num2, num3):
#   if num1 < num2 and num1 < num3:
#     return num1
#   elif num2 < num1 and num2 < num3:
#     return num2
#   else:
#     return num3

# print(min_num(4, 2, 3))

# Buildig a better calculater
# num1 = float(input(" Enter first number: "))  #float converts the string into number
# op = input(" Enter operator: ")
# num2 = float(input(" Enter second number: "))

# if op == "+":
#   print(num1 + num2)
# elif op == "-":
#   print(num1 - num2)
# elif op == "/":
#   print(num1 / num2)
# elif op == "*":
#   print(num1*num2)
# else:
#   print("Invalid Operator")

# My personal example
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
# if op == "+":
#   print(num1 + num2)
# elif op == "-":
#   print(num1 - num2)
# elif op == "*":
#   print(num1 * num2)
# elif op == "/":
#   print( num1 / num2)
# else:
#   print("invalid input")

# Dictionaries
# monthConversions = {
#   "Jan" : "January",
#   "Feb" : "February",
#   "Mar" : "March",
#   "April" : "April",
#   "May" : "May",
#   "Jun" : "June",
#   "Jul" : "July",
#   "Aug" : "August",
#   "Sep" : "September",
#   "Oct" : "October",
#   "Nov" : "November",
#   "Dec" : "December",
# }
# # print(monthConversions["Nov"])   one way of accessing November
# # print(monthConversions.get("Nov")) # another way is to usethe.get
# print(monthConversions.get("luv", "Not a valid key"))

#While Loop
# i = 1
# while i <= 10:
#   print(i)
#   i = i + 1
#   # i += 1    #short hand formular for i = i + 1
# print("Done with the loop")

#my persona example
# i = 20
# while i >= 20:
#   print(i)
#   i += 1
# print("done with loop")

# Building a basic guessing game
# secret_word = "Natalia"
# guess = ""

# while guess != secret_word:
#   guess = input("Enter first love: ")

# print("You win!")

# my personal example
# dreamcar_model = "Lexus"
# guess_dreamcar = ""

# while guess_dreamcar != dreamcar_model:
#   guess_dreamcar = input("Enter dreamcar: ")

# print("You win!")

# An advanced guessing game
# secret_word = "Natalia"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses) :
#   if guess_count < guess_limit:
#     guess = input("Enter first love: ")
#     guess_count += 1
#   else:
#     out_of_guesses = True 
    
  
# if out_of_guesses:
#   print("out of guesses! You lost!")
# else:
#   print("You win!")

# My personal Example
# Create a variable for the car to be guessed
# Create a variable that stores the user guesses
# Create a variable for the maximum number of guesses
# Create a variable for the zero guess
# create a while loop for the users guess
# create an input for the users guess
# Create a boolean for the maximum guess

# the_car = "Lexus"
# user_guess = ""
# maximum_guesses = 3
# guesses = 0
# out_of_guess = False

# while  user_guess != the_car and not(out_of_guess):
#    if guesses < maximum_guesses:
#      user_guess = input("Guess my favorite car: ")
#      guesses += 1 
#    else:
#      out_of_guess = True
   
   
# if out_of_guess:
#   print("Out of guess, lost!")
# else:
#   print("Correct guess!")


# Another personal project


# password = "Hello"
# user_input = ""
# user_trial = 3
# user_acces = 0
# user_limit_reached = False



# while user_input != password and not(user_limit_reached):
#   if user_acces < user_trial:
#     user_input = input("Enter password: ")
#     user_acces += 1
#   else:
#     user_limit_reached = True
    
  
# if user_limit_reached:
#   print("Sorry, Account locked! ")
              
  
# else:
#   print("Welcome!")

# Another personal project

# passcode = "12345"
# user_key_in = ""
# key_in_limit = 3
# key_in_default = 0
# key_in_exceeded = False

# while user_key_in != passcode and not(key_in_exceeded):
#   if key_in_default < key_in_limit:
#     user_key_in = input("Enter passcode: ")
#     key_in_default += 1

#   else:
#     key_in_exceeded = True
    
     
# if key_in_exceeded:
#    print("Sorry! Account locked")


# else:
#     print("Welcome!")


#For Loop--
# for friend in friends:
#    print(friend)


# friends = ["Jim", "Karen", "Kevin"]
# for names in friends:
#    print(names)


# for index in range(10):   prints out the range btwn 0-10
#    print(index)


# for index in range(3, 10):  #prints out the numbers btwn 3-10
#    print(index)


# friends = ["Jim", "Karen", "Kevin"]
# for index in range(len(friends)):
#   print(friends[index])


# friends = ["Jim", "Karen", "Kevin"]
# for index in range(7):
#   if index == 0:
#     print("First iteration")
#   else:
#     print("Not first")


# Exponent Function
# print(2**3)

# exponent with for loop// make sure to repeat this and fully understand
# def raise_to_power(base_num, pow_num):
#   result = 1
#   for index in range(pow_num):
#     result = result * base_num
#   return result

# print(raise_to_power(3, 2))


# 2D Lists And Nested Loops

# number_grid = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# print(number_grid[0][2])  /accessing elements inside a 2D list

# Nested for loop
number_grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
# for row in number_grid:   used in printing elements in a raw
#   print(row)

# for row in number_grid:  used in printing elements in a column
#   for col in row:
#     print(col)


# Building a translator--- To come back to this and practice

# def translate(phrase):
#   translation = ""
#   for letter in phrase:
#     if letter in "AEIOUaeiou":
#       translation = translation + "g"
#     else:
#       translation = translation + letter
#   return translation


# print(translate(input("Enter a phrase: ")))



# Comments in python
# to write notes, to comment a line of code


# Try Except

# try:
#   number = int(input("Enter a number: "))
#   print(number)
# except :                    #used to handle an error
#   print("Invalid Input")


# below example shows use of try/except used to catch specific errors
# try:
#   value = 10/0
#   number = int(input("Enter a number: "))
#   print(number)
# except ZeroDivisionError:
#   print("Divided by zero")
# except ValueError :                    
#   print("Invalid Input")



# Reading Files in python
# python read command

# open("employees.txt", "r")  #r mode means you only want to read information
# open("employees.txt", "w")  #w mode for writing
# open("employees.txt", "a")  #a mode for appending info at the end of the file
# open("employees.txt", "r+") #r+ mode for reading and writing

# employee_file = open("employees.txt", "r")

# print(employee_file.readable()) #the .readable function is used to confirm if we can read the file

# employee_file.close()


# employee_file = open("employees.txt", "r")

# print(employee_file.read()) #the .read function spits out the information in the file

# employee_file.close()


# employee_file = open("employees.txt", "r")

# print(employee_file.readline()) #the .readline function is used to read the first line on the file

# employee_file.close()


# employee_file = open("employees.txt", "r")

# print(employee_file.readlines()) #the .readlines function is used to list all the info in the file, we can specify by adding an index (.readlines()[1])

# employee_file.close()



# employee_file = open("employees.txt", "r")

# for employee in employee_file.readlines(): #you can also use a for loop
#   print(employee)

# employee_file.close()



# Writing and appending to Files in python

# employee_file = open("employees.txt", "a")  #"a" for adding text at the end of file
# employee_file.write("Jack - IT admin")

# employee_file.close()



# employee_file = open("employees.txt", "a")

# employee_file.write("\nJack - IT admin")  #appends new text in a new line

# employee_file.close()




# employee_file = open("employees.txt", "w")  #"w" ovewrites every text and writes adds new tex
# employee_file.write("\nJack - IT admin")

# employee_file.close()


# employee_file = open("employees1.txt", "w")  #adds new file and a new text in it, you can use different file extensions too "index.html"

# employee_file.write("\nJack - IT admin")

# employee_file.close()



# modules and pip

# we are going to assume we have an extrnal file called  "usefool_tools" and a tool inside it called "roll_dice"

# import "useful_tools" #used to import an external file and useful functions inside it
# print(usef_tools.roll_dice)

# to get more example of modules visit https://docs.python.org
# research about python docx
# read about pip     pip>>site-packages>>docx



# Classes and Objects in python

# we assume the below class is on a student.py file

# class student:
  
#      #the below function is called an initialised function
#   def __init__(self, name, major, gpa, is_on_probation):
#       self.name = name
#       self.major = major
#       self.gpa = gpa
#       self.is_on_probation = is_on_probation
  
  
  
# # the below info is on our current file "main.py"

# # from student import student---this will be used if the file was external
    
# student1 = student("Jim", "IT", 3.4, False)
# student2 = student("Jack", "Business", 3.8, True)

# print(student2.is_on_probation)
  


# Building a multiple Choice Quiz

# we assume the below information is on another file called"Question.py"
# class Question:
#   def __init__(self, prompt, answer):
#     self.prompt = prompt
#     self.answer = answer

# question_prompts = [
#   "What color are apples?\n(a) Red\n(b) Green\n(c) Purple\n\n",
#   "What color are banans?\n(a) Blue\n(b) Magenta\n(c) Yellow\n\n",
#   "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]

# questions = [
#    Question(question_prompts[0], "a"),
#    Question(question_prompts[1], "c"),
#    Question(question_prompts[2], "b"),

# ]

# def run_test(questions):
#   score = 0
#   for question in questions:
#     answer = input(question.prompt)
#     if answer == question.answer:
#       score +=1
#   print("You got " + str(score) + "/" + str(len(questions)) + "Correct")


    
# run_test(questions)

# Class Function--research and read about this

# Object Function--research and read about this

# Inheritance in python---read about this



# Python Interpreter--environment used to execute python commands(cmd/terminal)


