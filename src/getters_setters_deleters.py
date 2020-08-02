####################
# Use case 1
# Create "getter" using @property
####################

class rectangle:

    def __init__(self, l, w):
        self.l = l
        self.w = w

    # This makes accessing the property method just like accessing the property attribute
    # usage to get area:   r.area
    # non-usage to get area:  r.area()
    @property
    def area(self):
        return self.l * self.w

r = rectangle(l=3, w=2)

try:
    print(f"Area of the rectangle using method = {r.area()}")
except TypeError:
    print("I got TypeError trying to use area() as method")

# Lets use the property
print(f"Area of the rectangle using property = {r.area}")



####################
# Use case 2
# Create setter
####################

class person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # This makes accessing the property method just like accessing the property attribute
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@email.com"

    # NOTE:  Using same name of function (email)
    # Now I can "get" via getter above
    # Or I can set using same function below
    @email.setter
    def email(self, email_address):
        fname, lname = email_address[:-10].split(".")
        self.fname = fname
        self.lname = lname

p = person("Mandy", "Wong")
print(f"Names given = {p.fname}, {p.lname}")

p.email = "mark.carlebach@email.com"
print(f"New names derived from email = {p.fname}, {p.lname}")

####################
# Use case 3
# Use deleter
####################

class person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # This makes accessing the property method just like accessing the property attribute
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@email.com"

    # NOTE:  Using same name of function (email)
    # Now I can "get" via getter above
    # Or I can set using same function below
    @email.setter
    def email(self, email_address):
        fname, lname = email_address[:-10].split(".")
        self.fname = fname
        self.lname = lname


    @email.deleter
    def email(self):
        print(f"removing {self.fname}.{self.lname}@email.com")
        self.fname = None
        self.lname = None

p = person("Mandy", "Wong")
print(f"Names given = {p.fname}, {p.lname}")

p.email = "mark.carlebach@email.com"
print(f"New names derived from email = {p.fname}, {p.lname}")

del p.email

# Now use setter for validation
# KEY INSIGHT:
#    a)  object attribute, getter and setter are all named the same (age)
#    b)  setter sets a hidden/shadow version of age (i.e., age_saved)
#    c)  getter returns hidden/shadow version of age (i.e.,, age_saved)
from datetime import datetime


class Person(object):
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.age_saved

    @age.setter
    def age(self, age_input):
        if age_input < 0:
            raise ValueError("Age cannot be negative")
        self.age_saved = age_input

p=Person(10)
p.age = 3 # try -3
p.age


# Use case validation
class Rectangle(object):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    @property
    def h(self):
        return self.h_saved

    @property
    def w(self):
        return self.w_saved

    @h.setter
    def h(self, h):
        if h < 0:
            raise ValueError("Height cannot be negative")
        self.h_saved = h

    @w.setter
    def w(self, w):
        if w < 0:
            raise ValueError("Width cannot be negative")
        self.w_saved = w


rect1 = Rectangle(2, 2)
rect1.h = 4
print(rect1.h)
print()
rect1.w = 2 # try -3


# Use case integrity
class Person(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property  # getter
    def email(self):
        return f"{self.fname}.{self.lname}@email.com"

    @email.setter  # setter
    def email(self, _):
        # Write code to check conditions or return error
        raise ValueError("email == fname.lname@email.com")


mark = Person("Mark", "Carlebach")
print(mark.email)
