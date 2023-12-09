# A program that defines multiple useful classes
from universities import universities
from collections import defaultdict
import sys


class Student:

    def __init__(self, utme, olevel, post_utme):
        self.utme = utme
        self.olevel = olevel
        self.post_utme = post_utme

    def calculate_aggr(self):
        return (self.utme / 8) + self.olevel + (self.post_utme * 0.4)


class University:

    universities = universities

    def __init__(self, id):
        self.id = id

    def display_universities(self):
        for uni in self.universities:
            print("{}. {}".format(uni.get("id"), uni.get("name")))

    def get_uni_index(self):
        for uni in self.universities:
            if uni.get("id") == self.id:
                uni_index = universities.index(uni)
                return uni_index

    def get_courses(self):
        uni_index = self.get_uni_index()
        courses = self.universities[uni_index].get("courses")
        return courses

    def list_courses(self):
        index = self.get_uni_index()
        print("List of Courses offered in {}".format(
            self.universities[index].get("name")))
        phrase_len = len(self.universities[index].get("name")) + len("List of Courses offered in ")
        print("=" * phrase_len)
        for course, course_details in self.get_courses().items():
            print("{}. {}".format(course_details["id"], course))

    def display_faculties_and_courses(self):
        courses = self.get_courses()
        index = self.get_uni_index()
        if courses:
            faculties = defaultdict(list)
            for course, c_details in courses.items():
                faculties[c_details["faculty"]].append(course)

            print("List of faculties under {} with their respective Departments:".format(
                universities[index].get("name")))
            phrase_len = len(self.universities[index].get("name")) + len("List of faculties under  with their respective Departments:")
            print("=" * phrase_len)

            for faculty, courses in faculties.items():
                print(faculty)
                print("=" * len(faculty))
                for i, course in enumerate(courses, start=1):
                    print("{}. {}".format(i, course))
                print()
        else:
            print("Pending...")

    def display_name(self):
        index = self.get_uni_index()
        print("{}".format(self.universities[index].get("name")))

    def about_uni(self):
        uni_index = self.get_uni_index()
        print()
        self.display_name()
        print()
        print(self.universities[uni_index].get("about"))
    
    def exit(self):
        sys.exit("Thanks for using Merit")
        