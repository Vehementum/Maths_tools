import random
from models.questions import Question

# -----------------------------
# Helper functions
# -----------------------------

def make_linear_eq_add(level):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    q = rf"Solve for $x$: $x + {a} = {a+b}$"
    return Question(q, f"$x={b}$", "Algebra", level)

def make_linear_eq_mul(level):
    a = random.randint(2, 12)
    b = random.randint(1, 20)
    q = rf"Solve for $x$: ${a}x = {a*b}$"
    return Question(q, f"$x={b}$", "Algebra", level)

def make_substitution_linear(level):
    x = random.randint(1, 10)
    a, b = random.randint(1, 10), random.randint(1, 10)
    q = rf"Evaluate ${a}x + {b}$ for $x={x}$"
    return Question(q, f"${a*x+b}$", "Algebra", level)

def make_substitution_quadratic(level):
    x = random.randint(1, 10)
    a, b, c = random.randint(1, 5), random.randint(1, 5), random.randint(0, 5)
    q = rf"Evaluate ${a}x^2 + {b}x + {c}$ for $x={x}$"
    return Question(q, f"${a*x**2 + b*x + c}$", "Algebra", level)

def make_distributive(level):
    a, b = random.randint(1, 10), random.randint(1, 10)
    c, d = random.randint(1, 10), random.randint(1, 10)
    q = rf"Expand: $(x+{a})(x+{b})$"
    expanded = f"$x^2 + {(a+b)}x + {a*b}$"
    return Question(q, expanded, "Algebra", level)

def make_factorization(level):
    a, b = random.randint(1, 10), random.randint(1, 10)
    q = rf"Factorize: $x^2 + {(a+b)}x + {a*b}$"
    return Question(q, rf"$(x+{a})(x+{b})$", "Algebra", level)

def make_linear_eq_two_step(level):
    a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 50)
    rhs = a * c + b
    q = rf"Solve: ${a}x + {b} = {rhs}$"
    return Question(q, f"$x={c}$", "Algebra", level)

# -----------------------------
# Main generator
# -----------------------------

def generate_question_alg(level: int):
    if level == 1:
        ops = [
            lambda: make_linear_eq_add(level),
            lambda: make_linear_eq_mul(level),
            lambda: make_substitution_linear(level),
        ]
    elif level == 2:
        ops = [
            lambda: make_linear_eq_two_step(level),
            lambda: make_distributive(level),
            lambda: make_substitution_quadratic(level),
        ]
    elif level == 3:
        ops = [
            lambda: make_factorization(level),
            lambda: make_linear_eq_two_step(level),
            lambda: make_substitution_quadratic(level),
        ]
    elif level == 4:
        ops = [
            lambda: make_distributive(level),
            lambda: make_factorization(level),
            lambda: make_linear_eq_two_step(level),
            lambda: make_substitution_quadratic(level),
        ]
    elif level == 5:
        ops = [
            lambda: make_distributive(level),
            lambda: make_factorization(level),
            lambda: make_linear_eq_two_step(level),
            lambda: make_substitution_quadratic(level),
        ]
    else:
        raise ValueError("Level must be between 1 and 5")

    generator = random.choice(ops)
    return generator()
