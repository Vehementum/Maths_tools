from .basic_operations import generate_question_bo as basic_operations_question
from .fractions import generate_question_fr as fractions_question
from .percentages import generate_question_per as percentages_question
from .powers_roots import generate_question_p_r as powers_roots_question
from .algebra import generate_question_alg as algebra_question

CATEGORY_MAP = {
    "basic_operations": basic_operations_question,
    "fractions": fractions_question,
    "percentages": percentages_question,
    "powers_roots": powers_roots_question,
    "algebra": algebra_question,
}