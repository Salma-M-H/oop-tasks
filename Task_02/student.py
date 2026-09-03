class Student:

    def __init__(self, studentId, name, email):
        self.__name = name
        self.__email = email
        self.__grades = {} # {'subject_name': grade}
        self.__studentId = studentId

    @property
    def studentId(self):
        return self.__studentId

    @property
    def grades(self):
        return self.__grades

    @property
    def name(self):
        return self.__name
    

    def addGrade(self, subject, grades):
        self.__grades[subject] = grades

    def getGrade(self, subject): 
        for sub, grade in self.__grades.items():
            if sub.lower() == subject.lower():
                return grade

    def calculateAverage(self):
        grades = self.__grades.values()
        return round(sum(grades)/len(grades), 2)
    
    def getLetterGrade(self): 
        stud_grade = self.calculateAverage()
        
        if 90 <= stud_grade:
            return 'A'
        elif 80 <= stud_grade:
            return 'B'
        elif 70 <= stud_grade:
            return 'C'
        elif 60 <= stud_grade:
            return 'D'
        else:
            return 'F'

    def __print_grades(self):
        text = ""
        for sub, grade in self.__grades.items():
            text += f"\t{sub}: {grade}\n"
        return text


    def getStudentInfo(self):
        text = f"=== Student Information === \nID: {self.__studentId} \nName: {self.__name} \nE-mail: {self.__email} \nGrades:\n{self.__print_grades()} "
        return text


    def getTotalScore (self):
        return sum(self.__grades.values())
