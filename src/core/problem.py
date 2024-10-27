#
# Created by MC着火的冰块(zhdbk3) on 2024/10/26
#

from typing import Literal

from sympy import Symbol, Point2D


class ProblemCore:
    def __init__(self):
        """一个数学问题，实现了最核心的功能"""
        # 由名字对应对象
        self.symbols: dict[str, Symbol] = {}
        self.points: dict[str, Point2D] = {}

    def create_symbol(self, name: str, sign: Literal['+', '-', 'R'] = 'R') -> None:
        """
        创建一个未知数
        :param name: 未知数名字
        :param sign: 该未知数的正负性，可选 '+', '-', 'R'
        :return: None
        """
        kwargs = {'real': True}
        match sign:
            case '+':
                kwargs['positive'] = True
            case '-':
                kwargs['negative'] = True
            # 怎么会不合法呢？剩下情况不写了（逃
        self.symbols[name] = Symbol(name, **kwargs)

    def create_point(self, name: str, x, y) -> None:
        """
        创建一个点
        :param name: 点名字
        :param x: x 表达式
        :param y: y 表达式
        :return: None
        """
        self.points[name] = Point2D(x, y)
