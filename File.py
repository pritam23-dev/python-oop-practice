# creat own module মানে হলো একই file er kono function , list, etc. অন্য কোনও file এ module হিসেবে import kore বার বার use kora.

# import Module

import Module as kaka

kaka.pritam()

kaka.piu()

print(kaka.x)

print(kaka.person1["country"])

from Module import karim

karim()








# x = open("text.text","r")   # file open , read, write, change
# print(x.read())

# wr = open("pritam.html","a")      # r+ diye read & write 2 tai kora jay
#
# wr.write("tumi amay subscribe koro\n")
# wr.write("i love u \n")
#
# # print(wr.read())

# import os     # file remove
# os.remove("demofile.txt ")

# import os
#
# os.mkdir(".gitignore ")

import os

if os.path.exists(".gitignore "):
    os.rmdir(".gitignore ")
    print("Folder deleted")
else:
    print("The folder does not exist")



