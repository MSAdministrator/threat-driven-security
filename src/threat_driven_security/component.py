from attrs import fields
from pick import pick

from .base import Base


class Component(Base):

    def __prompt_options(self, title, options):
        options, index = pick(options, title)
        return options

    def surface(self, name):
        from .models import Surface

        if not self.surfaces:
            self.surfaces.append(
                Surface(
                    name=name,
                    category=self.session.prompt(fields(Surface).category.metadata["question"].substitute(name=name))
                )
            )
        else:
            exists = False
            for surface in self.surfaces:
                if surface.name == name:
                    self.__logger.info(f"The provided surface name '{name}' already exists.")
                    exists = True
            if not exists:
                self.surfaces.append(
                    Surface(
                        name=name,
                        category=self.session.prompt(fields(Surface).category.metadata["question"].substitute(name=name))
                    )
                )

    def event(self, event_name):
        from .models import Event

        if not self.surfaces:
            self.surface(name=self.session.prompt("Please provide a name for a surface before continuing: "))
        options = []
        for surface in self.surfaces:
            options.append(surface.name)
        title = f"Please select which surface you the event {event_name} to be added to: "
        surface_name = self.__prompt_options(title, options)
        events = []
        for surface in self.surfaces:
            if surface.name == surface_name:
                events.append(
                    Event(
                        name=event_name,
                        metadata=self.session.prompt(fields(Event).metadata.metadata["question"].substitute(name=event_name)),
                        description=self.session.prompt(fields(Event).description.metadata["question"].substitute(name=event_name)),
                        techniques=self.session.prompt(fields(Event).techniques.metadata["question"].substitute(name=event_name))
                    )
                )
                if not surface.events:
                    surface.events = events
                else:
                    surface.events.extend(events)

    def observation(self):
        from .models import Observation

        if not self.surfaces:
            surface_name = self.session.prompt("Please provide a name for a surface before continuing: ")
            self.surface(name=surface_name)
            event_name = self.session.prompt("Please provide an event name before continuing: ")
            self.event(event_name=event_name)
        else:
            surface_name = self.__prompt_options(
                title="Please select which surface you want this observation to be added to: ",
                options=list(self.surfaces.keys())
            )
            event_name = self.session.prompt(
                title="Please select which event you want this observation to be added to: ",
                options=list(self.surfaces[surface_name].keys())
            )
        print(surface_name)
        print(event_name)
        print(self.surfaces)
        for surface in self.surfaces:
            if surface and surface.name == surface_name:
                for event in surface.events:
                    if event.name == event_name:
                        observation = Observation(
                            name=self.session.prompt(fields(Observation).name.metadata["question"].substitute()),
                            sensors=self.session.prompt(fields(Observation).sensors.metadata["question"].substitute())
                        )
                        if not event.observations:
                            event.observations = [observation]
                        else:
                            event.observations.append(observation)
                            
        if self._ask_yes_no_question("Do you want to save? (Y or N) "):
            return self.generate(save_to_file=self.session.prompt("What is the name of this definition? "))
        return self.generate()
