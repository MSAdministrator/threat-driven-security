from string import Template
from datetime import date

from attrs import define, field
from pydantic import HttpUrl
from typing import AnyStr, List

from .types.semversion import SemVersion


@define
class Metadata:
    created_by: AnyStr = field(factory=str)
    modified_by: AnyStr = field(factory=str)
    created_date: date = field(factory=date.today)
    modified_date: date = field(factory=date.today)


@define
class Observation:
    name: AnyStr = field(factory=str, metadata={"question": Template("Please provide a unique name for this observation: ")})
    sensors: List = field(factory=list, metadata={"question": Template("Provide a list of sensors (logs, etc.) for this observation: ")})

    def __attrs_post_init__(self):
        if self.sensors:
            try:
                self.sensors = [x.strip() for x in self.sensors.split(',')]
            except TypeError as te:
                # the provided value is not a list so we will just force it to a list
                self.sensors = [self.sensors]


@define
class Event:
    name: AnyStr = field(factory=str)
    metadata: List = field(factory=list, metadata={"question": Template("What metadata (attributes) are required for the $name event? ")})
    description: AnyStr = field(factory=str, metadata={"question": Template("Provided a description of the $name event: ")})
    techniques: List = field(factory=list, metadata={"question": Template("Please provide a list of ATT&CK techniques for the $name event: ")})
    observations: List[Observation] = field(factory=list)

    def __attrs_post_init__(self):
        if self.metadata:
            try:
                self.metadata = [x.strip() for x in self.metadata.split(',')]
            except TypeError as te:
                # the provided value is not a list so we will just force it to a list
                self.metadata = [self.metadata]
        if self.techniques:
            try:
                self.techniques = [x.strip() for x in self.techniques.split(',')]
            except TypeError as te:
                # the provided value is not a list so we will just force it to a list
                self.techniques = [self.techniques]
        if self.observations:
            return_list = []
            for item in self.observations:
                return_list.append(Observation(**item))
            self.observations = return_list


@define
class Surface:
    name: AnyStr = field(factory=str)
    category: AnyStr = field(factory=str, metadata={"question": Template("Which category does the $name surface belong to? ")})
    events: List[Event] = field(factory=list)


@define
class ThreatDrivenSecurity:
    name: AnyStr = field()
    version: SemVersion = field()
    license: AnyStr = field(metadata={"question": Template("Which license would you like to use? ")})
    statement: AnyStr = field(factory=str, metadata={"question": Template("How would you describe this threat? ")})
    references: List[HttpUrl] = field(factory=list, metadata={"question": Template("Include any references you would like: ")})
    metadata: Metadata = field(factory=Metadata)
    surfaces: List[Surface] = field(factory=Surface)

    @version.default
    def _version_default(self):
        return "0.0.1"

    @license.default
    def _license_default(self):
        return "MIT"
