#!/usr/bin/python3
"""University Faculty class definition"""


class Faculty:
    """Body of class(Faculty) definition"""
    def __init__(self, name, courses, requirements):
        """Constructor method"""
        self.__name = name
        self.__courses = courses
        self.__requirements = requirements

    @property
    def name(self):
        """name's getter method"""
        return self.__name

    @name.setter
    def name(self, faculty_name):
        """name's setter method"""
        self.__name = faculty_name

    @property
    def courses(self):
        """courses' getter method"""
        return self.__courses

    @courses.setter
    def courses(self, courses):
        """courses' setter method"""
        self.__courses = courses

    @property
    def requirements(self):
        """admission requirement's getter method"""
        return self.__requirements

    @requirements.setter
    def requirements(self, requirement):
        """admission requirement's setter method"""
        self.__requirements = requirement
