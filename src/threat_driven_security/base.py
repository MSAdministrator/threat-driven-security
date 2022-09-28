import os

from attrs import asdict, fields
from prompt_toolkit import PromptSession
import yaml

from .utils.logger import LoggingBase


class Base(metaclass=LoggingBase):

    session = PromptSession()
    definition = None
    surfaces = []
    observations = []

    def _ask_yes_no_question(self, message):
        save = self.session.prompt(message=message)
        if save.upper().startswith('Y'):
            return True
        elif save.upper().startswith('N'):
            return False
        else:
            return self._ask_yes_no_question(message=message)

    def generate(self, save_to_file=None):
        from .models import ThreatDrivenSecurity

        data = ThreatDrivenSecurity(
            name="some name",
            surfaces=self.surfaces,
            statement=self.session.prompt(fields(ThreatDrivenSecurity).statement.metadata["question"].substitute())
        )
        if save_to_file:
            save_to_file = save_to_file.lower().strip()
            for item in ["&", "-", "!", "?", "%", " "]:
                save_to_file = save_to_file.replace(item, "_")
            save_to_file = f"{save_to_file}_{data.version}"
            if not os.path.exists("definitions"):
                os.makedirs("definitions")
            with open(f"definitions/{save_to_file}.yml", "w+") as f:
                yaml.dump(asdict(data), f)
        return asdict(data)
