
from prompt_toolkit import prompt

from ..base import Base


class Core(Base):
    SURFACE_TEMPLATE = {
        "name": {
            "category": None,
            "events": [
                {
                    "name": None,
                    "metadata": [],
                    "description": None,
                    "techniques": [],
                    "observations": [
                        {
                            "name": None,
                            "sensors": [],
                        }
                    ],
                }
            ],
        }
    }

    def ask_questions(self, questions: dict) -> dict:
        return_dict = {}
        if isinstance(questions, dict):
            for key, question in questions.items():   
                return_dict[key] = prompt(question)
        return return_dict
