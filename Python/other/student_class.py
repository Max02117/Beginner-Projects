class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def __str__(self):
        return f"Имя: {self.name}; Возраст: {self.age}; Курс: {self.course}."
    
student1 = Student("Max", 18, 2)
print(student1)