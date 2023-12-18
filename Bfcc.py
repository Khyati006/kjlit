# This code is for beginners who are learning Python.
character_name="Mrunmai"
character_age="18"
print("My roommate name is " + character_name)
print("Her age is"+character_age)
print("Indian institute\n of \n\"Information Technology\"")#\n is like enter
phrase= "DOTS"
print(phrase + " is my favourite k-drama")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.lower().isupper())#lower is for lower case and is upper is to check true or false
print(len(phrase))
print(phrase[3])#python start counting from 0 and it also count space
print(phrase.index("O"))
print(phrase.replace("DOTS","Extraordinary attorny woo"))
print(2.0981, 4+5, 4-2, 4*5, 4/2)
print(9*(2+2))
print(10%3)# % is used to show reminder division
my_num= 5 # for comp. no. written in " " is string and without that it is integer
print(my_num)
print(str(my_num)+ " is my fav no.")#str for string and it would be in bracket
print(abs(my_num))#abs is absolute value (it will not consider negative value like -5)
print(pow(3,2))#power function (3*3)
print(pow(3,2,4))# third no will divide the ans of first two no power function (3*3/4) it will show reminder only
print(max(1,2,4,8,9))#maximum no.
print(min(458,236,18))#minimum no
print(round(5.268))
from math import * # import function is give access to lot more math command
print(sqrt(36))
print(floor(55.856))#to chopp off decimal point
print(ceil(2.5))# round off
print(cos(30))
print(sinh(60))
name=input("Enter your name:")# Take value from user
age=input("Enter your age:")
print("hello" +  name +"! You are" + age)

num1=input("Enter a number : ")# programm to add a whole no.
num2=input ("Enter another number:")
result= int (num1) + int(num2)
print(result)

color=input("Enter a colour : ") # Mid labs game # input function
plural_noun=input("Enter a Plural noun: ")
celebrity=input("Enter a celebrity : ")
print("Roses are" + color)
print( plural_noun+ "are blue")
print("I love" + celebrity + "!")

lucky_number=[4,6,8,34,5]# list functions
friends = ["shrutika", "Varsha", " Mrunmai", "Oshin", "Shivai"]
friends.extend(lucky_number)# to extend the list
friends.append("Meoww")# to add into the list
friends.insert(1, "jyoti")# To insert into the list #friends.clear() to clear list # friends.remove- to remove from list
#friends.pop() # it will remove last item from list
friends.sort() # it will sort in ascending order
lucky_number.reverse() # it will show list in reverse order
print(friends)

#tuples are like list but it can't be modified after created hence called immutable.
cordinates=(4, 5)#immutable
print(cordinates[0])

#funcions
def say_hi (name , age ): # pyhon understand that we have to use function # need calling a function to execute
    print("hello" + name, "You are "+ str(age))
say_hi("khyati", 22)#Call a function
say_hi("Mrunmai", 16)

#return statement
def cube (num):
    return num*num*num# return statement- allow us to return a value back
# after return statement no function will work written in dowm line of return fun.
print(cube(4))

def cube (num):
    return num*num*num# return statement- allow us to return a value back
# after return statement no function will work written in dowm line of return fun.
result=cube(4)
print(result)

is_female=True#if and else statement
is_tall= False

if is_female or is_tall:
    print("you are a female or tall or both")
elif is_female and not(is_tall):
    print("you are short female")
elif not(is_female)and is_tall:
    print("you are a not a female but tall")
else:
    print("you are not a female nor tall")


#if and comparisons # other operators- == (double equal), >=, <=, <, >,(!=) both are not euqal

def max_num(num1, num2,num3):
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2>= num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(5,285,1245))

# calculator
num1 = float (input("Enter first number:"))
op = input("Enter operator:")
num2 = float (input("Enter second number:"))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
elif op=="*":
    print(num1*num2)
else:
    print ("Invalid operator")

# dictionary is a special structure in python which allows us to store information in key value pairs.
monthconversions = {
    "jan" : "January",
    "Feb" : "February",
    "mar ": "March",
     "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
}

print(monthconversions["Jun"])# we can also use .get to retrive the key

# while loops
i =1
while i<= 10:
    print(i)
    i += 1

print("Done with loop")

#Building a guessing game
secret_word="Mango"
guess=""
guess_count=0
guess_limit = 3
out_of_guesses = False

while guess !=secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess = input("Enter guess : ")
        guess_count +=1
    else:
        out_of_guesses= True

if out_of_guesses:
    print("You lose! Out of guess ")
