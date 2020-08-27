class My_Class():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __call__(self):

        # You can do anything you want in this method
        # But this method will get invoked when someone "types": object_name()
        return f"sum of my 2 parameters = {self.p1 + self.p2}"


my_instance = My_Class(p1=1, p2=2)

print(f"My first param = {my_instance.p1}")
print(f"My second param = {my_instance.p2}")

# By adding "()" after object, you are literally telling python interpretter to run __call__!
print(f"Using synatic suger to execute __call__:  {my_instance()}")

# The above is "syntactic sugar" for the below!
print(f"Using explicit invocation of method __call__:  {my_instance.__call__()}")
