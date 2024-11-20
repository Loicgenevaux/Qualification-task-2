from student import TUstudent
import unittest


class TestTUStudent(unittest.TestCase):
    def test_initialization(self):
        student = TUstudent(
            name="David",
            age=21,
            date="11-11-2011",
            study_program="Elektrotechnik und Informationstechnik",
            matricule=1234567,
            courses=["Math", "Physics", "Programming", "Datascience", "History"],
            favourite="Math"
        )
        self.assertEqual(student.name, "David")
        self.assertEqual(student.age, 21)
        self.assertEqual(student.date, "11-11-2011")
        self.assertEqual(student.study_program, "Elektrotechnik und Informationstechnik")
        self.assertEqual(student.matricule, 1234567)
        self.assertEqual(student.courses, ["Math", "Physics", "Programming", "Datascience", "History"])
        self.assertEqual(student.favourite, "Math")

    def test_study_program(self):
        with self.assertRaises(ValueError) as context:
            TUstudent(
                name="David",
                age=21,
                date="11-11-2011",
                study_program="Invalid",
                matricule=1234567,
                courses=["Math", "Physics", "Programming", "AI", "Ethics"],
                favourite="Math"
            )
        self.assertEqual(str(context.exception), "Study program invalid")

    def test_matricule(self):
        with self.assertRaises(ValueError) as context:
            TUstudent(
                name="David",
                age=21,
                date="11-11-2011",
                study_program="Elektrotechnik und Informationstechnik",
                matricule=12345,  # Invalid matricule length
                courses=["Math", "Physics", "Programming", "AI", "Ethics"],
                favourite="Math"
            )
        self.assertEqual(str(context.exception), "Matriculation number must be 7-digit")

    def test_courses(self):
        with self.assertRaises(ValueError) as context:
            TUstudent(
                name="David",
                age=21,
                date="11-11-2011",
                study_program="Elektrotechnik und Informationstechnik",
                matricule=1234567,
                courses=["Math", "Physics"],  # Not enough courses
                favourite="Math"
            )
        self.assertEqual(str(context.exception), "Minimum courses accomplished number should be 5")

    def test_favourite_course(self):
        with self.assertRaises(ValueError) as context:
            TUstudent(
                name="David",
                age=21,
                date="11-11-2011",
                study_program="Elektrotechnik und Informationstechnik",
                matricule=1234567,
                courses=["Math", "Physics", "Programming", "AI", "Ethics"],
                favourite="InvalidCourse"
            )
        self.assertEqual(str(context.exception), "Favourite courses have to be an accomplished course")


if __name__ == "__main__":
    unittest.main()
    