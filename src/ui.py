#
# Created by MC着火的冰块(zhdbk3) on 2024/10/26
#

from pyscript import document
from js import MathJax

from interface import Problem

problem = Problem()


def output(content) -> None:
    output_div = document.querySelector('#output')
    output_div.innerText += f'{content}\n'


def create_symbol(event) -> None:
    """创建一个未知数"""
    name = document.querySelector('#symbol-name').value
    sign = document.querySelector('input[name="symbol-sign"]:checked').value
    problem.create_symbol(name, sign)
    # 显示已有的未知数
    show_symbols()


def show_symbols() -> None:
    """显示已有的未知数"""
    symbols_label = document.querySelector('#symbols')
    symbols_label.innerHTML = problem.symbols_html()
    # 重新渲染
    MathJax.typeset()


def create_point(event) -> None:
    """添加一个点"""
    name = document.querySelector('#point-name').value
    x = document.querySelector('#point-x').value
    y = document.querySelector('#point-y').value
    x = problem.eval(x)
    y = problem.eval(y)
    problem.create_point(name, x, y)
    # 显示已有的点
    show_points()


def show_points() -> None:
    """显示已有的点"""
    points_ul = document.querySelector('#points')
    points_ul.innerHTML = problem.points_html()
    # 重新渲染
    MathJax.typeset()
