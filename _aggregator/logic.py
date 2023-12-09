from universities import universities
from collections import defaultdict
import sys

'''
for uni in universities:
    print("{}. {}".format(uni["id"], uni["name"]))
print()

uni_id = int(input("Enter the university id: "))

for uni in universities:
    if uni.get("id") == uni_id:
        uni_index = universities.index(uni)
        uni_courses = uni.get("courses")

if uni_courses == None:
    sys.exit("Pending..")

print("List of faculties under {} with their respective Departments:".format(universities[uni_index].get("name")))
print("========================================================================================================")

# Assuming uni_courses_ is your dictionary

# Create a defaultdict to store courses by faculty
faculties = defaultdict(list)

# Organize courses by faculty
for course, details in uni_courses.items():
    faculties[details["faculty"]].append(course)

# Print the result
for faculty, courses in faculties.items():
    print(faculty)
    for i, course in enumerate(courses, start=1):
        print("{}. {}".format(i, course))
    print()
'''

for uni in universities:
    print("{}. {}".format(uni["id"], uni["name"]))
print()

university_id = int(input("Enter your university ID: "))
id = university_id - 1
course_of_ch = input("Enter your course of choice: ").upper()
course_aggr = universities[id].get("courses")[f"{course_of_ch}"]["aggregate"]
c_faculty = universities[id].get("courses")[f"{course_of_ch}"]["faculty"]
utme_score = int(input("Enter your utme score: "))
post_utme = float(input("Enter your post utme score: "))

stu_aggr = (utme_score / 8) + ((post_utme/100) * 50)

if stu_aggr >= course_aggr:
    print(
        f"congratulations you met the requirements to study {course_of_ch} at {universities[id].get('name')}")
else:
    print(
        f"Did not meet the requirements to study {course_of_ch} at {universities[id].get('name')}")
print("The required score was {} and your final aggregate score was {}".format(
    course_aggr, stu_aggr))


same_faculty = []
for course, details in universities[id]["courses"].items():
    if c_faculty == details["faculty"]:
        if course_of_ch != course:
            same_faculty.append(details["faculty"])


if len(same_faculty) >= 1:
    print("You're qualified to study the following courses that share the same faculty as {}: ".format(course_of_ch))

    i = 1
    for course, course_details in universities[id]["courses"].items():
        if c_faculty == course_details["faculty"]:
            aggregate = course_details["aggregate"]
            if aggregate:
                v_aggregate = aggregate
            if stu_aggr >= v_aggregate:
                if course != course_of_ch:
                    print("{}. {} ({})".format(
                        i, course, course_details["aggregate"]))
                    i += 1

print("Please note that this was determined by the departmental cut off mark set by {} in the year {}"
      " and may not accurately reflect recent developments.".format(universities[id].get("name", ""),
                                                                    universities[id].get("aggr_year", "")))
