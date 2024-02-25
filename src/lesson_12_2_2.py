def divide (a, b):
    if b == 0:
        return "Делить на ноль нельзя"
    return a / b

assert divide(50, 5) == 10
assert divide(5, 5) == 1
assert divide(6, 0) == "Делить на ноль нельзя"