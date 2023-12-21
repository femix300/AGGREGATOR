#!/usr/bin/python3
"""
This module creates a database of ukzn faculties,
a list of courses that are found from each faculty
as well a dictionary of  admission requirements
"""
from engine.varsity import University
from engine.schools import Faculty


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
        ["B Soc Sc General Studies",
            "B Soc Sc Geography & Environmental Management",
            "B A Philosophy, Politics and Law",
            "B A General Studies",
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
            "physics": 50
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
