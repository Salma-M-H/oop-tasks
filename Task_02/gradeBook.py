class GradeBook:

    def __init__(self, className):
        self.__className = className
        self.__students = []

    def addStudent(self, student):
        self.__students.append(student)

    def removeStudent(self, studentId):
        self.__students = [student for student in self.__students if student.studentId != studentId]
        
    def findStudent(self, studentId):
        for student in self.__students:
            if student.studentId == studentId:
                return student.getStudentInfo()

    def getClassAverage(self):
        students_avg = []
        for student in self.__students:
            student_avg = student.calculateAverage()
            students_avg.append(student_avg)

        class_avg = round(sum(students_avg) / len(self.__students), 2)
        return class_avg

        
    def getTopStudents(self, count):
        students_with_grades = {student: student.getTotalScore() for student in self.__students}
        sorted_students = dict(sorted(students_with_grades.items(), key=lambda item: item[1], reverse=True))
        TopStudents = list(sorted_students.keys())
        return TopStudents[:count]


    def displayAllStudents(self):
        print(f"=== {self.__className} - All Students ===")
        for student in self.__students:
            print(f"{student.studentId} - {student.name}: {student.calculateAverage()} ({student.getLetterGrade()})")

        
    def getStudentsByLetterGrade(self, gradeLetter):
        studentsWithGrade = {student: student.getLetterGrade() for student in self.__students}
        studentsList = []
        for student, grade in studentsWithGrade.items():
            if grade.lower() == gradeLetter.lower():
                studentsList.append(student)

        return studentsList
        
