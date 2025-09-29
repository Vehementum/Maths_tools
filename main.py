from categories import CATEGORY_MAP
from generator import questions_to_student_table, table_to_latex, generate_weighted_questions
import random


# Generate 50 questions
questions = generate_weighted_questions(
    n_questions=50,
    category_weights={"basic_operations": 0.5, "percentages": 0.3, "fractions": 0.2},
    level_weights={1: 0.4, 2: 0.3, 3: 0.2, 4: 0.1, 5: 0}
)

# Convert to 6-column table rows
table_rows = questions_to_student_table(questions)

# Output LaTeX
latex_code = table_to_latex(table_rows, filename="outputs/student_worksheet.tex")