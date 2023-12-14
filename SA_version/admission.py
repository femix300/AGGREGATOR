#!/usr/bin/python3
from varsity import University
from schools import Faculty
from ukzn_data_base import ukzn_data
from up_data_base import up_data
from wits_data_base import wits_data
from uct_data_base import uct_data
from us_data_base import us_data
from uj_data_base import uj_data


def display(data=[], name=""):
    if len(data) > 0:
        var = "course" if len(data) == 1 else "courses"
        print("You qualify for the following {} in {}:".format(var,name))
        data.sort()
        for course in data:
            print(course)
    else:
        print("Unfortunately you don't qualify for any course in {}" \
                .format(name))

def admission(data):
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

    for univ in data:
        if univ_name == univ.name:
            engl_score = int(input("Enter your english score: "))
            aps_score = int(input("Enter your aps score: "))
            if aps_score < 29 or engl_score < 50:
                display(st_courses, univ_name)
                return

            print("Matric streams 1 (Technical), 2 (Science) and 3 (other)")
            stream = int(input("Enter your matric stream: "))
            if stream == 1 or stream == 2:
                maths_score = int(input("Enter your mathematics score: "))
                physics_score = int(input("Enter your physics score: "))
            if stream == 2:
                bio_score = int(input("Enter your life sciences score: "))
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
                            physics_req = school.requirements["physics"]
                        if stream == 1 or stream == 2:
                            if len(school.requirements) == 3:
                                if maths_score >= maths_req:
                                    for course in school.courses:
                                        st_courses.append(course)
                            elif len(school.requirements) == 4:
                                if (maths_score >= maths_req
                                        and physics_score >= physics_req):
                                    for course in school.courses:
                                        st_courses.append(course)
                            else:
                                bio_req = school.requirements["life sciences"]
                                if stream == 2:
                                    if (maths_score >= maths_req
                                            and
                                            (physics_score >= physics_req
                                                or bio_score >= bio_req )):
                                                for course in school.courses:
                                                    st_courses.append(course)
    display(st_courses, univ_name)

data_base = [ukzn_data,
        up_data,
        wits_data,
        uct_data,
        us_data,
        uj_data]

admission(data_base)
