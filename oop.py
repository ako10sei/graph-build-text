class Person:
    name = "Ivan"
    surname = "Belov"
    age = 10

    def set(self,name,surname='Belov',age=10):
        self.name=name
        self.surname=surname
        self.age=age

class Student(Person):
    course = 1

igor = Student()
igor.set("Влад")
vlad = Person()
vlad.set("Влад","Скворцов",20)


print(f"{igor.name} {igor.surname} {igor.age} лет")
