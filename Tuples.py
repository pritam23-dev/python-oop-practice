# NewTuples = (1,2,3,"pritam",True)

# print(type(NewTuples))

# NewTuples[3] = 4
# print(NewTuples)

# Negative indexing
# print(NewTuples[-1])

# Range of Indexes

# print(NewTuples[2:4])

### Update tuples

# x = ("apple","banana","orange")
# y = list(x)
# y[2] = "mango"
#
# x = tuple(y)
#
# print(x)
#
# y = (1,2,3)
# x =(4,)
#
# y += x
#
# print(y)
#
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.pop(1)
# thistuple = tuple(y)
#
# print(thistuple)

#
# # unpacking tuple #easy
#
# name = ("pritam","piku","dip","nirad")
#
# (a,*b,c) = name
#
# print(b)

######Loop Tuples

thistuple1 = ("apple","banana","cherry")
for x in thistuple1:
    print(x)

thistuple2 = ("apple","banana","cherry")
for x in range(len(thistuple2)):
    print(x)
    print(thistuple2[x])

thistuple3 = ("apple","banana","cherry","mango")
i = 0
while i < len(thistuple3):
    print(thistuple3[i])
    i += 1

# Join Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# tuple method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# y = thistuple.index(8)
y = thistuple.count(8)

print(y)


