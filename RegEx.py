import re

txt = "The rain in spain"
x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 5h95 dollars"
x = re.findall("\d", txt)
print(x)

txt = "Hello Planet"
x = re.findall("P..n.t", txt)
print(x)

txt = "Hello Planet"
x = re.findall("^Hello", txt)
if x:
  print("Yes, the string starts with 'Hello' ")
else:
  print("No match")

x = re.findall("He.{2}o", txt)
print(x)

txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# split func
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

import re

txt = "Python is a Programming Language"
x = re.split("\s", txt, 1)
print(x)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())

import camelcase

c = camelcase.CamelCase()
txt = "hello pakistan"
print(c.hump(txt))