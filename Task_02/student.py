class Student:

    def __init__(self, name, email, grades, studentId):
        self.__name = name
        self.__email = email
        self.__grades = grades # {'subject_name': grade}
        self.__studentId = studentId

    @property
    def studentId(self):
        return self.__studentId

    @property
    def grades(self):
        return self.__grades
    

    def addGrade(self, subject, grades):
        self.__grades[subject] = grades

    def getGrade(self, subject): 
        for sub, grade in self.__grades.items():
            if sub.lower() == subject.lower():
                return grade

    def calculateAverage(self):
        grades = self.__grades.values()
        return sum(grades)/len(grades)
    
    def getLetterGrade(self): 
        total = sum(self.__grades.values())
        if 90 <= total:
            return 'A'
        elif 80 <= total:
            return 'B'
        elif 70 <= total:
            return 'C'
        elif 60 <= total:
            return 'D'
        else:
            return 'F'

    def getStudentInfo(self):
        text = f"student name: {self.__name}\n \
            student email: {self.__email} \n \
        student grades: "

        print(text)

        for sub, grade in self.__grades.items():
            print(f'    {sub}: {grade}')