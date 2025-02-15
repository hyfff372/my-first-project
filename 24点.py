import random
import math
#def distance(x1, y1, x2)
from itertools import permutations, product

def calculate(a, b, op):
    """执行四则运算"""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else None

def generate_expressions(nums, ops):
    """按照不同的计算顺序生成表达式"""
    a, b, c, d = nums
    op1, op2, op3 = ops

    expressions = [
        f"(({a} {op1} {b}) {op2} {c}) {op3} {d}",
        f"({a} {op1} ({b} {op2} {c})) {op3} {d}",
        f"{a} {op1} (({b} {op2} {c}) {op3} {d})",
        f"{a} {op1} ({b} {op2} ({c} {op3} {d}))"
    ]
    
    return expressions

def evaluate_expression(expr):
    """计算表达式的值"""
    try:
        return abs(eval(expr) - 24) < 1e-6
    except ZeroDivisionError:
        return False

def solve_24(nums):
    """寻找所有可能的 24 点表达式"""
    operators = ['+', '-', '*', '/']
    results = set()

    for num_perm in permutations(nums):
        for ops in product(operators, repeat=3):
            expressions = generate_expressions(num_perm, ops)
            for expr in expressions:
                if evaluate_expression(expr):
                    results.add(expr)

    return results

# 示例
nums = list(map(int, input().split()))
solutions = solve_24(nums)

if solutions:
    print(f"找到 {len(solutions)} 个解：")
    for expr in solutions:
        print(expr)
else:
    print("没有找到解")
