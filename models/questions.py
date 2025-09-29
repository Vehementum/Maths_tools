class Question:
    def __init__(self, text, answer, category, level):
        self.text = text        # LaTeX string
        self.answer = answer    # LaTeX string
        self.category = category
        self.level = level