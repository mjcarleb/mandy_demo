#property is a built-in function creating and returning property object
#property object has three methods which are getter(), setter(), and deleter()

class datasciencelearningnerds:
    def __init__(self):
        # self.intelligence = 150

        self.attitude = "cool"

    #function to get value of intelligence
    @property
    def intelligence(self):
        print("This is the getter method in property object")
        return self._i

    #function to set value of intelligence
    @intelligence.setter
    def intelligence(self, i):
        if i < 130:
            print("No one with low IQ is allowed!")
            return
        self._i = i

    # #function to delete intelligence attribute
    # def del_intelligence(self):
    #     del self.intelligence

    # intelligence = property(get_intelligence, set_intelligence, del_intelligence)


Mandy = datasciencelearningnerds()
Mandy.intelligence=300
print(Mandy.intelligence)

#Now using the @property decorator


# class datasciencelearningnerds:
#     def __init__(self):
#         self.intelligence = 150
#
#     #using property decorator
#     #a getter function
#     @property
#     def intelligence(self):
#         print("Getting value")
#         return self.intelligence
#
#     #setter function
#     @intelligence.setter
#     def intelligence(self, i):
#         print("Setting value")
#         if i < 150:
#             raise ValueError("you are not smart enough for data science")
#         self.intelligence=i
#
# dumbo = datasciencelearningnerds()
# dumbo.intelligence=149
# print(dumbo.intelligence)


