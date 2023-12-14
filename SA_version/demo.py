#!/usr/bin/python3

from varsity import University
from schools import Faculty


eng = Faculty("Engineering", ["B Sc Eng: Computer",
    "B Sc Eng: Electrical",
    "B Sc Eng: Electronic",
    "B Sc: Land Surveying",
    "B Sc: Property Development",
    "B Sc Eng: Agricultural",
    "B Sc Eng: Chemical",
    "B Sc Eng: Civil",
    "B Sc Eng: Mechanical"],
    {"aps": 35,
        "maths": 65,
        "physics": 65,
        "english": 50}
    )

human = Faculty("Humanities",
        ["B Soc Sc (General Studies)",
            "B Soc Sc Geography & Environmental Management",
            "B A Philosophy, Politics and Law",
            "B A (General Studies)",
            "B A Music",
            "B A Music & Drama Performance",
            "B A Cultural & Heritage Tourism",
            "B Soc Sc Housing",
            "B Architectural Studies",
            "B Social Work "
            ],
        {"aps": 29, "english": 50}
        )

agric_sc = Faculty(
        "Agriculture and Science",
        ["B Sc Environmental Science",
            "B Sc Agric: Agribusiness",
            "B Sc Stream M (Mathematics)",
            "B Sc Biological Science",
            "B Sc Computer Science and Information Technology",
            "B Sc Environmental Earth Science",
            "B Agricultural Management",
            "B Sc Agric",
            "B Sc Agric: Animal and Poultry Science",
            "B Sc Dietetics",
            "B Sc Industrial and Applied Biotechnology",
            "B Sc Agric: Plant Pathology",
            "B Sc Agric: Soil Science",
            "B Sc Chemistry and Chemical Technology",
            "B Sc Applied Chemistry",
            "B Sc Geological Science",
            "B Sc Marine Biology"],
        {
            "aps": 30,
            "english": 50,
            "maths": 60,
            "physics": 50,
            "life sciences": 50,
            "agriculture": 50
        }
        )

health = Faculty("Health Sciences",
        ["B Dental Therapy",
            "B Occupational Therapy",
            "B Optometry",
            "B Pharmacy",
            "B Physiotherapy",
            "B Medical Science: Anatomy",
            "B Medical Science: Physiology",
            "B Sport Science"],
        {
            "aps": 33,
            "maths": 50,
            "physics": 50,
            "life sciences": 50,
            "english": 50
        }
        )

man = Faculty("Law and Management Studies",
        ["B Business Administration",
            "B Com",
            "B Business Science",
            "B Com Accounting",
            "B Admin"
            ],
        {"aps": 32, "english": 50, "maths": 60}
        )
law = Faculty("Law Studies",
        ["B Laws", "B Criminiology"],
        {"aps": 32, "english": 60}
        )

schools = [eng, human, agric_sc, health, man, law]

ukzn_data = University("ukzn", schools)

univ_name = str(input("Enter your university name: "))
aps_score = int(input("Enter your aps score: "))

st_courses = []
if aps_score < 29:
    print("Unfortunately you don't qualify for any course")
else:
    english_score = int(input("Enter your english score: "))
    if univ_name == ukzn_data.name:
        for i in range(6):
            if len(schools[i].requirements) == 2:
                if (aps_score >= schools[i].requirements["aps"]
                and english_score >= schools[i].requirements["english"]):
                    for course in schools[i].courses:
                        st_courses.append(course)

if len(st_courses) > 0:
    print("This is the list of course you qualify for in {}:".format(univ_name))
    st_courses.sort()
    for course in st_courses:
        print(course)
