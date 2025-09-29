import random
from models.questions import Question

# -----------------------------
# Helper functions
# -----------------------------

def make_addition(d1_range, d2_range, level):
    d1 = random.randint(*d1_range)
    d2 = random.randint(*d2_range)
    n1, n2 = random.randint(1, d1 - 1), random.randint(1, d2 - 1)
    q = rf"$\tfrac{{{n1}}}{{{d1}}} + \tfrac{{{n2}}}{{{d2}}} = \underline{{\phantom{{999}}}}$"
    ans = rf"$\tfrac{{{n1*d2 + n2*d1}}}{{{d1*d2}}}$"
    return Question(q, ans, "Fractions", level)

def make_blank_addition(d1_range, d2_range, level):
    d1 = random.randint(*d1_range)
    d2 = random.randint(*d2_range)
    n1, n2 = random.randint(1, d1 - 1), random.randint(1, d2 - 1)
    total_num = n1 * d2 + n2 * d1
    q = rf"$\tfrac{{{n1}}}{{{d1}}} + \underline{{\phantom{{999}}}} = \tfrac{{{total_num}}}{{{d1*d2}}}$"
    ans = rf"$\tfrac{{{n2}}}{{{d2}}}$"
    return Question(q, ans, "Fractions", level)

def make_subtraction(d1_range, d2_range, level):
    d1 = random.randint(*d1_range)
    d2 = random.randint(*d2_range)
    n1, n2 = random.randint(1, d1 - 1), random.randint(1, d2 - 1)
    q = rf"$\tfrac{{{n1}}}{{{d1}}} - \tfrac{{{n2}}}{{{d2}}} = \underline{{\phantom{{999}}}}$"
    ans = rf"$\tfrac{{{n1*d2 - n2*d1}}}{{{d1*d2}}}$"
    return Question(q, ans, "Fractions", level)

def make_blank_subtraction(d1_range, d2_range, level):
    d1 = random.randint(*d1_range)
    d2 = random.randint(*d2_range)
    n1, n2 = random.randint(1, d1 - 1), random.randint(1, d2 - 1)
    result_num = n1 * d2 - n2 * d1
    q = rf"$\tfrac{{{n1}}}{{{d1}}} - \underline{{\phantom{{999}}}} = \tfrac{{{result_num}}}{{{d1*d2}}}$"
    ans = rf"$\tfrac{{{n2}}}{{{d2}}}$"
    return Question(q, ans, "Fractions", level)

def make_multiplication(n_range, d_range, level):
    n1, d1 = random.randint(*n_range), random.randint(*d_range)
    n2, d2 = random.randint(*n_range), random.randint(*d_range)
    q = rf"$\tfrac{{{n1}}}{{{d1}}} \times \tfrac{{{n2}}}{{{d2}}} = \underline{{\phantom{{999}}}}$"
    ans = rf"$\tfrac{{{n1*n2}}}{{{d1*d2}}}$"
    return Question(q, ans, "Fractions", level)

def make_blank_multiplication(n_range, d_range, level):
    n1, d1 = random.randint(*n_range), random.randint(*d_range)
    n2, d2 = random.randint(*n_range), random.randint(*d_range)
    q = rf"$\tfrac{{{n1}}}{{{d1}}} \times \underline{{\phantom{{999}}}} = \tfrac{{{n1*n2}}}{{{d1*d2}}}$"
    ans = rf"$\tfrac{{{n2}}}{{{d2}}}$"
    return Question(q, ans, "Fractions", level)

def make_division(n_range, d_range, level):
    n1, d1 = random.randint(*n_range), random.randint(*d_range)
    n2, d2 = random.randint(*n_range), random.randint(*d_range)
    q = rf"$\tfrac{{{n1}}}{{{d1}}} \div \tfrac{{{n2}}}{{{d2}}} = \underline{{\phantom{{999}}}}$"
    ans = rf"$\tfrac{{{n1*d2}}}{{{d1*n2}}}$"
    return Question(q, ans, "Fractions", level)

def make_blank_division(n_range, d_range, level):
    n1, d1 = random.randint(*n_range), random.randint(*d_range)
    n2, d2 = random.randint(*n_range), random.randint(*d_range)
    q = rf"$\tfrac{{{n1}}}{{{d1}}} \div \underline{{\phantom{{999}}}} = \tfrac{{{n1*d2}}}{{{d1*n2}}}$"
    ans = rf"$\tfrac{{{n2}}}{{{d2}}}$"
    return Question(q, ans, "Fractions", level)

# -----------------------------
# Main generator
# -----------------------------
def generate_question_fr(level: int):
    if level == 1:
        ops = [
            lambda: make_addition((2, 6), (2, 6), level),
            lambda: make_blank_addition((2, 6), (2, 6), level),
        ]
    elif level == 2:
        ops = [
            lambda: make_addition((2, 9), (2, 9), level),
            lambda: make_blank_addition((2, 9), (2, 9), level),
            lambda: make_subtraction((2, 9), (2, 9), level),
            lambda: make_blank_subtraction((2, 9), (2, 9), level),
        ]
    elif level == 3:
        ops = [
            lambda: make_addition((3, 12), (4, 12), level),
            lambda: make_subtraction((3, 12), (4, 12), level),
            lambda: make_multiplication((1, 9), (2, 12), level),
            lambda: make_blank_multiplication((1, 9), (2, 12), level),
        ]
    elif level == 4:
        ops = [
            lambda: make_addition((5, 15), (5, 15), level),
            lambda: make_subtraction((5, 15), (5, 15), level),
            lambda: make_multiplication((1, 12), (2, 12), level),
            lambda: make_division((1, 12), (2, 12), level),
            lambda: make_blank_division((1, 12), (2, 12), level),
        ]
    elif level == 5:
        ops = [
            lambda: make_addition((6, 20), (6, 20), level),
            lambda: make_subtraction((6, 20), (6, 20), level),
            lambda: make_multiplication((1, 15), (2, 15), level),
            lambda: make_division((1, 15), (2, 15), level),
            lambda: make_blank_addition((6, 20), (6, 20), level),
            lambda: make_blank_subtraction((6, 20), (6, 20), level),
            lambda: make_blank_multiplication((1, 15), (2, 15), level),
            lambda: make_blank_division((1, 15), (2, 15), level),
        ]
    else:
        raise ValueError("Level must be between 1 and 5")

    generator = random.choice(ops)
    return generator()
