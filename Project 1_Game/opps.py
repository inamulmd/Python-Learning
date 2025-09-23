class Student:
    # Constructor to initialize student details
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade
 
    # Method to display student details
    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Grade:", self.grade)

# Create an object of the Student class
student1 = Student("Inamul", 101, "A")

# Call the method to display data
student1.display()
