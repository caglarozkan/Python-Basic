class StudentGrades:
    def __init__(self):
        self.records=[]

    def add_Student(self, name, grade):
        self.records.append((name, grade))

    def __iter__(self):
        for names in self.records:
            if names[1] >= 50:
                print("Greater thane 50: ")
                yield names[0]

students = StudentGrades()
students.add_Student("John", 40)
students.add_Student("Hassan", 76)
students.add_Student("Jack", 32)
students.add_Student("Jacob", 91)

for student in students:
    print(student)