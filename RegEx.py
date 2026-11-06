# import re
#
# #Check if the string starts with "The" and ends with "Spain":
#
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
#
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")


# import re
#
# txt = "The rain in Spain"
# #Check if "ain" is present at the end of a WORD:
# x = re.findall(r"ain\b", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# import re
# text = "The rain in Spain"
# y = re.findall(r"\bSpa", text)
# #z = re.findall(r"ain\b", text)
# print(y)
# if y:
#   print("Yes. there is at least one match!")
# else:
#   print("No match")

# import re
# txt = "The rain in Spain"
# #Find all lower case characters alphabetically between "a" and "m":
# x = re.findall("[a-m]", txt)
# print(x)
#
# import re
# text = "The rain in Spain"
# #Find all lower case characters alphabetically between "a" and "m":
# y = re.findall("[a-m]",text)
# print(y)
#
# import re
# Text = "Dhaka is the capital of Bangladesh"
# p = re.findall("[a-m]",Text)
# print(p)

# import re
# txt = "That will be 59 dollars"
# #Find all digit characters:
# x = re.findall("\\d", txt)
# print(x)
#
# import re
# Roll = " My roll number is 05"
# y = re.findall("\\d",Roll)
# print(y)
#
# import re
# My_age = " I'm 20 years old"
# z = re.findall("\\d",My_age)
# print(z)

# import re
# txt = "hello planet"
# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
# x = re.findall("he..o", txt)
# print(x)
#
# import re
# text = "hello planet"
# y = re.findall(".....t",text)
# print(y)
#
# import re
# mytext = "my id number is 34257"
# z = re.findall("nu....",mytext)
# print(z)

# import re
# txt = "hello planet"
# #Check if the string starts with 'hello':
# x = re.findall("^hello", txt)
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")
#
#
# import re
# txt = "hello planet"
# x = re.findall("^hello",txt)
# print(x)
# if x:
#   print("Yes, The string starts with 'hello'")
# else:
#   print("No match")

# import re
#
# txt = "hello planet"
#
# #Check if the string ends with 'planet':
#
# x = re.findall("planet$",txt)
# if x:
#   print("Yes, the string ends with 'planet'")
# else:
#   print("No match")

# import re
# txt = "hello planet"
# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters,
# # and an "o":
# x = re.findall("pl.*.t", txt)
# print(x)
#
# import re
# txt = "hello planet"
# #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
# x = re.findall("he.+o", txt)
# print(x)

# import re
# txt = "hello planet"
# #Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
# x = re.findall("he..?o", txt)
# print(x)
# #This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

# import re
# txt = "helllo planet"
# #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
# x = re.findall("he.{3}o", txt)
# print(x)

# import re
# txt = "The rain in Spain falls mainly in the plain!"
# #Check if the string contains either "falls" or "stays":
# x = re.findall("falls|stays", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")













