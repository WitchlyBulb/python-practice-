'''Level 1 — Classes & Objects Drill 1
Define a simple class called Book with no attributes.
Create two objects of the class and print them.'''
class Book: 
    pass 

b1 = Book() 
b2 = Book() 

print(b1) 
print(b2)

'''Drill 2 — Add attributes
Add two attributes to the Book class: title and author.
'''

class Book:
    """Represents a book"""

    def __init__(self, title:str, author:str) -> None:
        """Initiate a book with title and author"""
        self.title = title
        self.author = author

    # ----------Instance Methods ------------
    def book_info(self) -> None:
        """Print book info"""
        print(f"{self.title} by {self.author}")

b1 = Book("Python 101", "Dr. Code")
b2 = Book("OOP Simplified", "Priya Sawe")

b1.book_info()
b2.book_info()

'''Drill3:
Mini reinforcement
Modify your class to include a genre and a page_count, and print them as:
"Python 101 by Dr. Code — Programming (250 pages)" '''

class Book:
    """Represents a book"""

    def __init__(self, title:str, author:str, genre:str, page_count: int) -> None:
        """Initiate a book with its title, author and genre"""
        self.title = title
        self.author = author
        self.genre = genre
        self.page_count = page_count

    # --------Instance Method -------------
    def book_info(self) -> None:
        """Prints the books' information"""
        print(f"{self.title} by {self.author} - {self.genre} ({self.page_count} pages)")

# ------Create objects -------------
b1 = Book("Python 101", "Dr. Code", "Programming", 250)
b2 = Book("OOP Simplified", "Priya Sawe", "Intermediate Python", 126)

# -------Output ------------------------
b1.book_info()
b2.book_info()
     
'''Drill 4 setup:
Convert your page_count attribute into a private variable and add:
get_page_count() → to return the page count
set_page_count() → to update it (only if it’s a positive integer)''' 

class Book:
    """Represents a book's basic info"""

    def __init__(self, title: str, author: str, genre: str, page_count: int) -> None:
        """Initiate a book with title, author, genre and private page count"""
        self.title = title
        self.author = author
        self.genre = genre
        self.__page_count = page_count #private variable

    # -------------- Instance method -------------------
    def book_info(self) -> None:
        print(f"{self.title} by {self.author} - {self.genre} ({self.__page_count} pages)")

    # ------------- Getter -----------------------------
    def get_page_count(self) -> int:
        """Return page count"""
        return self.__page_count
    
    # -------------Setter -----------------------------
    def set_page_count(self, page_count: int) -> None:
        """Update page count"""
        if not int(page_count):
            raise ValueError
        self.__page_count = page_count

# Creating Book objects 
b1 = Book("Python 101", "Dr. Code", "Programming", 250)
b2 = Book("OOP Simplified", "Priya Sawe", "Intermediate Python", 126)

# Printing Book objects
b1.book_info()
b2.book_info()

# Updating page count 
b1.set_page_count(45)
b2.set_page_count(100)

# Using getters
print(b1.get_page_count())
print(b2.get_page_count())

# Printing Book objects
b1.book_info()
b2.book_info()

'''Drill 5:
Drill 1 — Private Attribute + Getter
Create a class called Patient that stores a patient’s name and diagnosis.
🔹 Make diagnosis a private attribute (__diagnosis).
🔹 Add a getter method get_diagnosis() to return it.
🔹 Then, create two patients and print each patient’s diagnosis using the getter.
💡 Hint structure:
class Patient:
    def __init__(self, name, diagnosis):
        self.name = name
        self.__diagnosis = diagnosis
    # getter here
# create two objects
# print their diagnoses'''

class Patient:
    """Represents a patient"""

    def __init__(self, name: str, diagnosis: str) -> None:
        """Initiate a patient with name and diagnosis"""
        self.name = name
        self.__diagnosis = diagnosis   #private attribute

    # ------ Instance Method -------
    def patient_info(self) -> None:
        """Prints patient name and diagnosis"""
        print(f"{self.name}: {self.__diagnosis}")

    # ------- Getter Method --------
        """Return diagnosis"""
    def get_diagnosis(self) -> str:
        return self.__diagnosis
    
    # ------ Setter Method ------
    def set_diagnosis(self, diagnosis:str) -> None:
        """Update diagnosis"""
        if not diagnosis.strip():
            raise ValueError("Diagnosis cannot be empty")
        self.__diagnosis = diagnosis
    
#creating Patient objects
p1 = Patient("Alice", "COPD")
p2 = Patient("Bobby", "IBS")

#printing Patient objects
p1.patient_info()
p2.patient_info()
# updating a diagnosis
p1.set_diagnosis("asthma")

# returning the diagnosis
print(p1.get_diagnosis())

