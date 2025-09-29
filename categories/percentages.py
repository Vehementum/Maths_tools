import random
from models.questions import Question

# -----------------------------
# Helper functions
# -----------------------------

def make_percent_of(base_range, pct_range, level):
    base = random.randint(*base_range)
    pct = random.choice(pct_range)
    result = round(base * pct / 100, 2)
    q = rf"${pct}\% \text{{ of }} {base} = \underline{{\phantom{{999}}}}$"
    return Question(q, f"${result}$", "Percentages", level)

def make_blank_percent_of(base_range, pct_range, level):
    base = random.randint(*base_range)
    pct = random.choice(pct_range)
    result = round(base * pct / 100, 2)
    q = rf"$\underline{{\phantom{{999}}}}\% \text{{ of }} {base} = {result}$"
    return Question(q, f"${pct}$", "Percentages", level)

def make_percentage_of(base_range, result_range, level):
    base = random.randint(*base_range)
    result = random.randint(*result_range)
    pct = round(result * 100 / base, 2)
    q = rf"${result} \text{{ is }} \underline{{\phantom{{999}}}}\% \text{{ of }} {base}$"
    return Question(q, f"${pct}$", "Percentages", level)

def make_blank_percentage_of(base_range, result_range, level):
    base = random.randint(*base_range)
    result = random.randint(*result_range)
    pct = round(result * 100 / base, 2)
    q = rf"$\underline{{\phantom{{999}}}} \text{{ is }} {pct}\% \text{{ of }} {base}$"
    return Question(q, f"${result}$", "Percentages", level)

def make_increase(base_range, pct_range, level):
    base = random.randint(*base_range)
    pct = random.choice(pct_range)
    result = round(base * (1 + pct / 100), 2)
    q = rf"${base} \text{{ increased by }} {pct}\% = \underline{{\phantom{{999}}}}$"
    return Question(q, f"${result}$", "Percentages", level)

def make_blank_increase(base_range, pct_range, level):
    base = random.randint(*base_range)
    pct = random.choice(pct_range)
    result = round(base * (1 + pct / 100), 2)
    q = rf"${base} \text{{ increased by }} \underline{{\phantom{{999}}}}\% = {result}$"
    return Question(q, f"${pct}$", "Percentages", level)

def make_decrease(base_range, pct_range, level):
    base = random.randint(*base_range)
    pct = random.choice(pct_range)
    result = round(base * (1 - pct / 100), 2)
    q = rf"${base} \text{{ decreased by }} {pct}\% = \underline{{\phantom{{999}}}}$"
    return Question(q, f"${result}$", "Percentages", level)

def make_blank_decrease(base_range, pct_range, level):
    base = random.randint(*base_range)
    pct = random.choice(pct_range)
    result = round(base * (1 - pct / 100), 2)
    q = rf"${base} \text{{ decreased by }} \underline{{\phantom{{999}}}}\% = {result}$"
    return Question(q, f"${pct}$", "Percentages", level)

# -----------------------------
# Main generator
# -----------------------------
def generate_question_per(level: int):
    if level == 1:
        ops = [
            lambda: make_percent_of((10, 100), [10, 25, 50], level),
            lambda: make_blank_percent_of((10, 100), [10, 25, 50], level),
        ]
    elif level == 2:
        ops = [
            lambda: make_percent_of((20, 200), list(range(5, 55, 5)), level),
            lambda: make_blank_percent_of((20, 200), list(range(5, 55, 5)), level),
            lambda: make_percentage_of((50, 200), (5, 100), level),
            lambda: make_blank_percentage_of((50, 200), (5, 100), level),
        ]
    elif level == 3:
        ops = [
            lambda: make_percent_of((50, 500), list(range(1, 31)), level),
            lambda: make_blank_percent_of((50, 500), list(range(1, 31)), level),
            lambda: make_percentage_of((100, 500), (10, 200), level),
            lambda: make_blank_percentage_of((100, 500), (10, 200), level),
            lambda: make_increase((50, 200), list(range(5, 31)), level),
            lambda: make_blank_increase((50, 200), list(range(5, 31)), level),
        ]
    elif level == 4:
        ops = [
            lambda: make_percent_of((100, 1000), list(range(1, 51)), level),
            lambda: make_blank_percent_of((100, 1000), list(range(1, 51)), level),
            lambda: make_percentage_of((200, 1000), (20, 500), level),
            lambda: make_blank_percentage_of((200, 1000), (20, 500), level),
            lambda: make_increase((100, 500), list(range(10, 51)), level),
            lambda: make_decrease((100, 500), list(range(10, 51)), level),
            lambda: make_blank_decrease((100, 500), list(range(10, 51)), level),
        ]
    elif level == 5:
        ops = [
            lambda: make_percent_of((200, 2000), list(range(1, 101)), level),
            lambda: make_blank_percent_of((200, 2000), list(range(1, 101)), level),
            lambda: make_percentage_of((500, 2000), (50, 1000), level),
            lambda: make_blank_percentage_of((500, 2000), (50, 1000), level),
            lambda: make_increase((200, 1000), list(range(1, 101)), level),
            lambda: make_blank_increase((200, 1000), list(range(1, 101)), level),
            lambda: make_decrease((200, 1000), list(range(1, 101)), level),
            lambda: make_blank_decrease((200, 1000), list(range(1, 101)), level),
        ]
    else:
        raise ValueError("Level must be between 1 and 5")

    generator = random.choice(ops)
    return generator()
