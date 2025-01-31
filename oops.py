# Self keyword is mandatory in python to call variable name into method
# Instance variable and class variable have whole different purpose
# Constructor name should always be __init__
# New keyword is not required when you create object


class calculator():
    num = 100       # This is the class variables
    # If we don't define the constructor, on run time in python it takes default constructor automatically
    def __init__(self, a, b):           # Self is global and store every variable
        self.firstNumber = a
        self.secondNumber = b           # This is instance variable
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + self.num # Self can also be use to call the comman variable. We can also use "calculator.num".

obj = calculator(5, 9)  #Syntax to create object in python
obj.getData()
print(obj.num)
print(obj.summation())

obj1 = calculator(9, 7)  # We can create multiple objects. In all the objects class variable will be constent.
obj1.getData()
print(obj1.num)
print(obj1.summation())