else:
    print("You Win!")

#for loop
friends=["Manu", "Tanu", "Anu", "Golu"]
for index in  range(len(friends)):
    print(friends[index])

for index in range(5):
    if index==0:
        print("First iteration")
    elif index==1:
        print("You are second")
    elif index==2:
        print("Third iteration")
    elif index==3:
        print("Fourth iteration")
    else:
        print("Not first")

#Exponent function
def raise_to_power(base_num, pow_num):
    result = 1 #if we change the result it will multiply the result number and and ans of power function
    for index in range(pow_num):
        result= result*base_num
    return result
print(raise_to_power(2,10))


#2D list and nested loops
number_grid= [
    [1,2,3,],
    ["Varsha", "Khyati", "Oshin", "Shivani"],
    [4,5,6],
    [7,8,9]
]
print (number_grid[0][2])

# nested loops
number_grid= [
    [1,2,3,],
    ["Varsha", "Khyati", "Oshin", "Shivani"],
    [4,5,6],
    [7,8,9]
]
#nested loop is for loop in for loop
for row in number_grid:
    for col in row:
        print(col)

#build a translator
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation=translation+"M" #INSTED OF VOWEL IT WILL SHOW YOU LETTER M
        else:
            translation=translation+letter
    return translation

print(translate(input("Enter a Word: ")))

#build a translator
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation=translation+"M"
            else:
                translation=translation+"m"
        else:
            translation=translation+letter
    return translation

print(translate(input("Enter a Word: ")))

#try except block
try:
    number= int(input("Enter a number:"))
    print(number)
except ZeroDivisionError: # except is to catch the error
    print("Divided by zero")
except ValueError:
    print("Invalid inpur")

    employee_file = open("student.txt", "r")  # w-write, r-read, r+=read and write
    for employee in employee_file.readlines():
        print(employee)

    print(
        employee_file.readlines())  # to access specific line in file use readline and to access many use readlines and it will show you line in array

    employee_file.close()

#writing to file
employee_file=open("student.txt", "a")#a=adding employee
employee_file.write(" \nMrunmai- studdent")

employee_file.close()

#writing to file
employee_file=open("student.txt", "w")#overwrite the exsisting file #we can use it for create new file
employee_file.write(" \nMrunmai- studdent")

employee_file.close()

#writing to file
employee_file=open("student.html", "w")# create a new  HTML file
employee_file.write("<p> This is HTML</p>")

employee_file.close()

#import file name give access to another file in current file which is python file
#search python module on internet for more modules

#creat file stuent.py
class student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_on_probation= is_on_probation
#and main function is as follows
#class and objects
from student import student

student1=student("jim", "jam", 7.6, False)

print(student1.name)
#this programm will print jim

#This is data for Building MCQ
class Question:
    def __init__(self,prompt, answer):
       self.prompt=prompt
       self.answer=answer
# Building a Muiltiple Choice Quiz
from Question import Question
question_prompts = [
    "What colour are apples?\n(a) Red/Green\n(b) purple\n(c) orange\n\n",
    "What colour are Bananas?\n (a) Teal\n(b) Black\n(c)Yellow\n\n",
    "what colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
questions =[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")
]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("You got"+str(score)+ "/"+str(len(questions)) + "correct")

run_test(questions)

#Object function
#file or data for object function
class Student:

    def __init__(self, name, major, gpa):
        self.name=name
        self.major=major
        self.gpa=gpa

    def on_honor_roll(self):
        if self.gpa>=3.5:
            return True
        else:
            return False
#Main file or code to run object function
from Student import Student

student1=Student ("Oscar", "Accounting", 3.1)
student2=Student ("Phyllis", "Business", 3.8)

print(student1.on_honor_roll()
#This will show you that the cgpa of particular student is greater than assign value or not

##inheritance- we can define buch of attributes and functions and things inside of class and then we create another
#another class and we can inherit all of those attributes.
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
#File 1- Chef
class Chef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print ("The chef makes bbq ribs")
#File 2 is ChinesesChef who have all function of normal Chef and also have another speial fuctions
from Chef import Chef
class ChineseChef(Chef): # it is important to write Chef in bracket

    def make_special_dish(self):
        print("The chef makes orange chicken")


    def make_fried_rice(self):
        print("The chef makes a fired rice")

    import math
    num = int(input("enter a number"))
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i == 0):
                print(num, "is not a prime number")
        else:
            print("given number is prime number")
    else:
        print("Given number is not a prime number")




















