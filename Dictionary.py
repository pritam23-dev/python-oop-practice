studentInfo = {
    "pritam" : {
        "name" : "Pritam",       # nested dictionary
        "profession" : "Programmer",
        "loccation" : "Madaripur",
        "age" : 19,
        "number" : 8885550
        #"number" : 0197666
        #পাইথনে (Python) কোনো সাধারণ সংখ্যার (যেমন: ৯ বা ৭) শুরুতে শূন্য বসালে (যেমন: 09 বা 07) এই SyntaxError বা কোডিং ভুলটি দেখায়।
    },
    "siam" : {
        "name" : "Siam",
        "profession" : "Worker",
        "loccation" : "Faridpur",
        "age" : 20,
        "number" : 0o124566,
        "number" : 0o124566 # no copy / no duplicate
        # শুরুতে শুধু 0 না লিখে 0o (শূন্য এবং ছোট হাতের o) বা 0O লিখুন। tahole eti octal number hobe
    }
}
# print(studentInfo["pritam"]["number"])
# print(studentInfo["siam"]["number"])
# print(studentInfo["siam"])
# print(len(studentInfo["pritam"]))
print(len(studentInfo))
# mydict = dict(name="pritam",age=19,profession="programmer")
# print(mydict)
# print(type(mydict))

# Loop Through Nested Dictionaries

# for x, obj in studentInfo.items():
#     print(x)
#
#     for y in obj:
#         print(y + ":" , obj[y])
for x, obj in studentInfo.items():
    print(x)

    for y in obj:
        print(y + ":" , obj[y])








