from .base import Base


class Security(Base):

    @property
    def add(self):
        from .component import Component

        return Component()

    @property
    def get(self):
        from .load import Load

        return Load().definitions()
