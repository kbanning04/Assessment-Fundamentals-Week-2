from datetime import date


class Trainee:
    """ A Trainee at Tau Labs. """

    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self) -> int:
        """ Calculates how old a trainee is. """
        date_of_birth = self.date_of_birth
        current_date = date.today()
        delta = (current_date - date_of_birth).days // 365.25
        age = round(delta)
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """ Adds an assessment to the trainee's list of assessments. """
        assessments = self.assessments
        assessments.append(assessment)
        return assessments

    def get_assessment(self, name: str) -> Assessment | None:
        """ Returns a specific assessment that has the name given. """
        assessments = self.assessments
        for test in assessments:
            if name == test.name:
                return test
        return None


class Assessment:
    """ An assessment that a trainee has completed. """

    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type
        self.type_check()
        self.score = score
        self.score_check()

    def type_check(self):
        """ Checks if a assessment is the right type: multiple-choice, technical or presentation."""
        type = self.type
        if type not in {"multiple-choice", "technical", "presentation"}:
            raise ValueError(
                "Assessment should be multiple-choice, technical or presentation only.")

    def score_check(self):
        """ Checks if the score is between 0 and 100. """
        score = self.score
        if score > 100:
            raise ValueError("Score must be 100 or less")
        elif score < 0:
            raise ValueError("Score must be 0 or more.")


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
