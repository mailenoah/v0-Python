class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        print("This will run when i call s1 or s2")
    
    def result (self):
        print(f"The result is {self.marks}")

s1 = Student("John", 20, 85)
s2 = Student("Alice", 22, 90)

print(s1.name)  # Output: John
print(s2.age)   # Output: 22

s3= Student("Bob", 19, 75)

s3.result()  # Output: The result is 75