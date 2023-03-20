from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def questions_to_objects():
    question_bank = []
    for question in question_data:
        question_bank.append(
            Question(
                question["question"],
                question["correct_answer"]
            )
        )
    return question_bank


def start_quiz():
    quiz = QuizBrain(questions_to_objects())
    while quiz.still_has_questions():
        quiz.next_question()
    quiz.final_prompt()

