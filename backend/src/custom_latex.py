"""https://zhdbk3.github.io/2025/07/14/sympy-customize-latex/"""

from sympy.printing.latex import LatexPrinter, print_function
import sympy


class CustomLatexPrinter(LatexPrinter):
    def _print_MatrixBase(self, expr):
        if expr.shape[1] == 1:
            return fr"\left( {', '.join(map(self.doprint, expr))} \right)"
        else:
            return super()._print_MatrixBase(expr)


@print_function(CustomLatexPrinter)
def custom_latex(expr, **settings):
    return CustomLatexPrinter(settings).doprint(expr)


def override_latex():
    sympy.latex = custom_latex
