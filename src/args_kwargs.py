######################
# Use of * or ** when defining functions with unknown optional arguments
######################

def my_function(arg1, arg2, arg3=None, *args, **kwargs):
    """

    :param arg1: a mandatory argument
    :param arg2: another mandatory argument
    :param arg3:  an optional argument
    :param args: an optional, variable number of arguments determined by person calling function
    :param kwargs: an optional dictioanry
    :return:  the sum of all the arguments
    """

    # arg1 and arg2 are mandatory
    my_sum = arg1 + arg2

    # arg3 is optional
    if arg3 is not None:
        my_sum += arg3

    # *args means optional, tuple of values
    for arg in args:
        my_sum += arg

    # **kwargs means optional, dictionary of values
    for k,v in kwargs.items():
        my_sum += v

    # Show total
    return my_sum

# Only mandatory values passed in
x= my_function(arg1=3, arg2=10)
print(f"Just 2 mandatory args, sum = {x}")
print()

# Pass in 3 other values to arg3
# first 2 now must be unnamed
x = my_function(arg1=3, arg2=10, arg3=100)
print(f"With 3rd optional arg, sum = {x}")
print()


# Pass optional/variable number of key values (that caller gets to decide on)
x= my_function(arg1=3, arg2=10, arg3=100, key1=100, key2=200)
print(f"With kwargs, sum = {x}")
print()

# Pass 5 unnamed values....first 3 go to 3 positional values, last 2 go as tuple to *args
x= my_function(3, 10, 100, 100, 200)
print(f"With args, sum = {x}")
print()

######################
# Use of * or ** when calling a function
# Separate from usage above
######################

# Putting * in front of l in function slots elements of l into first 3 positional arguments
l = [1,2,3]
x = my_function(*l)
print(f"With *l being slotted to first 3 positional arguments, sum = {x}")
print()

# Putting * in front of l in function slots elements of l into first 3 positional arguments
l = [1,2,3, 4, 5, 6, 7]
x = my_function(*l)
print(f"With *l being slotted to first 3 positional arguments & *args, sum = {x}")
print()

# Now slot an actual dictionary into key word arguments (not **kwargs)
d = dict()
d["arg1"] = 1
d["arg2"] = 2
d["arg3"] = 3
x = my_function(**d)
print(f"With **d being slotted to first 3 named arguments, sum = {x}")
print()

# Now slot an actual dictionary into key word arguments and **kwargs
d = dict()
d["arg1"] = 1
d["arg2"] = 2
d["arg30"] = 3
x = my_function(**d)
print(f"With **d being slotted to first 3 named arguments, sum = {x}")
print()
