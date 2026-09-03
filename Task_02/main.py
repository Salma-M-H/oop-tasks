from gradeBook import GradeBook
from student import Student

gradeBook =  GradeBook("Computer Science 101")

# Create students
student1 = Student("S001", "Alice Johnson", "alice@school.com")
student2 = Student("S002", "Bob Smith", "bob@school.com")
student3 = Student("S003", "Charlie Brown", "charlie@school.com")

# Add grades for students
student1.addGrade("Math", 95.0)
student1.addGrade("English", 88.0)
student1.addGrade("Science", 92.0)

student2.addGrade("Math", 78.0)
student2.addGrade("English", 85.0)
student2.addGrade("Science", 80.0)

student3.addGrade("Math", 90.0)
student3.addGrade("English", 92.0)
student3.addGrade("Science", 89.0)

# Add students to gradebook
gradeBook.addStudent(student1)
gradeBook.addStudent(student2)
gradeBook.addStudent(student3)

# Display all students
gradeBook.displayAllStudents()
print()

# Get class average
print("Class Average: " + str(gradeBook.getClassAverage()))


# Get top students
topStudents = gradeBook.getTopStudents(2)
print("Top 2 Students:")
for student in topStudents:
    print(student.name + ": " + str(student.calculateAverage()))

# Get student info
print(student1.getStudentInfo())
