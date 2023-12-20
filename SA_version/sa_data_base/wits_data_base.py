#!/usr/bin/python3
"""
This module creates a database of University of Wit's faculties,
with a list of courses each faculty offers,
as well a dictionary of  admission requirements
"""
from SA_version.varsity import University
from SA_version.schools import Faculty


eng = Faculty("Engineering",
        ["BSc Eng (Industrial Engineering)",
            "BSc Eng (Electrical Engineering)",
            "BSc Eng (Electronic Engineering)",
            "BSc Eng (Chemical Engineering)",
            "BSc Eng (Civil Engineering)",
            "BSc Eng (Mechanical Engineering)",
            "BSc Eng (Metallurgical and Materials Engineering)",
            "BSc Eng (Mining Engineering)",
            "BEngSc (Biomedical Engineering)",
            "BSc Eng (Aeronautical Engineering)",
            "BEngSc (Digital Arts)",
            "BSc Eng (Information Engineering)"],
        {"aps": 36, "maths": 70, "physics": 70, "english": 60}
    )

built_env = Faculty("Built Environment",
        ["BSc (Property Studies)",
            "BSc (Urban and Regional Planning)",
            "BSc (Construction Studies)",
            "BAS (Architectural Studies)",
            "BSc (Quantity Surveying)"],
        {"aps": 30, "maths": 60, "english":60}
        )

info_tech = Faculty("Information Technology",
        ["BSc (Computer Science)",
            "BSc (Information and Knolwedge Systems)",
            "BCom (Informatics)"],
        {"aps": 32, "english": 60, "maths": 70}
        )

human = Faculty("Humanities",
        ["BSocSc(Industrial Sociology and Labour studies)",
            "BSocSc(Geography & Environmental Management)",
            "BSocSc(Philosophy, Politics and Economics)",
            "BA(languages)",
            "BA(Fine Arts)",
            "BA(Audilogy)",
            "BA(Information Design)",
            "Bachelor of Drama(BDram)",
            "BSocSc(Heritage and Cultural Tourism)",
            "BA(Law)",
            "Bachelor of Social Work(BSW)",
            "Bachelor of  Music(BMus)",
            "BEd (Bachelor of Education)"
            ],
        {"aps": 30, "english": 60}
        )

science = Faculty(
        "Science",
        ["BSc (Mathematics)",
            "BSc (Applied Mathematics)",
            "BSc (Mathematical Science)",
            "BSc (Actuarial Science)",
            "BSc (Biological Science)",
            "BSc (Biochemistry)",
            "Bsc (Biotechnology)",
            "Bsc (Applied Chemistry)",
            "BSc (Material Sciences)",
            "BSc (Microbiology and Biotechnology)",
            "BSc (Astronomy and Astrophysics)",
            "BSc (Applied Bioinformatics)",
            "BScAgric (Computational and Applied Mathematics)",
            "BSc (Physics)",
            "BSc (Geography)",
            "BSc (Geological science)",
            "BSc (Geospatial Science)"],
        {"aps": 32, "english": 60, "maths": 60, "physics": 60}
        )

health_care = Faculty("Health Sciences",
        ["BHSc (Biomedical Sciences)",
            "BCMP (Clinical Medical Practice)",
            "BDS (Dental Science)",
            "BHSc (Health Systems Sciences)",
            "BPharm (Phamarcy)",
            "BSc (Physiotherapy)"],
        {
            "aps": 30,
            "maths": 60,
            "physics": 60,
            "life sciences": 60,
            "english": 60
        }
        )

law = Faculty("Law Studies",
        ["LLB"],
        {"aps": 35, "english": 70}
        )

com = Faculty("Commerce",
        ["BAccSc (Accounting Sciences)",
            "BCom (Accounting)",
            "BCom (Applied Development Economics)",
            "BCom (Bachelor of Commerce) (General)",
            "BCom (Economics)",
            "BEconSc (Economic Science)",
            "BCom (Insurance and Risk Management)",
            "BCom (Finance)",
            "BCom (Information Systems)",
            "BCom (Human Resource Management)",
            "BCom (With Law)",
            "BCom (Management)",
            "BCom (Marketing)"],
        {"aps": 30, "english": 60, "maths": 60}
        )

wits_schools = [eng, built_env, info_tech, human,
        science, health_care, law, com]

wits_data = University("wits", wits_schools)
