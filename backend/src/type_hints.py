from typing import TypedDict


class DomainSettings(TypedDict):
    negative: bool
    zero: bool
    positive: bool


class LatexItem(TypedDict):
    id: str
    latex: str


Status = tuple[bool, str]
