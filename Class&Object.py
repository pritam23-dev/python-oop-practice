class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def introduce(self):
        print(f"আমার নাম {self.name}, রোল {self.roll}")
                                                                    # HARD
S1 = Student("Pritam", 101)
S2 = Student("Rahim",102)

S1.introduce()
S2.introduce()

####

class Student:
    roll = ""   # প্রপার্টি / এট্রিবিউট
    gpa = ""    # প্রপার্টি / এট্রিবিউট

rahim = Student()       # অবজেক্ট
#print(isinstance(rahim,Student))
rahim.roll = 101
rahim.gpa = 3.43
print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")
                                                                # EASY
korim = Student()       # অবজেক্ট
korim.roll = 102
korim.gpa = 3.89
print(f"Roll : {korim.roll}, GPA : {korim.gpa}")














