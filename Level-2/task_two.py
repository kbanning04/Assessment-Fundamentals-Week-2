from datetime import date


class Trainee:
    """ A Trainee at Tau Labs. """

    def __init__(self, name: str, email: str, date_of_birth: date):
        """ Runs when a new Trainee instance is created. """
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
        self.assessment_check()
        assessments.append(assessment)
        return assessments

    def get_assessment(self, name: str) -> Assessment | None:
        """ Returns a specific assessment that has the name given. """
        assessments = self.assessments
        for test in assessments:
            if name == test.name:
                return test
        return None

    def __str__(self) -> str:
        """ Represents the trainee as a string. """
        return f"Trainee Name: {self.name}, Trainee Email: {self.email}, Trainee DOB: {self.date_of_birth}"

    def assessment_check(self):
        """ Checks if an assessment is the correct type. """
        assessments = self.assessments
        # When this code runs, a different test fails.
        # if assessments == []:
        #     raise TypeError("Assessment is empty.")
        for test in assessments:
            if not isinstance(test, Assessment):
                raise TypeError("Assessment Error is not an Assessment.")

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """ Lists all the assessments of the same type that was given. """
        assessments = self.assessments
        correct_type_assessments = []
        if type == "multiple-choice":
            assessment_type = MultipleChoiceAssessment
        elif type == "technical":
            assessment_type = TechnicalAssessment
        elif type == "presentation":
            assessment_type = PresentationAssessment
        else:
            raise TypeError(
                "An Assessment can only be multiple-choice, technical or presentation.")
        for test in assessments:
            if isinstance(test, assessment_type):
                correct_type_assessments.append(test)
        return correct_type_assessments


class Assessment:
    """ An assessment that a trainee has completed. """

    def __init__(self, name: str, score: float):
        """ Runs when a new Assessment instance is created. """
        self.name = name
        self.score = score
        self.score_check()

    def score_check(self):
        """ Checks if the score is between 0 and 100. """
        score = self.score
        if score > 100:
            raise ValueError("Score must be 100 or less")
        if score < 0:
            raise ValueError("Score must be 0 or more.")

    def __str__(self) -> str:
        """ Represents an assessment that a trainee has completed. """
        return f"Assessment name: {self.name}, Assessment score: {self.score}"


class MultipleChoiceAssessment(Assessment):
    """ A Multiple Choice style Assessment. """

    def calculate_score(self):
        """ Calculates the score for a multiple choice assessment. """
        score = self.score
        weighting = 0.7
        return score * weighting


class TechnicalAssessment(Assessment):
    """ A Technical style Assessment. """

    def calculate_score(self):
        """ Calculates the score for a technical assessment. """
        score = self.score
        weighting = 1
        return score * weighting


class PresentationAssessment(Assessment):
    """ A Presentation style Assessment. """

    def calculate_score(self):
        """ Calculates the score for a presentation assessment. """
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
