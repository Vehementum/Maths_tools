import random
from models.questions import Question

# -----------------------------
# Helper functions
# -----------------------------

def make_power(base_range, exp_range, level):
    base = random.randint(*base_range)
    exp = random.randint(*exp_range)
    q = rf"${base}^{exp} = \underline{{\phantom{{999}}}}$"
    return Question(q, f"${base ** exp}$", "Powers & Roots", level)

def make_blank_power(base_range, exp_range, level):
    base = random.randint(*base_range)
    exp = random.randint(*exp_range)
    q = rf"${base}^{{\underline{{\phantom{{9}}}}}} = {base ** exp}$"
    return Question(q, f"${exp}$", "Powers & Roots", level)

def make_square_root(max_root, level):
    root = random.randint(2, max_root)
    q = rf"$\sqrt{{{root ** 2}}} = \underline{{\phantom{{999}}}}$"
    return Question(q, f"${root}$", "Powers & Roots", level)

def make_blank_square_root(max_root, level):
    root = random.randint(2, max_root)
    q = rf"$\sqrt{{\underline{{\phantom{{999}}}}}} = {root}$"
    return Question(q, f"${root**2}$", "Powers & Roots", level)

def make_cube_root(max_root, level):
    root = random.randint(2, max_root)
    q = rf"$\sqrt[3]{{{root ** 3}}} = \underline{{\phantom{{999}}}}$"
    return Question(q, f"${root}$", "Powers & Roots", level)

def make_blank_cube_root(max_root, level):
    root = random.randint(2, max_root)
    q = rf"$\sqrt[3]{{\underline{{\phantom{{999}}}}}} = {root}$"
    return Question(q, f"${root**3}$", "Powers & Roots", level)

# -----------------------------
# Main generator
# -----------------------------
def generate_question_p_r(level: int):
    if level == 1:
        ops = [
            lambda: make_power((2, 12), (2, 2), level),   # squares
            lambda: make_power((2, 6), (3, 3), level),    # small cubes
            lambda: make_square_root(12, level),
            lambda: make_blank_power((2, 12), (2, 2), level),
            lambda: make_blank_square_root(12, level),
        ]
    elif level == 2:
        ops = [
            lambda: make_power((2, 20), (2, 2), level),
            lambda: make_power((2, 10), (3, 3), level),
            lambda: make_square_root(20, level),
            lambda: make_cube_root(5, level),
            lambda: make_blank_power((2, 20), (2, 3), level),
            lambda: make_blank_square_root(20, level),
            lambda: make_blank_cube_root(5, level),
        ]
    elif level == 3:
        ops = [
            lambda: make_power((2, 15), (2, 4), level),
            lambda: make_square_root(25, level),
            lambda: make_cube_root(7, level),
            lambda: make_blank_power((2, 15), (2, 4), level),
            lambda: make_blank_square_root(25, level),
            lambda: make_blank_cube_root(7, level),
        ]
    elif level == 4:
        ops = [
            lambda: make_power((2, 20), (2, 4), level),
            lambda: make_square_root(30, level),
            lambda: make_cube_root(10, level),
            lambda: make_blank_power((2, 20), (2, 4), level),
            lambda: make_blank_square_root(30, level),
            lambda: make_blank_cube_root(10, level),
        ]
    elif level == 5:
        ops = [
            lambda: make_power((2, 30), (2, 5), level),
            lambda: make_square_root(40, level),
            lambda: make_cube_root(15, level),
            lambda: make_blank_power((2, 30), (2, 5), level),
            lambda: make_blank_square_root(40, level),
            lambda: make_blank_cube_root(15, level),
        ]
    else:
        raise ValueError("Level must be between 1 and 5")

    generator = random.choice(ops)
    return generator()
