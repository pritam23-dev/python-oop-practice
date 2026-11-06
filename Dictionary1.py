# ACCESS DICTIONALY ITEMS

# mydict = {
#     "name"  : "pritam",
#     "age"   : 20 ,
#     "class" : "honours"
# }
# print(mydict["name"])
# x = mydict.get("age")
# print(x)
#
# x = mydict.keys()
# print(x)
#
# y = mydict.values()
# print(y)
# x = mydict.keys()
# y = mydict.values()
#
# mydict["number"] = 7890355
#
# print(x)
# print(y)
#
# z = mydict.items()
#
# print(z)

##### CHANGE ITEMS ##***## and ADD item aki

# MYdict = {
#     "my_age" : 20 ,
#     "year"   : 2007
# }

# MYdict["year"] = 2007

# MYdict.update({"number" : 1631400691})
#
# print(MYdict)

### remove doctionary

# MYdict = {
#     "my_age" : 20 ,
#     "year"   : 2007 ,
#     "number" : 78890989
# }

# MYdict.pop("year")

# MYdict.popitem()  # seser item delete kore

#del MYdict["year"]

#del MYdict

# MYdict.clear()

# print(MYdict)


#### Loop Through a Dictionary

# Mydict = {
#     "sum1" : 10,
#     "sum2" : 20,
#     "sum3" : 30
# }
#
# for x in Mydict:
#     print(x)
#
# for a in Mydict:
#     print(Mydict[a])
#
# for y in Mydict.keys():
#     print(y)
#
# for b in Mydict.values():
#     print(b)
#
#
# for p,s in Mydict.items():
#     print(p,s)
#
# for item in Mydict.items():
#     print(item)


#### Copy Dictionaries

Mydict = {
    "sum1" : 10,
    "sum2" : 20,
    "sum3" : 30
}

print(Mydict)

x = Mydict.copy()
print(x)

y = dict(Mydict)
print(y)








