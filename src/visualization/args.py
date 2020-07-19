def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum(1, 2, 3))

def concatenate(**mydict):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in mydict.values():
        result += arg
    return result

print(concatenate(a="Python", b=" ", c="Is", d=" ", e="Awesome!"))