'''Drill6:
Encapsulation Practice (Reinforcement Level)
You’ll design a class called Medication.
🧩 Your tasks:
Create a class Medication with:
Public attribute: name
Private attribute: __dose_mg
The constructor (__init__) should accept both and assign them.
Add:
get_dose() → returns dose (int)
set_dose() → updates dose only if it’s a positive integer
med_info() → prints medication info in this format:
"Aspirin: 500mg"
Create two medication objects:
"Aspirin", 500
"Ibuprofen", 200
Update Aspirin’s dose to 650 using the setter,
then print its dose with the getter.
'''
class Medication:
    """Represents a medication"""

    #-- Use a constructor to initiate a blank object--
    def __init__(self, name: str, dose: int) -> None:
        """Initiates a medication with name and dose"""
        self.name = name
        self.__dose = dose #private attribute

    # --------- Instance Method -------------
    def med_info(self) -> None:
        """prints medication info"""
        print(f"{self.name}: {self.__dose}mg")

    # ------------ Getter ------------------
    def get_dose(self) -> int:
        """returns medication dose"""
        return self.__dose
    
    # ------------ Setter ------------------
    def set_dose(self, dose:int) -> None:
        """updates medication dose"""
        if not isinstance(dose, int) or dose <= 0:
            raise ValueError("Dose must be a positive integer")
        self.__dose = dose

if __name__ == "__main__":
    # ---------- Create Objects ----------
    med1 = Medication("Aspirin", 500)
    med2 = Medication("Ibuprofen", 200)

    # -------print objects -----------
    med1.med_info()
    med2.med_info()

    # update and get private attribute 'dose'
    med1.set_dose(650)
    print(med1.get_dose())


'''Drill 7: Multiple Private Attributes
We’re going to create a class called Appointment that represents a hospital appointment.
Here’s what to do:
Define a class Appointment
It should have two private attributes:
__patient_name (string)
__time (string)
Include a constructor __init__ that initializes both.
Add getter and setter methods for each private attribute:
Validate that __patient_name isn’t empty
Validate that __time looks like "10:30 AM" (simple check: contains a space and “:”)
Add a method appt_info() that prints something like:
Appointment for Ava at 10:30 AM
In your test code:
Create two Appointment objects
Print their info
Update one using setters
Print again'''

class Appointment:
    """Represents appointment info"""

    # -- Use constructor to create a blank object --
    def __init__(self, name: str, time: str) -> None:
        """Initiates an appointment with patient name and time"""
        self.__name = name
        self.__time = time

    # -------- Instance Method --------
    def appt_info(self) -> None:
        """prints appointment info"""
        print(f"Appointment for {self.__name} at {self.__time}")
        
    # ------------ Getters ----------------
    def get_name(self) -> str:
        """returns patient name"""
        return self.__name
    
    def get_time(self) -> str:
        """returns appointment time"""
        return self.__time
    
    # -----------Setters -----------------
    def set_name(self, name: str) -> None:
        """updates patient name"""
        if not name.strip():
            raise ValueError("Patient name cannot be empty")
        self.__name = name

    def set_time(self, time: str) -> None:
        """updates appointment time"""
        if not(" " in time.strip() and ":" in time.strip()):
            raise ValueError("Please enter time in format HH:MM AM/PM")
        self.__time = time
                
if __name__ == "__main__" :
    # -------- Create Objects --------
    appt1 = Appointment("Alice", "08:30 AM")
    appt2 = Appointment("Bobby", "10:30 AM")

    # print objects using Instance Method
    appt1.appt_info()
    appt2.appt_info()

    # update an object
    appt1.set_time("11:30 AM")

    # return updated object
    print(appt1.get_time())



'''Drill 8
Patient Tracker with Hospital Count
You’ll build a Patient class that:
Keeps track of how many patients have been created (→ class variable total_patients)
Uses private attributes for name and diagnosis
Allows updating diagnosis only if not blank
Prints info like this:
Alice: COPD (City Health Center)
Bobby: IBS (City Health Center)
Total patients: 2
🧩 Step-by-step goal:
You’ll eventually make the output change like this:
STEP 1
Alice: COPD (City Health Center)
Bobby: IBS (City Health Center)
Total patients: 2
STEP 2 — Change hospital name via the CLASS
Alice: COPD (County Hospital)
Bobby: IBS (County Hospital)
Total patients: 2
STEP 3 — Change hospital name via ONE instance
Alice: COPD (Private Clinic)
Bobby: IBS (County Hospital)
Total patients: 2
'''

