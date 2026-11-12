"""示例被测代码：仅用于产出覆盖率报告。"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def classify(n):
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"
