class TUstudent :
    """
    Class student from TU Darmstadt
    """
    def __init__(self, name, age, registration_date, 
                 study_program, matricule_number,accomplished_courses
                 , favourite_courses):
        self.name=name
        self.age=age
        self.registration_date=registration_date
        self.study_program=study_program
        self.matricule_number=matricule_number
        self.accomplished_courses=accomplished_courses
        self.favourite_courses=favourite_courses

    @property
    def get_name(self):
        return self.name
    @property
    def get_age(self):
        return self.age
    @property
    def get_registration_date(self):
        return self.registration_date
    @property
    def get_study_program(self):
        return self.study_program
    @property
    def get_matricule_number(self):
        return self.matricule_number
    
    # Import des bibliothèques nécessaires
from datetime import date


# Création d'un étudiant en Robust Data Science
print("\nCréation d'un étudiant en Robust Data Science...")
rds_student = RobustDataScienceStudent(
    name="Bob Robust",
    age=25,
    registration_date="2020-09-01",
    study_program="Robust Data Science",
    registration_number=456789
)

# Test des getters
print("\nInformations de l'étudiant Robust Data Science :")
print("Nom :", rds_student.get_name())
print("Âge :", rds_student.get_age())
print("Date d'inscription :", rds_student.get_registration_date())
print("Programme d'études :", rds_student.get_study_program())
print("Numéro d'inscription :", rds_student.get_registration_number())

# Ajout de cours accomplis et d'un cours préféré
print("\nAjout de cours accomplis et d'un cours préféré pour Bob...")
rds_student.set_courses(["Programming", "Statistics", "AI", "Robotics", "Ethics"])
rds_student.set_favorite_course("Robotics")

print("Cours accomplis :", rds_student.get_courses())
print("Cours préféré :", rds_student.get_favorite_course())



