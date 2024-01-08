class QuizBrain:
    def __init__(self, list_of_questions):
        self.question_number = 0
        self.score = 0
        self.list_of_questions = list_of_questions

    def next_question(self):
        question = self.list_of_questions[self.question_number]
        question_text = question.text
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {question_text} (True/False)?: ").lower()
        self.check_answer(user_answer=user_answer, correct_answer=question.answer)

    def still_has_question(self):
        return self.question_number < len(self.list_of_questions)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")
