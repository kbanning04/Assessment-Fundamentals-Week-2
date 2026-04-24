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
    """ An assessment that a trainee should complete. """

    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score
        self.score_check()

    def score_check(self):
        """ Checks if the score is between 0 and 100. """
        score = self.score
        if score > 100:
            raise ValueError("Score must be 100 or less")
        elif score < 0:
            raise ValueError("Score must be 0 or more.")

    def calculate_score(self):
        pass


class MultipleChoiceAssessment(Assessment):
    def __init__(self, name, score):
        super().__init__(name, score)

    def calculate_score(self):
        score = self.score
        weighting = 0.7
        return score * weighting


class TechnicalAssessment(Assessment):
    def __init__(self, name, score):
        super().__init__(name, score)

    def calculate_score(self):
        score = self.score
        weighting = 1
        return score * weighting


class PresentationAssessment(Assessment):
    def __init__(self, name, score):
        super().__init__(name, score)

    def calculate_score(self):
        score = self.score
        weighting = 0.6
        return score * weighting


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
