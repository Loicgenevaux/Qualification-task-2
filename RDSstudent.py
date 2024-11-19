import numpy as np
from student import TUstudent

class RobustDataScienceStudent (TUstudent):
    def __init__(self, name,age, date,study_program, matricule,courses,favourite):
        super().__init__(name,age,date,study_programm,matricule,courses,favourite)
        