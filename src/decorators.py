####################
# Use case 1
# Create decorator with function
####################

def salutation(person):
    print(f"Hello, {person}")

# This is always how decorator is defined (i.e., with func as single argument)
def my_decorator(func):

    # The wrapper should always take *args, **kwargs
    # NOTE:  This wrapper is returned
    #        So, the *args, **kwargs are actually taking arguments from the
    #        the call of the wrapped function and get passed to the func
    #        as *args, **kwargs
    #
    # NOTE2:  *args, **kwargs in def of wrapper() are saying optional args, kwargs
    #         *args, **kwargs in call of func() are "slotting" args, kwargs to
    #          actual arguments of the decorated function
    def wrapper(*args, **kwargs):

        # This happens when the decorated function is executed
        print("This is new functionality from decorator")

        # This happens when the decorated function is executed
        return func(*args, **kwargs)

    # The wrapper is returned UNEXECUTED
    # Like loaded gun but trigger not pulled until the decorated
    # function is executed
    return wrapper

# Base case
print("running un-decorated function")
print("================================")
salutation("Mandy")
print()

# Using decorator without @
print("running function decorator around function (without @)")
print("================================")
salutation = my_decorator(salutation)
salutation("Mandy")
print()

# Using decorator with @
print("running function decorator around function (with @)")
print("================================")

@my_decorator
def salutation(person):
    print(f"Hello, {person}")

salutation("Mandy")
print()

####################
# Use case 2
# Create decorator with class
#
# NOTE:  use of __call__()
####################

class My_Decorator:

    # As above, the only "argument" to the decorator class/function
    # is func
    def __init__(self, func):
        self.func = func

    # The __call__ is just like the wrapper
    # It takes the args and is executed when the decorated function
    # is exeucuted
    # NOTE:  *args, **kwargs are optional arguments
    def __call__(self, *args, **kwargs):

        # This happens when the decorated function is executed
        print("This is new functionality from CLASS decorator")

        # This happens when the decorated is executed
        # NOTE:  *args, **kwargs are saying to "slot" args/kwargs
        #        to func's arguments as appropriate
        return self.func(*args, **kwargs)


# Using decorator with @
print("running class decorator around function (with @)")
print("================================")

@My_Decorator
def salutation(person):
    print(f"Hello, {person}")

salutation("Mandy")
print()

####################
# Use case 3
# Use functools update_wrapper for stacking class decorators
####################

class My_Decorator2:
    """I am creating a 2nd decorator to show how to stack decorators"""

    # As above, the only "argument" to the decorator class/function
    # is func
    def __init__(self, func):
        self.func = func

    # The __call__ is just like the wrapper
    # It takes the args and is executed when the decorated function
    # is exeucuted
    # NOTE:  *args, **kwargs are optional arguments
    def __call__(self, *args, **kwargs):

        # This happens when the decorated function is executed
        print(f"This is new functionality from CLASS decorator 2")
        try:
            print(f"function name = {self.func.__name__}")
        except AttributeError:
            print("could not get __name__ of original function")

        # This happens when the decorated is executed
        # NOTE:  *args, **kwargs are saying to "slot" args/kwargs
        #        to func's arguments as appropriate
        return self.func(*args, **kwargs)

# Stacking 2 decorators
print("stacking 2 class decorators around function (with @)")
print("inner function tries to access __name__")
print("================================")
@My_Decorator
@My_Decorator2
def salutation(person):
    print(f"Hello, {person}")

salutation("Mandy")
print()

# Stacking 2 decorators
print("stacking 2 class decorators around function (with @)")
print("outer function tries to access __name__")
print("this will fail without @wraps")
print("================================")
@My_Decorator2
@My_Decorator
def salutation(person):
    print(f"Hello, {person}")

salutation("Mandy")
print()


# We will fix problem with __name__ by using update_wrapper
from functools import update_wrapper


