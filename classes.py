class Vehicle:
    def _init_(self="self",Make="Make",Model="Model",Year="Year",Weight="Weight",NeedsMaintenance="NeedsMaintenance",TripsSinceMaintenance="TripsSinceMaintenance"):
        self.myMake=Make
        self.myModel=Model
        self.myYear=Year
        self.myWeight=Weight
    def saymake(self,Make):
        self.myMake=Make
    def sayModel(self,Model):
        self.myModel=Model
    def sayYear(self,Year):
        self.myYear=Year
    def sayWeight(self,Weight):
        self.myWeight=Weight
class Car(Vehicle):
    def _init_(self,isDriving,mynumber,myMake,myModel,myYear,myWeight):
        Vehicle._init_(self,mynumber,myMake,myModel,myYear,myWeight)
        self.drive=isDriving
    def defineDrive(self):
        self.drive+=1
car1=Car(0,"234","2nd","3rd","1998","250lbs")
print(car1.myMake)
print(car1.myModel)
print(car1.myWeight)
print(car1.myYear)
car1.defineDrive()
print(car1.drive)