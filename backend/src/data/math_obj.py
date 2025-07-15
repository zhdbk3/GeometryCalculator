from abc import ABC


class MathObj(ABC):
    """
    数学对象（未知数、点、条件等）的抽象类
    :ivar id: 每个数学对象都有唯一的 ``id``
    :ivar required_by: 该对象被哪些对象依赖，存放它们的 ``id``
    """

    def __init__(self, identifier: str):
        self.id = identifier
        self.required_by: set[str] = set()

    def add_required_by(self, obj: 'MathObj') -> None:
        self.required_by.add(obj.id)
