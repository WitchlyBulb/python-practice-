'''Drill 1
Create a class Doctor.Create two objects of Doctor.
Add attributes to your Doctor class: name, specialty.
Create 2 doctors with different names and specialties.
Add a method describe() to your Doctor class that prints name and specialty.
Call it for d1 and d2.
'''

class Doctor:
    num_doctors = 0

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        Doctor.num_doctors += 1

    def describe(self):
        print(f"Hello, my name is {self.name} and I am a doctor of {self.specialty}.")

d1 = Doctor("Harrison", "cardiology")
d2 = Doctor("Cunningham", "pediatrics")

d1.describe()
d2.describe()
print(Doctor.num_doctors)

'''Drill 2
Create a class Hospital.
Create 2 hospitals with different values.
Add attributes to your Hospital class: name, capacity.
Add a method info() to your Hospital class that prints name and capacity.
Call it for h1 and h2.'''

class Hospital: # Hospital is a class
    num_hospitals = 0 # class variable (shared across all objects)

    def __init__(self, name, capacity): # self refers to the current object
        self.name = name # self.name is an attribute
        self.capacity = capacity  #attribute (also an instance variable meaning each object has its own copy)
        Hospital.num_hospitals += 1 #(putting this here will track all objects created)

    def info(self):  #info is a method, meaning a function inside the class
        print(f"Hospital {self.name} has {self.capacity} beds") #methods act on the object's data(eg self.name)

h1 = Hospital("MGH", 1000) #h1 and h2 are objects 
h2 = Hospital("NWH", 2000) #objects store data using attributes

h1.info()
h2.info()
print(Hospital.num_hospitals)


# Encapsulation (Private/Protected Attributes)
'''Drill 3
Make the Doctor’s specialty a private attribute.
Add getter and setter methods for specialty.
Try accessing it directly (should not be recommended) and via getter (should work).'''
class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.__specialty = specialty

    def get_specialty(self):
        return self. __specialty
    
    def set_specialty(self, specialty):
        self.__specialty = specialty

d1 = Doctor("Harrison", "cardiology")
print(d1.get_specialty())


