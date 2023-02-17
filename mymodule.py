# Create a Module
def greeting(name):
    print("Hello," + name)

# Use A Module
import mymodule
mymodule.greeting("Hamza")

# Variables in Module
person1 = {
    "Name": "Muhammad Hamza Jabbar",
    "Age": 21,
    "Country": "Pakistan"
}

import mymodule
a = mymodule.person1["Name"]
b = mymodule.person1['Age']
c = mymodule.person1["Country"]
print(a, b, c)

# RE-Naming a Module
import mymodule as mmd
a = mmd.person1["Name"]
print(a)

# Built In Modules
import platform
x = platform.uname()
print(x)

# Using the dir() Function
import platform
x = dir(platform)
print(x)

# Import From Module
def Info(name):
    print("Hello, " + name)
client  = {
    "Name": "Muhammad Hamza Mughal",
    "Age": 21,
    "Country": "Pakistan"
}
from mymodule import client

print(client["Name"])