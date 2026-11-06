
class baba:
    car = "BMW"
    tk = "1000 Crore"
    home = "15 Floor"

class baba2:
    SmartPhone = "Iphone"
    AC = "Walton"
    Microphone = "Fifine"

class baba3:
    Webcam = "Fifine 08"
    Laptop = "macbook"
    Camera = "dsr"

class kaka(baba,baba2,baba3):
    brokenPhone = ""            # kaka(baba): inheritance kaj korteche##  দালাল
    brokenHome = ""

k = kaka()
print(k.car)
print(k.home)
print(k.Laptop )

# inheritance 1 class(parent class / base class)er sathe r 1 ti class( child class / derived class) er proparty guluke akti somporko kore dey.
# multiple inheritance baba2,baba3, ....

