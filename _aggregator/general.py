import sys
from merit import University
from universities import universities
import pyinputplus as pyip
from ui import Ui
from oau import Oau
from unilag import Unilag
from unn import Unn

def start(uni_instance):
    uni_instance.about_uni()
    index = uni_instance.get_uni_index()
    print()
    courses = list(uni_instance.universities[index]["courses"].keys())

    course_of_ch = pyip.inputMenu(
        courses,
        numbered=True,
        prompt="Please enter one of the following (course name or serial number): \n",
    )
    print("\nYou selected {}\n".format(course_of_ch))

    uni_instance.print_grades_info()

    return index, course_of_ch


def evaluate_and_recommend(uni, universities, index, course_of_ch):
    course_aggr = universities[index].get(
        "courses")[f"{course_of_ch}"]["aggregate"]
    stu_aggr = uni.calculate_aggregate()
    stu_aggr = round(stu_aggr, 2)

    if stu_aggr >= course_aggr:
        print(
            "Congratulations! You met the requirements to "
            "study {} at {}.".format(
                course_of_ch, universities[index].get("name")
            )
        )
    else:
        print(
            "You did not meet the requirements to study {} at {}.".format(
                course_of_ch, universities[index].get("name")
            )
        )

    print(
        "The required score was {} and your final aggregate "
        "score was {}.".format(course_aggr, stu_aggr)
    )

    course_faculty = universities[index].get(
        "courses")[f"{course_of_ch}"]["faculty"]

    same_faculty = []
    for course, details in universities[index]["courses"].items():
        if course_faculty == details["faculty"]:
            if course_of_ch != course:
                same_faculty.append(details["faculty"])

    if len(same_faculty) >= 1:
        qualified_to_study = {}
        for course, course_details in universities[index]["courses"].items():
            if course_faculty == course_details["faculty"]:
                aggregate = course_details["aggregate"]
                if aggregate:
                    if stu_aggr >= aggregate:
                        if course != course_of_ch:
                            qualified_to_study[course] = aggregate
    if qualified_to_study:
        print(
            "You're qualified to study the following courses "
            "that share the same faculty as {}: ".format(course_of_ch)
        )
        for i, (course, aggregate) in enumerate(qualified_to_study.items()):
            print("{}. {} ({})".format(i+1, course, aggregate))

    print(
        "Please note that this was determined by the departmental "
        "cut off mark set by {} in the year {} and may not accurately "
        "reflect recent developments.".format(
            universities[index].get("name", ""),
            universities[index].get("aggr_year", ""),
        )
    )


def determine_post_utme_score(uni, course_of_ch, universities, index):
    course_aggr = universities[index].get(
        "courses")[f"{course_of_ch}"]["aggregate"]
    required_score = uni.calculate_required_post_utme_score(course_aggr)

    if required_score is None:
        print("Currently Unavailable")
        return

    pd_score = required_score / 0.4

    if required_score < 25:
        required_score = 25
        if pd_score < 60:
            pd_score = 60

    required_score = int(round(required_score))
    pd_score = round(pd_score, 1)

    if required_score <= 40:
        print(
            "Based on your O-level and UTME score, "
            "you are required to score at least {} "
            "in your post utme exams in order to be "
            "considered for admission.".format(required_score)
        )
        print(
            "If you're coming through predegree then you'll need "
            "to score at least {} out of 100 marks.".format(pd_score)
        )
    else:
        print(
            "With your previous grades, in order to be considered "
            "for admission to study {}, you'll have to score at least {} "
            "out of {} marks which is simply impossible.".format(
                course_of_ch, required_score, 40
            )
        )


def get_uni_id(universities):
    university_names = [uni["name"] for uni in universities]
    uni_name = pyip.inputMenu(
        university_names,
        numbered=True,
        prompt="Please enter one of the following "
        "(serial number or university name)\n")

    print("\nYou selected {}\n".format(uni_name))

    for uni in universities:
        if uni["name"] == uni_name:
            # 1 was added to solve indexing issues
            uni_id = (universities.index(uni) + 1)

    # I substracted 1 from the id here to prevent errors, but 1 will be substracted later
    if not universities[uni_id - 1]["courses"]:
        return None
    return uni_id

def start(uni_instance):
    uni_instance.about_uni()
    index = uni_instance.get_uni_index()
    print()
    courses = list(uni_instance.universities[index]["courses"].keys())

    course_of_ch = pyip.inputMenu(
        courses,
        numbered=True,
        prompt="Please enter one of the following (course name or serial number): \n",
    )
    print("\nYou selected {}\n".format(course_of_ch))

    uni_instance.print_grades_info()

    return index, course_of_ch

def entry_point(universities):
    uni_id = get_uni_id(universities)

    uni_classes = {
        "1": Ui,
        "2": Unilag,
        "3": Unn,
        "4": Oau,
    }

    uni_id_str = str(uni_id)
    _class = uni_classes[uni_id_str]

    if uni_id:
        _class_instance = _class(uni_id)
        index, course_of_ch = start(_class_instance)

        options = {
            "Calculate Aggregate": lambda: evaluate_and_recommend(_class_instance, universities, index, course_of_ch),
            "Determine required POST UTME score": lambda: determine_post_utme_score(_class_instance, course_of_ch, universities, index),
            "About University": _class_instance.about_uni,
            "Display University Name": _class_instance.display_name,
            "Display list of courses": _class_instance.list_courses,
            "Display Faculties and Courses": _class_instance.display_faculties_and_courses,
            "Display all Universities": _class_instance.display_universities,
            "Exit": _class_instance.exit
        }

        choices = list(options.keys())

        choice = pyip.inputMenu(
            choices,
            numbered=True,
        )

        selected_option = options[choice]

        selected_option()
        
    else:
        print("\nComing Soon!")



entry_point(universities)