from typing import Callable


def mark_vec_coord(expr: str) -> str:
    """用 ``Matrix([])`` 标记表达式中向量的坐标表示（二元组）"""
    char_list = list(expr)
    # 找出所有逗号
    comma_indexes = [i for i, c in enumerate(char_list) if c == ',']
    for comma_i in comma_indexes:
        # 向左找出未闭合的左括号
        n = 1
        for i in range(comma_i, -1, -1):
            if char_list[i] == ')':
                n += 1
            elif char_list[i] == '(':
                n -= 1
                if n == 0:
                    char_list[i] = 'Matrix(['
                    break
        # 向右找出未闭合的右括号
        n = 1
        for i in range(comma_i, len(char_list)):
            if char_list[i] == '(':
                n += 1
            elif char_list[i] == ')':
                n -= 1
                if n == 0:
                    char_list[i] = '])'
                    break
    return ''.join(char_list)


class Infix:
    """【Python 竟然允许这种语法， Python中缀运算符】 https://www.bilibili.com/video/BV1Xe411r7VE"""

    def __init__(self, func: Callable):
        self.func = func

    def __rmatmul__(self, other) -> 'Infix':
        return Infix(lambda var: self.func(other, var))

    def __matmul__(self, other):
        return self.func(other)


dot = Infix(lambda a, b: a.dot(b))
