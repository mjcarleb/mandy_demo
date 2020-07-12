from functools import reduce

# Create map to convert centrigade to farenheight
m = map(lambda c:  9/5 * c + 32, [0, 30, 100])
print(list(m))

# filter temperaturs above freezing
f = filter(lambda x:  x > 32, [0,10,20,30,40,50,60])
print(list(f))

# Add up all the terperatures in celsiss
r1 = reduce(lambda a,b:  a+b, [0,30, 100])
print(r1)

# Add up all the terperatures in celsiss
#r2 = reduce(lambda a,b:  a+b, list(m))
#print(r2)

# Add up all the terperatures in celsiss
m = map(lambda c:  9/5 * c + 32, [0, 30, 100])
r2 = reduce(lambda a,b:  a+b, m)
print(r2)
