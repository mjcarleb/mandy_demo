def squares_gen():

    """Generate an infinite sequence of squares"""

    i = 0
    while True:

        # Python stops here until next is applied to generator
        # After next is applied, execution continues until the next yield
        yield i**2
        i += 1

print("Example Squares Generator:  ")
o = squares_gen()
for i in range(10):
    print(next(o))
print()

def fib_gen():

    """Generate an infinite sequence of fibinocci numbers"""

    # Python stops here until next is applied to generator
    # After next is applied, execution continues until the next yield
    yield 1

    # Python stops here until next is applied to generator
    # After next is applied, execution continues until the next yield
    yield 1

    a=1
    b=1
    while True:
        c = a + b

        # Python stops here until next is applied to generator
        # After next is applied, execution continues until the next yield
        yield c
        a = b
        b = c

print("Example Fib Generator:  ")
o = fib_gen()
for i in range(10):
    print(next(o))
print()
