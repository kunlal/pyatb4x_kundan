class Person:
    # attribute class static variables
    _id = 12
    __atte = 30
    name = "kundan"
    age = 30
    weight = 70.12
    address = "bangalore Marathalli  560016"

    def __init__(self, gender, marks_10th):
        self.gender = gender
        self.marks10 = marks_10th
        print(self._id)
        print("Class initialized!....")

    def getDetails(self,mobno):
        print("ID ",self._id)
        print("ID2: ",Person._id)
        print("Name",self.name)
        self.mobile = mobno
        print(self.mobile)
        print("gender ",self.gender)

p1 = Person("Male", 500)
p1.getDetails(9045889023)
print(p1._id)
print(p1.name)
print(p1.gender)
print(p1.mobile)
