from typing import Optional
from functools import cache

from sympy import Symbol, latex

from .math_obj import MathObj
from type_hints import DomainSettings


def get_domain_latex_and_assumptions(domain_settings: Optional[DomainSettings] = None) -> tuple[str, dict[str, bool]]:
    if domain_settings is not None:
        domain_list = [domain_settings[i] for i in ['negative', 'zero', 'positive']]  # type: ignore
    else:
        domain_list = [True, True, True]

    match domain_list:
        case [True, True, True]:
            return r'\mathbb{R}', {'real': True}
        case [True, False, False]:
            return r'(-\infty, 0)', {'negative': True}
        case [True, True, False]:
            return r'(-\infty, 0]', {'nonpositive': True}
        case [False, False, True]:
            return r'(0, +\infty)', {'positive': True}
        case [False, True, True]:
            return r'[0, +\infty)', {'nonnegative': True}
        case [True, False, True]:
            return r'(-\infty, 0) \cup (0, +\infty)', {'nonzero': True}

    # 前端已经做过合法性检查，实际上不可能执行到这里
    # 仅用于消除 IDE 警告
    return '', {}


class GCSymbol(MathObj):
    def __init__(self, name: str, domain_settings: Optional[DomainSettings] = None):
        """
        几何计算器中的符号
        为与 SymPy 的 ``Symbol`` 区分，在前面加上了 GC- (Geometry Calculator) 前缀
        :param name: 符号名称，通常为一个小写英文字母（x, y 除外）或希腊字母的英文拼写
                     特殊时，为类似 x_A 的格式，这是在输入点坐标为空时创建的
        :param domain_settings: 取值范围设置
                                若为 None，则视作 R（方便后端调用）
        """
        super().__init__(name)
        self.domain_latex, assumptions = get_domain_latex_and_assumptions(domain_settings)
        self.sp_symbol = Symbol(name, **assumptions)

    @cache
    def get_name_latex(self) -> str:
        return latex(self.sp_symbol)

    @cache
    def get_domain_latex(self) -> str:
        return self.domain_latex
