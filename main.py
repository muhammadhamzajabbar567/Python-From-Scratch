
"""
y = "Programming Language"

def myfunc():
    global y
    y = "Fantastic"
    print("Python is " + y)
myfunc()
print("Python is " + y)
"""
'''
import random
print(random.randrange(1, 111))

'''
'''
b = 'Hello, World!'
print(b[3])
print(len(b))

txt1 ="The best things in life are !"
if "free" in txt1:
 print("yes, Free is Present")
else:
    print("No, Free is not present")
print(txt1.capitalize())

age = 21
TXT = 'My Name is Hamza, and I am {} years old'
print(TXT.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."

c = 1
d = []
print(bool(c))
print(bool(d))

class myclass():
    def __len__(self):
        return 1
myobj = myclass()
print(bool(myobj))

def myfunction():
    return False
if myfunction():
    print('Yes')
else:
    print('No')

e = 20000
print(isinstance(e, int))
'''
'''
thislist = ["apple", "banana", "cherry", "cherry"]
print(thislist)

thislist = list(("apple", "banana", "cherry", "cherry",
                 "cherry", "cherry", "cherry", "cherry", "cherry",
                 "cherry", "cherry", "cherry", "cherry", "cherry", "cherry",
                 "cherry", "cherry", "cherry", "cherry", "cherry","Mango")) # note the double round-brackets

thislist[3:18] = ['Chicko','Watermelon']
thislist.append('Kiwi')
print(thislist)
'''
'''
list1 = ['Kiwi', 'Orange', 'Banana']
list2 = ['Greyfruit', 'Mango', 'Cherry']
list1.clear()
del list2
print(list1)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist1 = ["Audi","Ferrari", "BMW", "Fortunare"]
for x in thislist1:
    print(x)

for i in range(len(thislist1)):
    print(thislist1[i])

'''
'''
fruits = ["Banana", "Apple", "Cherry"]
for x in fruits:
    print(x)

for x in "Apple":
    print(x)

#Break Statement
fruits = ["Banana", "Apple", "Cherry"]
for x in fruits:
    print(x)
    if x== "Apple":
        break

# fruits = ["Banana", "Apple", "Cherry"]
# for x in fruits:
#     if x== "Apple":
#         break
#     print(x)
#Continue Statement
fruits = ["Banana", "Apple", "Cherry"]
for x in fruits:
    if x == "Apple":
        continue
    print(x)

#Range Function
for x in range(2, 30, 5):
    print(x)
#Else in For Loop
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally Finished!")

#Nested Loops

adj = ["Red", "Yellow", "Green"]
fruits = ["Kiwi", "Orange", "Apple"]

for x in adj:
     for y in fruits:
         print(x,y)

#Pass Statement
for x in [0, 1, 2]:
    pass

#While Loop

i = 1
while i < 6:
    print(1)
    i += 1
#Break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Continue Statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#Else Statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer than 6")

#FUNCTIONS
def my_function(fname, surname, lname):
  print(fname + " " + surname + " " + lname)

my_function("Muhammad","Hamza","Jabbar")

#Parameters Or Arguments
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Muhammad Hamza", "Mughal")

#Arbitrary Arguments, *args
def my_function(*Kids):
    print("The Youngest child is " + Kids[2])
my_function("ABC", "DEF", "GHI")

#Keyword Arguments
def my_function(child3,child2,child1):
    print("The Youngest Child is " + child3)
my_function(child1= "ABC", child2= "DEF", child3= "GHI")

#Arbitrary Keyword Arguments, **kwargs
def my_function(**Kids):
    print("His Last Name is " + Kids["lname"] + " And His First Name is " + Kids["fname"])
my_function(fname = "ABC", lname= "DEF")

#Default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("Austrailia")
my_function()
my_function("USA")

#Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["Apple", "Banana", "Cheery"]
my_function(fruits)

#Return Values
def my_function(x):
    return 6 * x
print(my_function(6))
print(my_function(5))
print(my_function(28))

#The pass Statement
def my_function():
    pass

#Recursion
def tri_function(k):
    if (k > 0):
        result = k + tri_function(k - 1)
        print(result)
    else:
        result = 0
        return result
print("\n\n Recursion Example Results")
tri_function(25)
'''

#Python Lambda

x = lambda a : a + 5
print(x(15))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a,b,c : a * b + c
print(x(5, 8, 9))

#lambda functions
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

#EXAMPLE
def myfunc(x):
    return lambda a: a * x
mydoubler1 = myfunc(58)
print(mydoubler1(5))

#example2
def myfu(y):
    return lambda a: a * y
mydb = myfu(2)
mytp = myfu(3)

print(mydb(11))
print(mytp(22))

#Classes
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

#The __init__() Function
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"


p1 = person("ABC",24)
print("The Name Of the person is " + p1.name)
print(p1.age)

#Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#The self Parameter (name change self to this)
class Student:
    def __init__(this, name, age):
        this.name = name
        this.age = age
    def Info(abc):
        print("My name is " + abc.name)
        print(abc.age)


std = Student("Hamza",25)
std.Info()
#Python Inheritance

class Person(Student):
    def __init__(xyz,f_name, l_name, year):
      super().__init__(f_name,l_name)
      xyz.gradutionyear = year

    def welcome(self):
        print("Welcome ",self.name, self.age, "to the class of ", self.gradutionyear)


p3 = Person("ABC","XYZ",123)
print(p3.name)
print(p3.age)
print(p3.gradutionyear)
print(p3.welcome())

#Python Iterators

mytuple = ("Apple", "Banana", "Cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
mytuple = ("Apple", "Banana", "Cherry")

for x in mytuple:
    print(x)

mystr = "iPhone 14 PRO MAX"

for x in mystr:
    print(x)

#How to create an iterator

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

mynum = MyNumbers()
myiter = iter(mynum)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# example 2
class MyAlphabets:
    def __iter__(self):
        self.abc = "CDE"
        return self
    def __next__(self):
        H = self.abc
        self.abc += "CDE"
        return H

myalpha = MyAlphabets()
myiter1 = iter(myalpha)

print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))

# for x in myiter1:
#     print(x)
#
# #Stop Ieration
class MyNUM:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

num = MyNUM()
Iter = iter(num)

for x in Iter:
    print(x)

#Python Scope
# Local Scope
def myfunc():
    x = 300
    print(x)
myfunc()

# Function Inside Function
def myfunc():
    x = 589525
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()


# User Input

username = input("Enter UserName")
print("UserName is: " + username)

# string format()
price = 100
txt = "The Price is {} Dollars"
print(txt.format(price))