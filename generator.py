import math
from textwrap import dedent
import os

def questions_to_student_table(questions):
    """
    Convert a list of Question instances into 6-column table rows for LaTeX.
    Returns a list of rows: [#1, Q1_text, #2, Q2_text, A1, A2].
    """
    n = len(questions)
    half = math.ceil(n / 2)
    left_qs = questions[:half]
    right_qs = questions[half:]
    
    # Pad right_qs if odd number of questions
    while len(right_qs) < len(left_qs):
        right_qs.append(None)
    
    table_rows = []
    for i in range(len(left_qs)):
        q1 = left_qs[i]
        q2 = right_qs[i]
        
        row = [
            i + 1,  # left number
            q1.text if q1 else "",  # Q1
            i + 1 + half if q2 else "",  # right number
            q2.text if q2 else "",  # Q2
            q1.answer if q1 else "",  # A1
            q2.answer if q2 else ""   # A2
        ]
        table_rows.append(row)
    
    return table_rows


def table_to_latex(table_rows, filename="latex/src/student_worksheet.tex"):
    """
    Convert a 6-column student table into a LaTeX tabular and save to file.
    Assumes all cells are already valid LaTeX (math mode if needed).
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    header = dedent(r"""
    \documentclass[french,a4paper,10pt]{article}
    \input{latex/src/common/common_header.tex}
    \input{latex/src/common/macros/math.tex}
    \input{latex/src/common/macros/theorems.tex}
    \usepackage[a4paper,hmargin=30mm,vmargin=30mm]{geometry}
    \usepackage{array}
    \title{\hspace{-2.0cm}\color{astral} \sffamily \bfseries Fiche de calcul mental}
    \author{\hspace{-2.0cm}Stéphane Lejeune}
    \date{\hspace{-2.0cm}\today}

    \begin{document}
    \maketitle
    \noindent
    \renewcommand{\arraystretch}{1.6}
    \center
    \begin{tabular}{|c|p{4cm}|c|p{4cm}||p{1cm}|p{1cm}|}
    \hline
    """)

    rows = ""
    for row in table_rows:
        # Convert all cells to string
        row_str = [str(cell) for cell in row]
        rows += " & ".join(row_str) + r" \\" + "\n" + r"\hline" + "\n"

    footer = dedent(r"""
    \end{tabular}
    \end{document}
    """)

    latex_code = header + rows + footer

    with open(filename, "w", encoding="utf-8") as f:
        f.write(latex_code)

    print(f"LaTeX table written to {filename}")
    return latex_code

import random
from categories import CATEGORY_MAP

def generate_weighted_questions(
    n_questions: int,
    category_weights: dict[str, float],
    level_weights: dict[int, float]
) -> list:
    """
    Generate a list of Question instances with weighted probability over categories and levels.

    :param n_questions: Number of questions to generate
    :param category_weights: Dictionary mapping category names to weights, e.g.
                             {"basic_operations": 0.4, "fractions": 0.2, ...}
    :param level_weights: Dictionary mapping level numbers (1-5) to weights, e.g.
                          {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.3, 5: 0.1}
    :return: List of Question instances
    """
    # Normalize weights
    cat_names = list(category_weights.keys())
    cat_probs = [category_weights[c] for c in cat_names]
    total_cat = sum(cat_probs)
    cat_probs = [w / total_cat for w in cat_probs]

    lvl_numbers = list(level_weights.keys())
    lvl_probs = [level_weights[l] for l in lvl_numbers]
    total_lvl = sum(lvl_probs)
    lvl_probs = [w / total_lvl for w in lvl_probs]

    questions = []
    for _ in range(n_questions):
        # Pick category and level
        chosen_cat = random.choices(cat_names, weights=cat_probs, k=1)[0]
        chosen_lvl = random.choices(lvl_numbers, weights=lvl_probs, k=1)[0]

        # Generate question
        question_func = CATEGORY_MAP[chosen_cat]
        q = question_func(level=chosen_lvl)
        questions.append(q)

    return questions