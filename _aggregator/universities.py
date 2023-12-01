# Creates a Python dictionary that stores information about universities
from about_universities import about_uni

universities = [
    {
        "id": 1,
        "name": "University of Ibadan (UI)",
        "about": about_uni[0]['description'],
        "courses": [
        {
            "BIOCHEMISTRY": {
            "id": 1,
            "faculty": "COLLEGE OF MEDICINE",
            "aggregate": 60.375,
        },
            "DENTISTRY": {
                "id": 2,
                "faculty": "COLLEGE OF MEDICINE",
                "aggregate": 71.875,
            },
            "ENVIRONMENTAL HEALTH SCIENCE": {
                "id": 3,
                "faculty": "COLLEGE OF MEDICINE",
                "aggregate": 55.625,
            },
            "HUMAN NUTRITION AND DIETETICS": {
                "id": 4,
                "faculty": "COLLEGE OF MEDICINE",
                "aggregate": 57.75,
            },
            "MEDICAL LABORATORY SCIENCE": {
                "id": 5,
                "faculty": "COLLEGE OF MEDICINE",
                "aggregate": 68.25,
            },
            "MEDICINE AND SURGERY": {
                "id": 6,
                "faculty": "COLLEGE OF MEDICINE",
                "aggregate": 76.25,
            },
            "NURSING SCIENCE": {
                "id": 7,
                "faculty": "COLLEGE OF MEDICINE",
                "aggregate": 68.375,
            },
            "PHYSIOLOGY": {
                "id": 8,
                "faculty": "COLLEGE OF MEDICINE",
                "aggregate": 57.5,
            },
            "PHYSIOTHERAPY": {
                "id": 9,
                "faculty": "COLLEGE OF MEDICINE",
                "aggregate": 66.5,
            },
            "LAW": {
                    "aggregate": 73.7,
                    "faculty": "law",
                }
            }
        ]
        },
        {
            "id": 2,
            "name": "University of Lagos (UNILAG)",
            "about": about_uni[1]['description']
        },
        {
            "id": 3,
            "name": "University of Nigeria, Nsukka (UNN)",
            "about": about_uni[2]['description']
        },
        {
            "id": 4,
            "name": "Obafemi Awolowo University (OAU)",
            "about": about_uni[3]['description']
        },
        {
            "id": 5,
            "name": "Ahmadu Bello University (ABU)",
            "about": about_uni[4]['description']
        },
        {
            "id": 6,
            "name": "University of Ilorin (UNILORIN)",
            "about": about_uni[5]['description']
        },
        {
            "id": 7,
            "name": "Federal University of Technology, Akure (FUTA)",
            "about": about_uni[6]['description']
        },
        {
            "id": 8,
            "name": "Nnamdi Azikiwe University, Awka (UNIZIK)",
            "about": about_uni[7]['description']
        },
        {
            "id": 9,
            "name": "University of Benin (UNIBEN)",
            "about": about_uni[8]['description']
        },
        {
            "id": 10,
            "name": "Federal University Oye Ekiti (FUOYE)",
            "about": about_uni[9]['description']
        }
]

for uni in universities:
    print("{}. {}".format(uni["id"], uni["name"]))
print()

university_id = int(input("Enter your university ID: "))
course_of_ch = input("Enter your course of choice: ").upper()
course_aggr = universities[0].get("courses")[0][f"{course_of_ch}"]["aggregate"]
c_faculty = universities[0].get("courses")[0][f"{course_of_ch}"]["faculty"]
utme_score = int(input("Enter your utme score: "))
post_utme = int(input("Enter your post utme score: "))

stu_aggr = (utme_score / 8) + ((post_utme/100) * 50)

if stu_aggr >= course_aggr:
    print(f"congratulations you met the requirements to study {course_of_ch} at {universities[university_id - 1].get('name')}")
else: 
    print(f"Did not meet the requirements to study {course_of_ch} at {universities[university_id - 1].get('name')}")
print("The required score was {} and your final aggregate score was {}".format(course_aggr, stu_aggr))

if c_faculty != "law":
    print("You're qualified to study: ")


i = 1
for course, course_details in universities[0]["courses"][0].items():
    if c_faculty == course_details["faculty"]:
        if stu_aggr >= course_details["aggregate"]:
            if course != course_of_ch:
                print("{}. {} ({})".format(i, course, course_details["aggregate"]))
                i += 1

