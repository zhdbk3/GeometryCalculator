import re

from sympy import Eq, latex, sympify
from sympy.printing.latex import LatexPrinter

from .math_obj import MathObj
from vec_parse_utils import mark_vec_coord


def to_raw_latex(expr: str) -> str:
    """
    生成出用户原始输入的表达式的 LaTeX
    只能是单个表达式
    """
    expr = mark_vec_coord(expr)

    # TODO: 支持向量点乘
    expr = latex(sympify(expr))

    rules = [
        #          ->
        # vecAB -> AB
        (r'\bvec([A-Z]{2})\b', r'\\overrightarrow{\1}'),
        # ABC -> △ABC
        (r'\b([A-Z]{3})\b', r'\\triangle \1'),
        # angABC -> ∠ABC
        (r'\bang([A-Z]{3})\b', r'\\angle \1'),
        # 删除多余点号
        (r'(?:(?<![A-Z])\s+\\cdot\s+)|(?:\s+\\cdot\s+(?![A-Z]))', '')
    ]
    for pattern, repl in rules:
        expr = re.sub(pattern, repl, expr)

    return expr


class CustomLatexPrinter(LatexPrinter):
    def _print_MatrixBase(self, expr):
        return self._print_Tuple((*expr,))


class Cond(MathObj):
    def __init__(self, raw_latex: str, eqs: list[Eq]):
        """
        一个条件，可以时简单的，也可以是复合的
        :param raw_latex: 用户原始输入的 LaTeX 形式
        :param eqs: 解析得到的方程，可能需要多个
        """
        super().__init__(raw_latex)
        self.eqs = eqs

    def get_raw_latex(self) -> str:
        # 前面用原始 LaTeX 做了 ``id``
        return self.id

    def get_eqs_latex(self) -> str:
        return ' '.join(f'$$ {latex(eq)} $$' for eq in self.eqs)
