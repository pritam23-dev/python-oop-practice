
names = ["pritam","gopal","piu"]
fruits = ["apple","banana","mango"]

jora = zip(names,fruits)

print(list(jora))

# for লুপের সাথে zip() এর দারুণ ব্যবহার

names = ["pritam","gopal","piu"]
fruits = ["apple","banana","mango"]

for names, fruits in zip(names,fruits):
    print(f"{names} এর প্রিয় ফল {fruits}" )



