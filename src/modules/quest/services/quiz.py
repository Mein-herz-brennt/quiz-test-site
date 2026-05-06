from fastapi import Depends
from src.modules.quest.repositories import QuizRepository
from src.modules.quest.models import Quiz, QuizStatus, Question, QuestionStatus, Answer
from src.modules.quest.schemas.quiz import QuizCreate


class QuizService:
    def __init__(
            self,
            quiz_repository: QuizRepository = Depends(QuizRepository),
    ) -> None:
        self.quiz_repository = quiz_repository

    def create_quiz(self, quiz_data: QuizCreate, user_id: int) -> Quiz:
        questions = []
        for q_data in quiz_data.questions:
            answers = [
                Answer(text=a_data.text, is_correct=a_data.is_correct)
                for a_data in q_data.answers
            ]
            question = Question(
                title=q_data.title,
                description=q_data.description,
                status=QuestionStatus.active,
                answers=answers
            )
            questions.append(question)

        quiz = Quiz(
            title=quiz_data.title,
            created_by=user_id,
            status=QuizStatus.draft,
            questions=questions
        )

        return self.quiz_repository.create(quiz)

    def get_quiz_by_id(self, quiz_id: int) -> Quiz | None:
        return self.quiz_repository.get_by_id(quiz_id)

    def get_quizzes_by_user(self, user_id: int):
        return self.quiz_repository.get_by_user(user_id)

    def update_quiz_status(self, quiz_id: int, status: QuizStatus) -> Quiz | None:
        quiz = self.quiz_repository.get_by_id(quiz_id)
        if quiz:
            quiz.status = status
            self.quiz_repository.update(quiz)
        return quiz
