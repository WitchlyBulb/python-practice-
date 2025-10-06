'''Drill 1: Classes & Objects
Create a class Nurse.
Make two objects: n1 and n2.
Print both objects.'''

class Nurse: #this is the class
    pass

n1 = Nurse() # these are the objects or instances, we are attributing them to class Nurse
n2 = Nurse()

print(n1)
print(n2)

'''Drill 2: Attributes
Create a class Nurse that has:
Two attributes: name and department (set inside __init__)
Create two nurses with different values
Print both their names and departments'''

class Nurse: #blueprint or class
    def __init__(self, name, dept): # self refers to the current object
        self.name = name #attribute = instance variable --> each object will have its own copy
        self.dept = dept #will be storing some data about each object in class Nurse

    def nurse_info(self): #this is a function used inside a class, it is called "method",
        #method tells us what to do with the attributes of the object
        print(f"{self.name} works in {self.dept}") #self.name refers to the attribute of the
        #current object 'self' but the method will apply to every object or instance in class Nurse

n1 = Nurse("Sally", "GI") 
n2 = Nurse("Molly", "ICU")

n1.nurse_info() #here we are applying the method to the attributes name and dept of the instances
n2.nurse_info()

'''
Drill3: Class Variables
Create a class Nurse that:
Has a class variable num_nurses = 0
Increments it each time a new nurse is created (__init__)
Print the total number of nurses after creating two objects'''
class Nurse: #defining a blueprint or class for our objects
    num_nurses = 0 # class variable which will get applied across all objects from this class

    def __init__(self, name, dept): # constructor that helps initialize an object, and assigns it some attributes
        self.name = name # we create a generalized object 'self' 
        self.dept = dept # we give it the attributes we want every object in this class to have
        Nurse.num_nurses += 1 #to increment the class variable per object

    def nurse_info(self): # this is called method, its a function that helps us do something with the attributes
        print(f"{self.name} works in {self.dept}") # we are still using general object self to create a template

n1 = Nurse("Sally", "GI")
n2 = Nurse("Molly", "ICU")

n1.nurse_info()
n2.nurse_info()
print(Nurse.num_nurses)

'''Drill4: Add getters and setters for multiple attributes
Take your Nurse class (with name and dept) and:
Make both attributes private (__name and __dept)
Add getter and setter methods for both
Create one nurse object
Print the name and dept using getters
Update both using setters and print again'''

class Nurse: 
    num_nurses = 0

    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept
        Nurse.num_nurses += 1

    def nurse_info(self):
        print(f"{self.__name} works in {self.__dept}")

    # -------------------------------------
    def get_name(self):
        return self.__name
    
    def get_dept(self):
        return self.__dept
    
    # -----------------------------------
    def set_name(self, name):
        self.__name = name
    
    def set_dept(self, dept):
        self.__dept = dept

    
n1 = Nurse("Sally", "GI")
print(n1.get_name())
print(n1.get_dept())

n1.set_name("Molly")
n1.set_dept("ICU")
print(n1.get_name())
print(n1.get_dept())


'''Drill: LabTest Class

Write a class called LabTest that does the following:
Tracks how many tests have been created (use a class variable and a class method to access it safely).
Each test should have:
test_name (string)
patient_name (string)
result (optional — may be None until entered)
Add a method set_result(self, result: float) -> None
Updates the result
Add a method get_result(self) -> float | None
Returns the result
Add a @classmethod named get_total_tests(cls)
Returns how many tests have been created (don’t access the class variable directly)
Example expected behavior:
t1 = LabTest("Glucose", "Ava")
t2 = LabTest("Cholesterol", "Leo", 210.5)
t3 = LabTest("Hemoglobin", "Mia")

t3.set_result(12.8)

print(t1.get_result())      # None
print(t2.get_result())      # 210.5
print(t3.get_result())      # 12.8
print(LabTest.get_total_tests())  # 3
'''

class LabTest:
    """Represents a lab test"""

    #class variable
    num_tests = 0

    def __init__(self, test_name: str, patient_name: str, result=None) -> None:
        """initiate a LabTest with test name, pt name and result"""
        self.__test_name = test_name
        self.__patient_name = patient_name
        self.__result = result
        LabTest.num_tests += 1

    # ---------------- Instance Methods -----------------
    def test_result(self) -> None:
        """Print lab tests"""
        print(f"Patient {self.__patient_name}: {self.__test_name} {self.__result}")

        # ---------------- Getters ---------------------------
    def get_test_name(self) -> str:
        """Return test name"""
        return self.__test_name
        
    def get_patient_name(self) -> str:
        """Return patient's name"""
        return self.__patient_name
        
    def get_result(self) -> float | None:
        """Return test result"""
        return self.__result
        
    # --------------- Setters ----------------
    def set_test_name(self, test_name: str) -> None:
        """Update test name"""
        if not test_name.strip():
            raise ValueError("Test name cannot be empty")
        self.__test_name = test_name

    def set_patient_name(self, patient_name: str) -> None:
        """Update patient name"""
        if not patient_name.strip():
            raise ValueError("Patient name cannot be empty")
        self.__patient_name = patient_name

    def set_result(self, result=None) -> None:
        """Update lab result"""
        self.__result = result

    # -----------------Class Method -----------------------
    @classmethod
    def get_num_tests(cls) -> int:
        """Return the total number of lab tests"""
        return cls.num_tests
        
# -------------- Example Usage ----------------------
if __name__ == "__main__":
    # Creating LabTest objects
    t1 = LabTest("Glucose", "Ava")
    t2 = LabTest("Cholesterol", "Leo", 210.5)
    t3 = LabTest("Hemoglobin", "Mia")

    # Printing test results
    t1.test_result()   # Patient Ava: Glucose None
    t2.test_result()   # Patient Leo: Cholesterol 210.5
    t3.test_result()   # Patient Mia: Hemoglobin None

    # Updating a result
    t3.set_result(12.8)
    t3.test_result()   # Patient Mia: Hemoglobin 12.8

    # Using getters
    print(t1.get_result())      # None
    print(t2.get_result())      # 210.5
    print(t3.get_result())      # 12.8

    # Using class method to get total tests
    print("Total lab tests:", LabTest.get_num_tests())  # 3

    # Using setters to update patient info
    t1.set_patient_name("Lila")
    t1.set_test_name("Hct")
    t1.set_result(23.0)

    # Verify updates
    print(t1.get_patient_name())   # Lila
    t1.test_result()               # Patient Lila: Hct 23.0