'''
single , multiple , multi level
TODO
super , mro 
'''
class A:
    def feture1(self):
        print("feture 1")
    def feture2(self):
        print("feture 2")

class B(A): #* Means B is inherited from A
    def feture3(self):
        print("feture 3")
    def feture4(self):
        print("feture 4")

a1 = A()
print(a1.feture1())
print(a1.feture2())

a2 = B()
print(a2.feture1())