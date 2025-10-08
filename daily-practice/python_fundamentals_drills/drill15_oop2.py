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

    def patient_info(self, name: str, diagnosis: str) -> None:
        """Initiate a patient with name and diagnosis"""
        self.name = name
        self.diagnosis = diagnosis
        

