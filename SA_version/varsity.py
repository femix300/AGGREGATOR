#!/usr/bin/python3
"""
This a module that defines class called universities
"""
from schools import Faculty


class University:
    """Universities class definition"""
    def __init__(self, name, schools):
        """University's constructor method"""
        self.__name = name #string representing universty name
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
