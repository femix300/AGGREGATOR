#!/usr/bin/python3
"""
This a module that defines class called universities
"""
from engine.schools import Faculty


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
        """
        Displays the list of courses that the student qualifies for,
        from the university of his or her choice
        """
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
        """
        Finds the list of courses that the student qualifies for
        from a university of his or her choice
        """

        st_courses = []
        """
        The following loop prompts the user to enter
        a university of his/her choice
        """
        loop = 1
        while (loop):
            names = ["ukzn", "up", "uct", "uj", "us", "wits"]
            print("Choose from the following list of universities")
            for choice in names:
                print("{}".format(choice), end=" ")
            print()

            # Prompts the user to enter the university of his or her choice
            univ_name = str(input("Enter your university name: "))

            # check if the user input is among the supported list of varsities
            if univ_name in names:
                # Exit the loop if the student's choice is in 'names' list
                loop = 0
            
        for univ in data_base:
            if univ_name == univ.name:
                while True:
                    engl_score = input("Enter your English score (0-100): ")
                    aps_score = input("Enter your APS score (0-42): ")

                    if engl_score.isdigit() and aps_score.isdigit():
                        engl_score = int(engl_score)
                        aps_score = int(aps_score)

                        if 0 <= engl_score <= 100 and 0 <= aps_score <= 42:
                            # Exit the loop if 'engl_score'
                            break
                        else:
                            print("Re-enter the values.")
                            print("Make sure they're within the specified ranges.")
                    else:
                        print("Re-enter the values.")
                        print("Make sure you enter valid digits.")

                if aps_score < 29 or engl_score < 50:
                    univ.display(univ_name, st_courses)
                    return

                s = ["Technical", "Science", "other"]
                
                while True:
                    print("Matric streams 1", end=" ")
                    print("({}), 2 ({}) and 3 ({})".format(s[0], s[1], s[2]))
                    stream = input("Enter your matric stream: ")
                    if stream.isdigit():
                        stream = int(stream)
                        if stream > 0 and stream < 4:
                            # If the stream is within [1, 3], exit the loop
                            break
                #Checks if the student is Technical or Science
                if stream == 1 or stream == 2:
                    while True:
                        maths_sc = input("Enter your maths score(0-100): ")
                        physics_sc = input("Enter your physics score(0-100): ")
                        # Check if both maths_sc and physics_sc are digits
                        if maths_sc.isdigit() and physics_sc.isdigit():
                            # Convert maths_sc and physics_sc to integers
                            maths_sc = int(maths_sc)
                            physics_sc = int(physics_sc)
                            if ((maths_sc >= 0 and maths_sc < 101)
                                    and physics_sc >= 0 and physics_sc < 101):
                                # If both scores are valid, exit the loop
                                break
                            else:
                                """
                                If scores are not within the valid range,
                                prompt the user to re-enter values
                                """
                                print("Re-enter the values")
                                print("Make sure they're within 0-100 range")
                        else:
                            """
                            If input values are not composed of digits,
                            prompt the user to re-enter valid digits
                            """
                            print("Re-enter the values.")
                            print("Make sure you enter valid digits.")
                # Checks if the student is from Science stream
                if stream == 2:
                    while True:
                        """
                        Prompt the user to enter their life sciences score
                        and store it in the variable 'bio_sc'
                        """
                        bio_sc = input("Enter your life sciences score(0-100): ")

                        # Check if the input consists only of digits
                        if bio_sc.isdigit():
                            """
                            Convert the input to an integer,
                            if it contains only digits
                            """
                            bio_sc = int(bio_sc)
                            
                            # Check if the entered score is within [0, 100]
                            if bio_sc >= 0 and bio_sc < 101:
                                # Exit the loop if the score is valid
                                break
                            else:
                                """
                                Print an error message
                                if the score out of range
                                """
                                print("Re-enter the value")
                                print("Make sure it's within the specified range")
                        else:
                            """
                            Print an error message
                            if the input does not consist of valid digits
                            """
                            print("Re-enter the value.")
                            print("Make sure you enter valid digits.")
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
                                if stream == 1:
                                    bio_sc = 0
                                if len(school.requirements) == 3:
                                    if maths_sc >= maths_req:
                                        for course in school.courses:
                                            st_courses.append(course)
                                elif len(school.requirements) == 4:
                                    if (maths_sc >= maths_req and
                                            physics_sc >= phys_req):
                                        for course in school.courses:
                                            st_courses.append(course)
                                elif len(school.requirements) == 5:
                                    bio_req = school.\
                                            requirements["life sciences"]
                                    if (maths_sc >= maths_req):
                                        if (physics_sc >= phys_req
                                                or bio_sc >= bio_req):
                                            for course in school.courses:
                                                st_courses.append(course)
        univ.display(univ_name, st_courses)
