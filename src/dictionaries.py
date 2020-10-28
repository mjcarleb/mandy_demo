# people = {'Julian': 30, 'Bob': 35, 'Michael': 38}
# print(people)
#
# print(people.keys())
#
# for keys, values in people.items():
#     print(f'{keys} is {values} of age')

#
# def fib(num: int, msg: str):
#     try:
#         assert (num > 0), "Please give a number greater than 0"
#     except AssertionError as msg:
#         print(msg)
#     """(This is called a docstring, contains info about the function)
#        This function calculates the first `num` numbers in the
#        Fibonacci sequence.
#        ----
#        Arguments: the number of numbers to create
#        ----
#        Returns: a list containing those numbers
#     """
#     # your code here
#     fib_list = {1:0, 2:1}
#     if num==1:
#         return fib_list
#     if num==2:
#         return fib_list
#     else:
#         for i in range(3, num+1):
#             #add two previous numbers to get the next list element listel
#             fib_list[i] = fib_list[i-1]+fib_list[i-2]
#
#     return fib_list
#
# print(fib(4, "msg"))



# x=[1,2,[[3,4,5], [6,7,8,9]]]
# print(x[2][1][0])
#
# x = list(range(1,10))
# x.append(11)
# print(x)

# fibonacci = []
# a, b = 0,1
# while b<=4:
#     fibonacci.append(b)
#     a,b = b, a+b
# print(fibonacci)

#a,b
#b=1
#fibonacci[1]
#0, 1 = 1, 1
#fibonacci[1,1]
#1, 1, = 1, 2
#fibonacci[1,1,2]
#1, 2 = 2, 3
#fibonacci[1,1,2,3]
#2,3 = 3, 5

n=5
f=1
for i in range(1, n+1):
    f = f*i
print(n, "! = ", f, sep='')

#f=1*1=1
#f=1*2=2
#f=2*3=6
#f=6*4=24
#f=24*5=5

#5!=120

#total/8 = 127.3
#total = 127.3*8 = 1018.4
#1018.4+58=1076.4
#1076.4/9