from functools import cache

from sympy import Expr, latex, Point2D

from .math_obj import MathObj


class GCPoint(MathObj):
    def __init__(self, name: str, x: Expr, y: Expr):
        """
        几何计算器中的点
        :param name: 点名称，一个大写字母
        :param x: 横坐标
        :param y: 纵坐标
        """
        super().__init__(name)
        self.x = x
        self.y = y
        self.sp_point = Point2D(x, y)

    @cache
    def get_latex(self) -> str:
        return fr'{self.id} \left( {latex(self.x)}, {latex(self.y)} \right)'
