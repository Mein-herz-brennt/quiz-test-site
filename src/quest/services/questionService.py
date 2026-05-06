from fastapi import Depends
from src.quest.repositories.questionRepository import QuestionRepository
from src.models.questions import Question


class QuestionService:
    def __init__(
            self,
            question_repository: QuestionRepository = Depends(QuestionRepository),
    ) -> None:
        self.example_repository = question_repository

    def _find_example_by_id(self, question_id: int):
        example = self.example_repository.get_question_by_id(question_id)
        if example is None:
            # raise ("Example", example_id)
            raise Exception
        return example
    #
    # async def get_example(self) -> Example:
    #     # Implement logic to get default example or list of examples
    #     example = await self.example_repository.get_example()
    #     if example is None:
    #         raise NotFoundError("Example")
    #     return Example(
    #         name=example.name,
    #         id=example.id,
    #     )
    #
    # def get_list(self):
    #
    # async def create_example(self, example: ExampleCreate) -> Example:
    #     existing_example = await self.example_repository.get_example_by_name(
    #         example.name
    #     )
    #     if existing_example:
    #         raise ConflictError(message="Name already exists", field="name")
    #     created_example = await self.example_repository.create(
    #         ExampleModel(
    #             name=example.name,
    #         )
    #     )
    #     return Example(name=created_example.name, id=created_example.id)
    #
    # async def update_example(self, example_id: int, example: ExampleUpdate) -> Example:
    #     existing_example = await self._find_example_by_id(example_id)
    #     if example.name is not None:
    #         existing_example.name = example.name
    #     updated_example = await self.example_repository.update(existing_example)
    #     return Example(name=updated_example.name, id=updated_example.id)
    #
    # async def delete_example(self, example_id: int):
    #     example = await self._find_example_by_id(example_id)
    #     await self.example_repository.delete(example)
    #     return {"message": "Example deleted successfully"}
