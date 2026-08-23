class Student:

    def __init__(self, name, email, grades, studentId):
        self.__name = name
        self.__email = email
        self.__grades = grades # {'subject_name': grade}
        self.__studentId = studentId

    def addGrade(self, subject, grades):
        self.__grades[subject] = grades

    def getGrade(self, subject): 
        for sub, grade in self.__grades.items():
            if sub.lower() == subject.lower():
                return grade

    def calculateAverage(self):
        grades = self.__grades.values
        return sum(grades) #TODO: make sure the syntax is valid

    def getLetterGrade(self): pass
    def getStudentInfo(self): pass