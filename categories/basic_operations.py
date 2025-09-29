import random
from models.questions import Question

# -----------------------------
# Helper functions
# -----------------------------

def make_addition(a_range, level):
    a, b = random.randint(*a_range), random.randint(*a_range)
    q = f"${a} + {b} = \\underline{{\\phantom{{999}}}}$"
    return Question(q, f"${a + b}$", "Basic Operations", level)

def make_blank_addition(a_range, level):
    a, b = random.randint(*a_range), random.randint(*a_range)
    q = f"${a} + \\underline{{\\phantom{{999}}}} = {a + b}$"
    return Question(q, f"${b}$", "Basic Operations", level)

def make_subtraction(a_range, level):
    a, b = random.randint(*a_range), random.randint(*a_range)
    q = f"${a} - {b} = \\underline{{\\phantom{{999}}}}$"
    return Question(q, f"${a - b}$", "Basic Operations", level)

def make_blank_subtraction(a_range, level):
    a, b = random.randint(*a_range), random.randint(*a_range)
    q = f"${a} - \\underline{{\\phantom{{999}}}} = {a - b}$"
    return Question(q, f"${b}$", "Basic Operations", level)

def make_multiplication(a_range, b_range, level):
    a, b = random.randint(*a_range), random.randint(*b_range)
    q = f"${a} \\times {b} = \\underline{{\\phantom{{999}}}}$"
    return Question(q, f"${a * b}$", "Basic Operations", level)

def make_blank_multiplication(a_range, b_range, level):
    a, b = random.randint(*a_range), random.randint(*b_range)
    q = f"${a} \\times \\underline{{\\phantom{{999}}}} = {a * b}$"
    return Question(q, f"${b}$", "Basic Operations", level)

def make_division(dividend_range, divisor_range, level):
    divisor = random.randint(*divisor_range)
    dividend = divisor * random.randint(*dividend_range)
    q = f"${dividend} \\div {divisor} = \\underline{{\\phantom{{999}}}}$"
    return Question(q, f"${dividend // divisor}$", "Basic Operations", level)

def make_blank_division(dividend_range, divisor_range, level):
    divisor = random.randint(*divisor_range)
    dividend = divisor * random.randint(*dividend_range)
    q = f"${dividend} \\div \\underline{{\\phantom{{999}}}} = {dividend // divisor}$"
    return Question(q, f"${divisor}$", "Basic Operations", level)

# -----------------------------
# Main generator
# -----------------------------
def generate_question_bo(level: int):
    if level == 1:
        ops = [
            lambda: make_addition((1, 50), level),
            lambda: make_subtraction((1, 50), level),
            lambda: make_multiplication((2, 9), (2, 9), level),
            lambda: make_blank_addition((1, 50), level),
            lambda: make_blank_subtraction((1, 50), level),
            lambda: make_blank_multiplication((2, 9), (2, 9), level),
        ]
    elif level == 2:
        ops = [
            lambda: make_addition((1, 100), level),
            lambda: make_subtraction((1, 100), level),
            lambda: make_multiplication((2, 12), (2, 12), level),
            lambda: make_blank_addition((1, 100), level),
            lambda: make_blank_subtraction((1, 100), level),
            lambda: make_blank_multiplication((2, 12), (2, 12), level),
        ]
    elif level == 3:
        ops = [
            lambda: make_addition((100, 500), level),
            lambda: make_subtraction((100, 500), level),
            lambda: make_division((11, 100), (2, 12), level),
            lambda: make_multiplication((1, 100), (2, 9), level),
            lambda: make_multiplication((2, 20), (2, 20), level),
            lambda: make_blank_addition((100, 500), level),
            lambda: make_blank_subtraction((100, 500), level),
            lambda: make_blank_division((11, 100), (2, 12), level),
            lambda: make_blank_multiplication((1, 100), (2, 9), level),
            lambda: make_blank_multiplication((2, 20), (2, 20), level),
        ]
    elif level == 4:
        ops = [
            lambda: make_addition((100, 1000), level),
            lambda: make_subtraction((100, 1000), level),
            lambda: make_division((100, 500), (2, 12), level),
            lambda: make_multiplication((1, 500), (2, 12), level),
            lambda: make_multiplication((2, 25), (2, 25), level),
            lambda: make_blank_addition((100, 1000), level),
            lambda: make_blank_subtraction((100, 1000), level),
            lambda: make_blank_division((100, 500), (2, 12), level),
            lambda: make_blank_multiplication((1, 500), (2, 12), level),
            lambda: make_blank_multiplication((2, 25), (2, 25), level),
        ]
    elif level == 5:
        ops = [
            lambda: make_addition((100, 1000), level),
            lambda: make_subtraction((100, 1000), level),
            lambda: make_division((100, 1000), (2, 20), level),
            lambda: make_multiplication((1, 500), (2, 12), level),
            lambda: make_multiplication((2, 30), (2, 30), level),
            lambda: make_blank_addition((100, 1000), level),
            lambda: make_blank_subtraction((100, 1000), level),
            lambda: make_blank_division((100, 1000), (2, 20), level),
            lambda: make_blank_multiplication((1, 500), (2, 12), level),
            lambda: make_blank_multiplication((2, 30), (2, 30), level),
        ]

    else:
        raise ValueError("Level must be between 1 and 5")

    generator = random.choice(ops)
    return generator()
