from merit import University
import pyinputplus as pyip


class Unilag(University):
    uni_name = "University of Lagos (UNILAG)"

    unilag_olevel = {
        "A1": {"value": 4.0, "index": 1},
        "B2": {"value": 3.6, "index": 2},
        "B3": {"value": 3.2, "index": 3},
        "C4": {"value": 2.8, "index": 4},
        "C5": {"value": 2.4, "index": 5},
        "C6": {"value": 2.0, "index": 6},
    }

    @classmethod
    def print_grades_info(cls):
        print(
            "In order to be considered for admission "
            "into {} you must have at least 5 credits "
            "in 5 relevant subjects.\n".format(cls.uni_name)
        )

    @classmethod
    def calculate_olevel(cls):
        total = 0
        for i in range(5):
            grade = pyip.inputMenu(
                list(Unilag.unilag_olevel.keys()),
                numbered=True,
                prompt="Enter grade for subject({}): \n".format(i + 1),
            ).upper()
            total += cls.unilag_olevel[grade]["value"]
        return round(total, 3)

    @classmethod
    def calculate_aggregate(cls):
        olevel = Unilag.calculate_olevel()
        utme = pyip.inputInt("Enter UTME score: ", min=200, max=400)
        post_utme = pyip.inputInt("Enter POST UTME score: ", min=0, max=30)
        aggregate = olevel + (utme * 0.125) + post_utme
        return round(aggregate, 4)

    @classmethod
    def calculate_required_post_utme_score(cls, course_aggregate):
        olevel = Unilag.calculate_olevel()
        utme = pyip.inputInt("Enter UTME score: ", min=180, max=400)
        post_utme = course_aggregate - ((utme * 0.125) + olevel)
        return post_utme