class Patient:
    """Represents a patient and their info"""

    # -------- Class Variables ----------
    total_patients = 0
    hospital_name = "City Health Center"

    # -------- Constructor ----------
    def __init__(self, name: str, diagnosis: str) -> None:
        """Initiates a patient with name and diagnosis"""
        self.__name = name
        self.__diagnosis = diagnosis
        Patient.total_patients += 1 #class variable, counts patients

    # -------- Instance Method ----------
    def patient_info(self) -> None:
        """prints patient info"""
        print(f"{self.__name}: {self.__diagnosis} ({self.hospital_name})")

    # -------- Getters -------------------
    def get_name(self) -> None:
        """returns patient name"""
        return self.__name
    
    def get_diagnosis(self) -> None:
        """returns diagnosis"""
        return self.__diagnosis
    
    # ---------Setters ----------------
    def set_name(self, name: str) -> None:
        """updates patient name"""
        if not name.strip():
            raise ValueError("Patient name cannot be empty""")
        self.__name = name

    def set_diagnosis(self, diagnosis: str) -> None:
        """updates diagnosis"""
        if not diagnosis.strip():
            raise ValueError("Diagnosis cannot be empty")
        self.__diagnosis = diagnosis

if __name__ == "__main__":
    # ----- Create objects --------
    pt1 = Patient("Alice", "COPD")
    pt2 = Patient("Bobby", "IBS")

    # ----- Print objects ------
    # --- step 1 ----
    print("\nSTEP 1")
    pt1.patient_info()
    pt2.patient_info()
    print(f"Total patients: {Patient.total_patients}")

    # change hosp name via class
    Patient.hospital_name = "County Hospital"

    # --- step 2 -----
    print("\nSTEP 2 — Change hospital name via the CLASS")
    pt1.patient_info()
    pt2.patient_info()
    print(f"Total patients: {Patient.total_patients}")

    # change hosp name via an instance
    pt1.hospital_name = "Private Clinic"

    # --- step 3 -----
    print("\nSTEP 3 — Change hospital name via ONE instance")
    pt1.patient_info()
    pt2.patient_info()
    print(f"Total patients: {Patient.total_patients}")

'''Drill 9:
Extend the Patient class:
Keep total_patients
Keep hospital_name
Add @classmethod to get hospital name
Create multiple patients
Update hospital via class and via instance
Use class method to print current hospital and total patients
This drill will combine:
private attributes
getters/setters
class variables
@classmethod
'''


class Patient:
    """Represents a patient and their info"""

    # -------- Class Variables ----------
    total_patients = 0
    hospital_name = "City Health Center"

    # -------- Constructor ----------
    def __init__(self, name: str, diagnosis: str) -> None:
        """Initiates a patient with name and diagnosis"""
        self.__name = name
        self.__diagnosis = diagnosis
        Patient.total_patients += 1 #class variable, counts patients

    # -------- Class Method -----------
    @classmethod
    def get_hospital_name(cls):
        """Returns hospital name"""
        return cls.hospital_name

    # -------- Instance Method ----------
    def patient_info(self) -> None:
        """prints patient info"""
        print(f"{self.__name}: {self.__diagnosis} ({self.hospital_name})")

    # -------- Getters -------------------
    def get_name(self) -> None:
        """returns patient name"""
        return self.__name
    
    def get_diagnosis(self) -> None:
        """returns diagnosis"""
        return self.__diagnosis
    
    # ---------Setters ----------------
    def set_name(self, name: str) -> None:
        """updates patient name"""
        if not name.strip():
            raise ValueError("Patient name cannot be empty""")
        self.__name = name

    def set_diagnosis(self, diagnosis: str) -> None:
        """updates diagnosis"""
        if not diagnosis.strip():
            raise ValueError("Diagnosis cannot be empty")
        self.__diagnosis = diagnosis

if __name__ == "__main__":
    # ----- Create objects --------
    pt1 = Patient("Alice", "COPD")
    pt2 = Patient("Bobby", "IBS")
    pt3 = Patient("Cathy", "CKD")
    pt4 = Patient("Dolly", "DM")

    # ----- Print objects ------
    # --- step 1 ----
    print("\nSTEP 1")
    pt1.patient_info()
    pt2.patient_info()
    pt3.patient_info()
    pt4.patient_info()

    print(f"Total patients: {Patient.total_patients}")

    # change hosp name via class
    Patient.hospital_name = "County Hospital"

    # --- step 2 -----
    print("\nSTEP 2 — Change hospital name via the CLASS")
    pt1.patient_info()
    pt2.patient_info()
    pt3.patient_info()
    pt4.patient_info()
    print(f"Total patients: {Patient.total_patients}")

    # change hosp name via an instance
    pt1.hospital_name = "Private Clinic"

    # --- step 3 -----
    print("\nSTEP 3 — Change hospital name via ONE instance")
    pt1.patient_info()
    pt2.patient_info()
    pt3.patient_info()
    pt4.patient_info()
    print(f"Total patients: {Patient.total_patients}")

    print(Patient.get_hospital_name())
    print(pt1.get_hospital_name())
    print(pt1.hospital_name)

