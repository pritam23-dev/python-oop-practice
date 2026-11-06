# 3 method ➡️ Instance/normal , class , static 

class className:
    def InstanceMethod(self,):
        print(f"Hello instance method")

    @classmethod
    def ClassMethod(cls):
        print("This is class Method")

    @staticmethod
    def StaticMethod():
        print("Hello static Method")

v1 = className()
v1.InstanceMethod()

v1.ClassMethod()
className.ClassMethod()

v1.StaticMethod()
className.StaticMethod()

