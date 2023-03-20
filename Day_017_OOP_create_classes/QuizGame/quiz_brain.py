class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, actual, expected):
        if actual == expected:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {actual}")
        print(f"Your score is: {self.question_number}/{self.score}\n")

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").capitalize()
        self.check_answer(question.answer, answer)

    def final_prompt(self):
        print(f"You've completed the quiz")
        print(f"Your final score was: {self.question_number}/{self.score}\n")
