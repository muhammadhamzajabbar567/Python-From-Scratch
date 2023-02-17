try:
    print(x)
except:
    print("An exception occured")

# ---------------------------------------------------------------------------------------------------


try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# ---------------------------------------------------------------------------------------------------


try:
    print("Hello")
except:
    print("Something went Wrong")
else:
    print("Nothing went wrong")

# ---------------------------------------------------------------------------------------------------


try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished ")

# ---------------------------------------------------------------------------------------------------


try:
    f = open("demofile.txt")
    try:
        f.write("lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

# Raisa an Exception

                       # Exception

x = -1

if x < 0:
    raise Exception("Sorry, No Numbers below zero")

# ---------------------------------------------------------------------------------------------------

ab = -6
if ab >= 1:
        raise Exception("Value of Variable is smaller than 1")

# ---------------------------------------------------------------------------------------------------

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")

