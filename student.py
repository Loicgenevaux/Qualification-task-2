class Human ():
    def __init__(self, name, age, date):
        self.name=name
        self.age=age
        self.date = date
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name=name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        if age <0:
            raise ValueError("Age is not negative")
        self._age=age

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        try:
            number = date.split("-")
            if len(number) != 3:
                raise ValueError("Date should look like : 'YYYY-MM-DD'.")
            self._day = int(number[0])
            self._month = int(number[1])
            self._year = int(number[2])

            if not (1 <= self._month <= 12):
                raise ValueError("month should be between 1 and 12.")
            if not (1 <= self._day <= 31):
                raise ValueError("Days should be between 1 et 31.")
        except ValueError as file:
            raise ValueError(f"Error on date : {file}")
        self._date=date
    
    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nDate: {self._date}"

class TUstudent (Human):
    def __init__(self, name,age, date,study_program, matricule,courses,favourite):
        


        super().__init__(name, age,date)
        self.study_program=study_program
        self.matricule=matricule
        self.courses=courses
        self.favourite=favourite

    @property
    def study_program(self):
        return self._study_program
    
    @study_program.setter
    def study_program(self, study_program):
        tu_programs=[
            "Aerospace Engineering","Angewandte Linguistik","Architektur","Energy Science and Engineering","Elektrotechnik und Informationstechnik"
            ]
        if study_program not in tu_programs:
            
            raise ValueError("study program invalid")
        self._study_program=study_program
    
    @property
    def matricule(self):
        return self._matricule
    @matricule.setter
    def matricule (self, matricule):
        if not isinstance(matricule, int) or len(str(matricule)) != 7:
            raise ValueError("Matriculation number must be 7-digit")
        self._matricule=matricule
    
    @property
    def courses(self):
            return self._courses
    @courses.setter
    def courses(self, courses):
        if len(courses)!=5:
            raise ValueError("Minumum courses accomplished number should be 5")
        self._courses=courses
    
    @property
    def favourite(self):
        return self._favourite
    
    @favourite.setter
    def favourite(self, favourite):
        if favourite not in self.courses :
            raise ValueError("Favourite courses have to be an accomplished courses")
        self._favourite=favourite
    

    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nDate: {self._date}\nStudy program: {self._study_program}\nMatricule number: {self._matricule}\nAccomplished courses: {self.courses}\nFavourite courses: {self.favourite}"

def main():
    s1=TUstudent("David Dupond",21,"11-11-2011","Elektrotechnik und Informationstechnik",1234567,["e","m","p","t","h"],"e")
    print(s1)

if __name__=="__main__":
    main() 