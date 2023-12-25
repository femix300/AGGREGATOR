#!/usr/bin/python3
""" This module creates a database of University of Pretorea's faculties,
a list of courses that are found from each faculty,
as well a dictionary of  admission requirements
"""

from engine.varsity import University
from engine.schools import Faculty


eng = Faculty("Engineering", ["BEng (Industrial Engineering)",
    "BEng (Electrical Engineering)",
    "BEng (Electronic Engineering)",
    "BEng (Chemical Engineering)",
    "BEng (Civil Engineering)",
    "BEng (Mechanical Engineering)",
    "BEng (Metallurgical Engineering)",
    "BEng (Mining Engineering)",
    "BEng (Computer Engineering)"],
    {"aps": 35, "maths": 70, "physics": 70, "english": 60}
    )

built_env = Faculty("Built Environment",
        ["BSc (Construction Management)",
            "BSc (Real Estate)",
            "BSc (Quantity Surveying"],
        {
            "aps": 30,
            "maths": 60,
            "physics": 50,
            "english":60
            }
        )

info_tech = Faculty("Information Technology",
        ["BSc (Computer Science)",
            "BSc (Information and Knolwedge Systems)",
            "BCom (Informatics)"],
        {"aps": 30, "english": 60, "maths": 60}
        )

human = Faculty("Humanities",
        ["BSocSc (Industrial Sociology and Labour studies)",
            "B Soc Sc Geography & Environmental Management",
            "BSocSc (Philosophy, Politics and Economics",
            "BA (Languages)",
            "BA (Fine Arts)",
            "BA (Audilogy)",
            "BA (Information Design)",
            "Bachelor of Drama (BDram)",
            "BSocSc (Heritage and Cultural Tourism",
            "BA (Law)",
            "Bachelor of Social Work (BSW)",
            "Bachelor of Music (BMus)",
            "BEd (Bachelor of Education)"
            ],
        {"aps": 30, "english": 60}
        )

agric_sc = Faculty(
        "Natural and Agricultural Sciences",
        ["BSc (Mathematics)",
            "BSc (Applied Mathematics)",
            "BSc (Mathematical Statistics)",
            "BSc (Actuarial and Financial Mathematics)",
            "BSc (Biological Science)",
            "BSc (Biochemistry)",
            "Bsc (Biotechnology)",
            "Bsc (Ecology)",
            "BSc (Zoology)",
            "BSc (Genetics)",
            "BSc (Physiology)",
            "BSc (Medical Sciences)",
            "BSc (Microbiology)",
            "BSc (Plant Science)",
            "BSc (Food Science)",
            "BSc (Nutrition)",
            "BScAgric (Agricultural Economics and Agribusiness Management)",
            "BScAgric (Animal Science)",
            "BScAgric (Plant Pathology)",
            "BScAgric (Applied Plant and Soil Sciences)",
            "BSc (Physics)",
            "BSc (Geography and Environmental Science)",
            "BSc (Geoinformatics)",
            "BSc (Geology)"],
        {
            "aps": 32,
            "english": 60,
            "maths": 60,
            "physics": 60
        }
        )

health_care = Faculty("Healthcare Sciences",
        ["Bachelor of Occupational Therapy (BOT)",
            "B Physiotherapy (BPhysio)",
            "B Radiography (Diagnostics) (BRad Diagnostics)",
            "Bachelor of Nursing (BNurs)"],
        {
            "aps": 30,
            "maths": 50,
            "physics": 50,
            "life sciences": 50,
            "english": 50
        }
        )

dentist = Faculty("Dentistry",
        ["Bachelor of Dental Surgery (BChD)"],
        {"aps": 35, "english": 60, "maths": 70, "physics": 60}
        )

med = Faculty("Medicine",
        ["Bachelor of Medicine and Surgery (MBChB)",
            "Bachelor of Sports Science (BSportSci)",
            "Bachelor of Clinical Medical Practice (BCMP)"],
        {
            "aps": 30,
            "english": 50,
            "physics": 50,
            "maths": 50,
            "life sciences": 50
        }
        )


law = Faculty("Law Studies",
        ["LLB"],
        {"aps": 35, "english": 70}
        )

man = Faculty("Economic and Management Sciences",
        ["BCom (Accounting Sciences)",
            "BCom (Investment Management)",
            "BCom (Financial Sciences)",
            "BCom (Econometrics)",
            "BCom (Economics)",
            "BCom (Law)",
            "BCom (Statistics and Data Science)",
            "BCom (Informatics)",
            "BCom (Agribusiness Management)",
            "BCom",
            "BCom (Business Management)",
            "BCom (Supply Chain Management)",
            "BCom (Marketing Management)",
            "BCom (Human Resource Management)"],
        {"aps": 30, "english": 60, "maths": 60}
        )

up_schools = [eng, built_env, info_tech, human,
        agric_sc, health_care, dentist, med, law, man]

up_data = University("up", up_schools)
