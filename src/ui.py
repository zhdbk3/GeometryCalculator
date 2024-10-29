#
# Created by MC着火的冰块(zhdbk3) on 2024/10/26
#

from pyscript import document
from js import MathJax
from sympy import Expr, Line2D

from interface import Problem

problem = Problem()


def output(content) -> None:
    output_div = document.querySelector('#output')
    output_div.innerText += f'{content}\n'


def add_symbol(event) -> None:
    """创建一个未知数"""
    name = document.querySelector('#symbol-name').value
    sign = document.querySelector('input[name="symbol-sign"]:checked').value
    problem.add_symbol(name, sign)
    # 显示已有的未知数
    show_symbols()


def show_symbols() -> None:
    """显示已有的未知数"""
    symbols_ul = document.querySelector('#symbols')
    symbols_ul.innerHTML = problem.symbols_html()
    # 重新渲染
    MathJax.typeset()


def add_point(event) -> None:
    """添加一个点"""
    # TODO: 合法性检查

    # 读取并解析输入
    name = document.querySelector('#point-name').value
    x0 = problem.eval_expr(document.querySelector('#point-x').value)
    y0 = problem.eval_expr(document.querySelector('#point-y').value)
    line1 = problem.eval_line(document.querySelector('#point-line1').value)
    line2 = problem.eval_line(document.querySelector('#point-line2').value)
    # 添加点
    problem.add_point(name, x0, y0, line1, line2)
    # 显示已有的点
    show_points()


def show_points() -> None:
    """显示已有的点"""
    points_ul = document.querySelector('#points')
    points_ul.innerHTML = problem.points_html()
    # 重新渲染
    MathJax.typeset()