class My_Decorator2:
    """I am creating a 2nd decorator to show how to stack decorators"""

    # As above, the only "argument" to the decorator class/function
    # is func
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    # The __call__ is just like the wrapper
    # It takes the args and is executed when the decorated function
    # is exeucuted
    # NOTE:  *args, **kwargs are optional arguments
    def __call__(self, *args, **kwargs):

        # This happens when the decorated function is executed
        print(f"This is new functionality from CLASS decorator 2")
        try:
            print(f"function name = {self.func.__name__}")
        except AttributeError:
            print("could not get __name__ of original function")

        # This happens when the decorated is executed
        # NOTE:  *args, **kwargs are saying to "slot" args/kwargs
        #        to func's arguments as appropriate
        return self.func(*args, **kwargs)

# Stacking 2 decorators
print("stacking 2 class decorators around function (with @)")
print("this will now works with update_wrapper")
print("================================")
@My_Decorator2
@My_Decorator
def salutation(person):
    print(f"Hello, {person}")
salutation("Mandy")
print()

####################
# Use case 4
# Use functools @wraps for stacking function decorators
####################

def my_decorator2(func):

    # Always wrap the wrapper with @wraps to perserve names
    # Always define the wrapper to include *args, **kwargs which
    # you pass to the func being decorated
    # So that the decorated function can have arguments!
    def wrapper(*args, **kwargs):

        # This is executed when the decorated function is executed
        print("This is from functional decorator #2!")
        print(f"name of decorated function = {func.__name__}")

        # Be sure to load the decorated function with its arguments
        return func(*args, **kwargs)

    # Return the wrapper LOADED but not exeucted
    return wrapper

# Stacking 2 decorators
print("stacking 2 function decorators around function (with @)")
print("this will not work without @wraps")
print("================================")
@my_decorator2
@my_decorator
def salutation(person):
    print(f"Hello, {person}")
salutation("Mandy")
print()


from functools import wraps

# Always create decorator with func as argument

def my_decorator(func):

    # The wrapper should always take *args, **kwargs
    # NOTE:  This wrapper is returned
    #        So, the *args, **kwargs are actually taking arguments from the
    #        the call of the wrapped function and get passed to the func
    #        as *args, **kwargs
    #
    # NOTE2:  *args, **kwargs in def of wrapper() are saying optional args, kwargs
    #         *args, **kwargs in call of func() are "slotting" args, kwargs to
    #          actual arguments of the decorated function
    @wraps(func)
    def wrapper(*args, **kwargs):

        # This happens when the decorated function is executed
        print("This is new functionality from decorator")

        # This happens when the decorated function is executed
        return func(*args, **kwargs)

    # The wrapper is returned UNEXECUTED
    # Like loaded gun but trigger not pulled until the decorated
    # function is executed
    return wrapper

def my_decorator2(func):

    # Always wrap the wrapper with @wraps to perserve names
    # Always define the wrapper to include *args, **kwargs which
    # you pass to the func being decorated
    # So that the decorated function can have arguments!
    @wraps(func)
    def wrapper(*args, **kwargs):

        # This is executed when the decorated function is executed
        print("This is from functional decorator #2!")
        print(f"name of decorated function = {func.__name__}")

        # Be sure to load the decorated function with its arguments
        return func(*args, **kwargs)

    # Return the wrapper LOADED but not exeucted
    return wrapper

# Stacking 2 decorators
print("stacking 2 function decorators around function (with @)")
print("this will now works with @wraps")
print("================================")
@my_decorator2
@my_decorator
def salutation(person):
    print(f"Hello, {person}")
salutation("Mandy")
print()

####################
# Use case 5
# Now pass arguments to decorator function
####################

# Unusual use case to pass arguments to decorator
# Just like above with one more layer of wrapping

def dec_with_args(x):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            # This is executed when the decorated function is executed
            print(f"this is arg passed to decororater x={x}")
            print("This is from functional decorator #2!")
            print(f"name of decorated function = {func.__name__}")

            # Be sure to load the decorated function with its arguments
            return func(*args, **kwargs)
        return wrapper
    return my_decorator

print("Using decorator with arguments")
print("================================")
@dec_with_args(x=17)
def salutation(person):
    print(f"Hello, {person}")
salutation("Mandy")
print()







