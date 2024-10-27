#
# Created by MC着火的冰块(zhdbk3) on 2024/10/27
#

import re

from sympy import (Symbol, latex, Expr,
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

    def eval(self, s: str) -> Expr:
        """
        解析字符串表达式
        :param s: 字符串表达式
        :return: 一个 sympy.Expr 子类对象
        """
        # 处理表达式里的未知数
        repl = r'self.symbols["\1"]'
        for pattern in self.symbols.keys():
            s = re.sub(fr'\b({pattern})\b', repl, s)

        return eval(s)
