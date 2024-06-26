from pydantic import BaseModel

class AmericanQuestionObject(BaseModel):
    id: int
    question: str
    answers: list[str]
    right_answer: int
    assistant_id: str
    thread_id: str

class AmericanQuestionObjectWithFileName(AmericanQuestionObject):
    file_name: str
