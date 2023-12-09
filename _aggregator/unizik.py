from merit import University
from universities import universities
import pyinputplus as pyip

class Unizik(University):

    uni_name = "Nnamdi Azikiwe University (UNIZIK)"

    @classmethod
    def print_grades_info(cls):
        print(
            "In order to be considered for admission "
            "into {} you must have at least 5 credits "
            "in 5 relevant subjects.\n".format(cls.uni_name)
        )

    @classmethod
    def calculate_aggregate(cls):
        utme = pyip.inputInt("Enter UTME score: ", min=200, max=400)
        post_utme = pyip.inputInt("Enter POST UTME score: ", min=0, max=100)
        aggregate = ((utme) + (post_utme * 4) / 2)
        return round(aggregate, 4)

    @classmethod
    def calculate_required_post_utme_score(cls, course_aggregate):
        utme = pyip.inputInt("Enter UTME score: ", min=180, max=400)
        post_utme = ((2 * course_aggregate) - (utme)) / 4
        return post_utme
