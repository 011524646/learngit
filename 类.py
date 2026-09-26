class Student:
    def __init__(self,name,age):
        self.name_=name
        self.age_=age
    def print(self):
        print("姓名:"+self.name_ ,"年龄:"+str(self.age_))
s1=Student("abcd",23)
s2=Student("bc",20)
s3=Student("sdawd",33)
s1.print()
s2.print()
s3.print()