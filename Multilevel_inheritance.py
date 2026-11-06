class baba:
    car = "Bugatti"
    tk = "1 trillion"
    home = "3 luxury houses"

class son1(baba):
    smartPhone = "I-phone"
    AC = "Walton"
    microphone = "Fifine"

class son2(son1):
    camera = "DSLR"
    Laptop = "Mac-book"
    Bike = "R15"

class son3(son2):
    BrokenPhone = ""
    BrokenHome = ""

s3 = son3
print(s3.Laptop)
print(s3.car)

s2 = son2
print(s2.home)

s1 = son1
print(s1.tk)

# oporer class gulo holo parent r nicher gulu child , so child class parent er poparty use korte parbe but parent child er proparty use korte parbe na
# eder aro akta type ache ta holo "" Hierarchical inheritance 














