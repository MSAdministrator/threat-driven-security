from glob import glob

import yaml

from .base import Base
from .models import ThreatDrivenSecurity


class Load(Base):

    def _definition(self, path):
        with open(path) as f:
            return ThreatDrivenSecurity(**yaml.safe_load(f))

    def definitions(self):
        return_list = []
        for item in glob(f"definitions/*.yml"):
            return_list.append({f"{item.split('definitions/')[-1]}": self._definition(path=item)})
        return return_list
