import unittest

class TestUniversity(unittest.TestCase):
    def test_constructor(self):
        name = "MIT"
        schools = ["Engineering", "Science"]
        university = University(name, schools)

        self.assertEqual(university.name, name)
        self.assertEqual(university.schools, schools)

    def test_name_property(self):
        university = University("MIT", ["Engineering"])

        new_name = "Havard"
        university.name = new_name
        self.assertEqual(university.name, new_name)

        with self.assertRaises(ValueError):
            university.name = 123  # Should raise a ValueError

    def test_schools_property(self):
        university = University("Havard", ["Humanities"])

        new_schools = ["Humanities", "Commerce"]
        university.schools = new_schools
        self.assertEqual(university.schools, new_schools)

        with self.assertRaises(ValueError):
            university.schools = "Invalid"  # Should raise a ValueError

    def test_display_method(self):
        university = University("Test University", ["FacultyA"])
        data = ["CourseA", "CourseB"]

        with unittest.mock.patch('builtins.print') as mock_print:
            university.display("Test University", data)

            # Assert that the display method printed the correct message
            mock_print.assert_called_with("You qualify for the following courses in Test University:")
            mock_print.assert_any_call("1. CourseA")
            mock_print.assert_any_call("2. CourseB")

    def test_admission_method(self):
        # Note: For testing methods like admission, it's usually better to refactor
        # the code to make it more testable and modular. Here, we just test if the method runs without errors.
        University.admission()

if __name__ == '__main__':
    unittest.main()

