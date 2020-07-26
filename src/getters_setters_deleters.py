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