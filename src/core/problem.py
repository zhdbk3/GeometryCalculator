#
# Created by MC着火的冰块(zhdbk3) on 2024/10/26
#

from typing import Literal, Optional

from sympy import Symbol, Point2D, Line2D, Expr, solve

# x, y 的全局变量，它们一定要指定是实数，以适配 sympy.geometry 的轮子
x = Symbol('x', real=True)
y = Symbol('y', real=True)


class ProblemCore:
    def __init__(self):
        """一个数学问题，实现了最核心的功能"""
        # 由名字对应对象
        self.symbols: dict[str, Symbol] = {}
        self.points: dict[str, Point2D] = {}

    def add_symbol(self, name: str, sign: Literal['+', '-', 'R'] = 'R') -> Symbol:
        """
        添加一个未知数
        :param name: 未知数名字
        :param sign: 该未知数的正负性，可选 '+', '-', 'R'
        :return: Symbol 对象
        """
        kwargs = {'real': True}
        match sign:
            case '+':
                kwargs['positive'] = True
            case '-':
                kwargs['negative'] = True
            # 怎么会不合法呢？剩下情况不写了（逃
        symbol = Symbol(name, **kwargs)
        self.symbols[name] = symbol
        return symbol

    def add_point(self, name: str, x0: Optional[Expr] = None, y0: Optional[Expr] = None,
                  line1: Optional[Line2D] = None, line2: Optional[Line2D] = None) -> Point2D:
        """
        添加一个点
        x, y, line1, line2 中应有 2 个有值
        :param name: 点的名字
        :param x0: 横坐标
        :param y0: 纵坐标
        :param line1: 所在直线 1
        :param line2: 所在直线 2
        :return: Point2D 对象
        """
        # 合法性检查应写在网页部分，而不是这里
        if x0 is not None and y0 is not None:
            # 已知坐标
            point = Point2D(x0, y0)
        elif line1 is not None and line2 is not None:
            # 两线交点
            point = line1.intersection(line2)[0]
        else:
            # 已知一个坐标和一条所在直线
            # 已知直线的方程
            line_eq: Expr = (line1 if line1 is not None else line2).equation()
            if x0 is not None:
                # 已知横坐标，解纵坐标
                y0 = solve(line_eq.subs({x: x0}), y)[0]
            else:
                # 已知纵坐标，解横坐标
                x0 = solve(line_eq.subs({y: y0}), x)[0]
            point = Point2D(x0, y0)
        self.points[name] = point
        return point
