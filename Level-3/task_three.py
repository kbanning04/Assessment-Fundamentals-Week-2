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

    def assessment_check(self):
        """ Checks if an assessment is the correct type. """
        assessments = self.assessments
        if not assessments:
            raise TypeError("Assessment is empty.")
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


class Question:
    """ A question in a quiz. """

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    """ A quiz. """

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:
    """ Marks assessments. """

    def __init__(self, quiz: Quiz):
        self._quiz = quiz

    @property
    def quiz(self) -> Quiz:
        """ Getter for the private variable 'quiz'. """
        return self._quiz

    @quiz.setter
    def quiz(self, quiz_questions: Quiz) -> int:
        """ Setter for the private variable 'quiz'."""
        self._quiz = quiz_questions

    def mark(self) -> int:
        """ Returns the score for an assessment as a percentage rounded to 0 decimal places. """
        quiz = self.quiz
        score = 0
        questions = quiz.questions
        if questions == []:
            return 0
        for question in questions:
            if question.chosen_answer == question.correct_answer:
                score += 1
        percentage = (score / len(questions)) * 100
        return percentage

    def generate_assessment(self) -> Assessment:
        """" Generates an Assessment that has been completed. """
        new_quiz = self.quiz
        if new_quiz.type == "multiple-choice":
            assessment_type = MultipleChoiceAssessment
        elif new_quiz.type == "technical":
            assessment_type = TechnicalAssessment
        elif new_quiz.type == "presentation":
            assessment_type = PresentationAssessment
        else:
            raise ValueError(
                "Assessment type must be multiple-choice, technical or presentation.")

        new_assessment = assessment_type(new_quiz.name, self.mark())
        return new_assessment


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
    marking = Marking.mark(quiz)
    print(marking)
    # generate = Marking.generate_assessment(quiz)
    # print(generate)
