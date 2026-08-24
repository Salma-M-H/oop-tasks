class GradeBook:

    def __init__(self, className, students):
        self.__className = className
        self.__students = students

    def addStudent(self, student):
        self.__students.append(student)

    def removeStudent(self, studentId):
        for student in self.__students:
            if student.studentId == studentId:
                self.__students.remove(student)
        
    def findStudent(self, studentId):
        for student in self.__students:
            if student.studentId == studentId:
                return student.getStudentInfo()

    def getClassAverage(self):
        grades_sum = 0
        num_of_students = len(self.__students)
        for student in self.__students:
            stud_grades_sum = sum(student.grades.values())
            grades_sum += stud_grades_sum

        return grades_sum / num_of_students

    def getTopStudents(self, count): pass
    def displayAllStudents(self): pass
    def getStudentsByLetterGrade(seld, gradeLetter): pass