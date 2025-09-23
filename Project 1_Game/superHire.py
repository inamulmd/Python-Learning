class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):
        print("This is the Child class.")
        super().show()  # Call Parent class method

# Create object of Child class
c = Child()
c.show()
