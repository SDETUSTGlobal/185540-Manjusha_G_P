class myClass():
    def method(self):
        print("Guru99")
class childClass(myClass):
    def method1(self):
        print("childClass Method1")
    def method2(self):
        print("childClass method2")


c2 = childClass()
c2.method()
c2.method1()
c2.method2()
