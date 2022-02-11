class Student:
  def __init__(self, name, surname, grade, points):
    self.name = name
    self.surname = surname
    self.grade = grade
    self.points = points
    


matej = Student("Matej", "Tlapak", 6, 28)

print(matej.name)
print(matej.surname)
print("Je v " + str(matej.grade) + ".rocniku a ma", matej.points, "bodu")

def ma_zapocet(student, max_body):
    if student.points / max_body >= 0.5:
        print("ma zapocet")
    else:
        print("nema zapocet")

ma_zapocet(matej, 40)


studenti = [
    Student("Matej", "Tlapak", 6, 28),
    Student("Lucka", "Hockova", 6, 32),
    Student("Max", "Klimes", 6, 5)
]

for student in studenti:
    print(student.name)
    ma_zapocet(student, 40)
    
def prumer_bodu(pole_stud):
    pass

prumer_bodu(studenti)

class Student2:
  def __init__(self):
    self.name = "Max"
    self.surname = "Klimes"

student2 = Student2()
print(student2.name)
