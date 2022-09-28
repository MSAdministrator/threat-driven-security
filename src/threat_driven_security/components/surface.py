from string import Template

from .core import Core


class Surface(Core):

    QUESTION_DICT = {
        "category": Template("Which category does the $name surface belong to?"),
    }

    def __init__(self, name=None):
        self.name = name
        self.SURFACE_TEMPLATE[name] = self.SURFACE_TEMPLATE["name"]

    def get(self):
        from attrs import fields
        from ..models import ThreatDrivenSecurity

        print(ThreatDrivenSecurity(name=self.name))
        print(fields(ThreatDrivenSecurity).license.metadata["question"])
        question = self.QUESTION_DICT["category"].substitute(name=self.name)
        self.QUESTION_DICT["category"] = question
        resp = self.ask_questions(questions=self.QUESTION_DICT)
        return resp
