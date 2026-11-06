list = [1,2,3,"Pritam","Korno"]     # iterable

# for i in list:
#     print(i)

x = iter(list)    # iterator
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(next(x))
print(next(x))

fruits = ["আম","জ্যাম","কাঁঠাল"]   # iterable

it = iter(fruits)               # iterator

print(next(it))
print(next(it))
print(next(it))











