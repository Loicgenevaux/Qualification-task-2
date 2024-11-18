class Date :
    def __init__(self,date_str):
        self._date_str = date_str
        self._year = None
        self._month = None
        self._day = None
        self.test_date(date_str)

    def test_date (self, date_str):
        try:
            number = date_str.split("-")
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
    
    def get_day(self):
        return self._day

    def get_month(self):
        return self._month

    def get_year(self):
        return self._year

    def __str__(self):
        return f"{self._day}-{self._month}-{self._year}"

class Human ():

    def __init__(self, name, age):
        if not name:
            raise ValueError("Missing name")
        self._name=name

        if age <0:
            raise ValueError("Age is not negative")
        self._age=age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
    
    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}"

class TUstudent (Human):
    def __init__(self, name,age, date_str,study_program, matricule,courses,fav_courses):
        
        tu_programs=[
            "Aerospace Engineering","Angewandte Linguistik","Architektur","Energy Science and Engineering","Elektrotechnik und Informationstechnik"
        ]

        super().__init__(name, age)
        self._date = Date(date_str)
        
        if study_program not in tu_programs:
            raise ValueError("study program invalid")
        self._study_program=study_program
        if not isinstance(matricule, int) or len(str(matricule)) != 7:
            raise ValueError("Matriculation number must be 7-digit")
        self._matricule=matricule

        if len(courses)!=5:
            raise ValueError("Minumum courses accomplished number should be 5")
        self.courses=courses

        if fav_courses not in courses :
            raise ValueError("Favorite courses have to be an accomplished courses")
        self.fav_courses=fav_courses

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
    
    def get_date(self):
        return self._date

    def get_study_program(self):
        return self._study_program

    def get_matricule(self):
        return self._matricule
    

    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nDate: {super().__str__()}\nStudy program: {self._study_program}\nMatricule number: {self._matricule}\nAccomplished courses: {self.courses}\nFavorite courses: {self.fav_courses}"

def main():
    s1=TUstudent("David Dupond",21,"11-11-2011","Elektrotechnik und Informationstechnik",1234567,["e","m","p","t","h"],"e")
    print(s1)

    print("\ngetters:")
    print("Name:", s1.get_name())
    print("Age:", s1.get_age())
    print("Matricule:", s1.get_matricule())
    print("Study program:", s1.get_study_program())
    print("Date:", s1.get_date())

if __name__=="__main__":
    main() 