#!/usr/bin/python3
"""
This a module that defines class called universities
"""
from SA_version.schools import Faculty


class University:
    """Universities class definition"""
    def __init__(self, name, schools):
        """University's constructor method"""
        self.__name = name #universty name (string)
        self.__schools = schools #list whose elements are of type Faculty

    @property
    def name(self):
        """University name's getter method"""
        return self.__name

    @name.setter
    def name(self, name):
        """University name's setter method"""
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Name must be a string")

    @property
    def schools(self):
        """University school's getter method"""
        return self.__schools

    @schools.setter
    def schools(self, faculties):
        """University name's setter method"""
        if isinstance(faculties, list):
            self.__schools = facuties
        else:
            raise ValueError("Courses must be a list")

    def display(self, u_name, data=None):
        if data:
            count = 0
            var = "course" if len(data) == 1 else "courses"
            print("You qualify for the following {} in {}:".format(var, u_name))
            data.sort()  #sorts the courses
            for course in data:
                count = count + 1
                if int(count / 10) == 0:
                    print(" {}. {}".format(count, course))
                else:
                    print("{}. {}".format(count, course))
        else:
            print("Unfortunately,", end=" ")
            print("you don't qualify for any course in {}.".format(u_name))
    
    @classmethod
    def admission(cls, data_base=[]):
        st_courses = []
        """
        The following loop prompts the user to enter
        a university of his/her choice
        """
        loop = 1
        while (loop):
            names = ["ukzn", "up", "uct", "uj", "us", "wits"]
            print("You can choose from the following list of universities")
            for choice in names:
                print("{}".format(choice), end=" ")
            print()

            univ_name = str(input("Enter your university name: "))
            if univ_name in names:
                loop = 0 #sets loop to zero to terminate the while loop
            
        for univ in data_base:
            if univ_name == univ.name:
                engl_score = int(input("Enter your english score: "))
                aps_score = int(input("Enter your aps score: "))
                if aps_score < 29 or engl_score < 50:
                    univ.display(univ_name, st_courses)
                    return

                s = ["Technical", "Science", "other"]
                print("Matric streams 1", end=" ")
                print("({}), 2 ({}) and 3 ({})".format(s[0], s[1], s[2]))
                stream = int(input("Enter your matric stream: "))
                if stream == 1 or stream == 2:
                    maths_sc = int(input("Enter your mathematics score: "))
                    physics_sc = int(input("Enter your physics score: "))
                if stream == 2:
                    bio_sc = int(input("Enter your life sciences score: "))
                for school in univ.schools:
                    engl_req = school.requirements["english"]
                    aps_req = school.requirements["aps"]
                    if (aps_score >= aps_req and engl_score >= engl_req):
                        if len(school.requirements) == 2:
                            for course in school.courses:
                                st_courses.append(course)
                        else:
                            maths_req = school.requirements["maths"]
                            if len(school.requirements) > 3:
                                phys_req = school.requirements["physics"]
                            if stream == 1 or stream == 2:
                                if len(school.requirements) == 3:
                                    if maths_sc >= maths_req:
                                        for course in school.courses:
                                            st_courses.append(course)
                                elif len(school.requirements) == 4:
                                    if (maths_sc >= maths_req and
                                            physics_sc >= phys_req):
                                        for course in school.courses:
                                            st_courses.append(course)
                                else:
                                    bio_req = school.\
                                            requirements["life sciences"]
                                    if stream == 2:
                                        if (maths_sc >= maths_req):
                                            if (physics_sc >= phys_req 
                                                    or bio_sc >= bio_req):
                                                for course in school.courses:
                                                    st_courses.append(course)
        univ.display(univ_name, st_courses)
