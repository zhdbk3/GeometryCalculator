#
# Created by MC着火的冰块(zhdbk3) on 2024/10/27
#

import re

from sympy import (Symbol, latex, Expr, Line2D,
                   sqrt, sin, cos, tan)

from core import ProblemCore


class Problem(ProblemCore):
    def symbols_html(self) -> str:
        """获取该问题所有未知数的 HTML LaTeX 表示，并按取值范围分类在一个无序列表里"""
        # 分类
        real = []
        positive = []
        negative = []
        for symbol in self.symbols.values():
            if symbol.is_positive:
                positive.append(symbol)
            elif symbol.is_negative:
                negative.append(symbol)
            else:
                real.append(symbol)

        # 生成 HTML
        html = ''

        def add_li(symbols: list[Symbol], val_set: str) -> None:
            """
            生成无序列表的一项（如果有）
            :param symbols: 未知数列表
            :param val_set: 取值集合 LaTeX
            :return: None，直接加到了 html 上
            """
            if len(symbols) == 0:
                return
            nonlocal html
            html += (fr'<li>\('
                     fr'{",".join([latex(s) for s in symbols])} \in {val_set}'
                     fr'\)</li>')

        add_li(real, 'R')
        add_li(positive, r'\left(0, +\infty\right)')
        add_li(negative, r'\left(-\infty, 0\right)')

        return html

    def points_html(self) -> str:
        """获取该问题所有点的 HTML LaTeX 表示，放在一个无序列表里"""
        html = ''
        for name, p in self.points.items():
            html += (fr'<li>\('
                     fr'{name}\left({latex(p.x)}, {latex(p.y)}\right)'
                     fr'\)</li>')
        return html

    def eval_expr(self, s: str) -> Expr | None:
        """
        解析字符串表达式，若字符串为空，返回 None
        :param s: 字符串表达式
        :return: Expr 子类对象或 None
        """
        # 判空
        if len(s) == 0:
            return None
        # 处理表达式里的未知数
        repl = r'self.symbols["\1"]'
        for name in self.symbols.keys():
            s = re.sub(fr'\b({name})\b', repl, s)
        return eval(s)

    def eval_line(self, s: str) -> Line2D | None:
        """
        解析一条直线，若字符串为空，返回 None
        :param s: 直线，两个点的名字
        :return: Line2D 对象或 None
        """
        # 判空
        if len(s) == 0:
            return None
        pattern = r"([A-Z]_?\d*'*)" * 2  # 一个点名字
        repl = r'Line2D(self.points["\1"], self.points["\2"])'  # 必须用双引号包裹点名字，因为里面可能有撇
        s = re.sub(pattern, repl, s)
        return eval(s)
