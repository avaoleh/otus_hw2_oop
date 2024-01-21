"""module Class Square"""
from src.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, side_a):
        super().__init__(side_a, side_a)
        if side_a <= 0:
            raise ValueError("нельзя создать квадрат")

    def __str__(self):
        """Метод описания (description)"""
        return f"Square with side: {self.side_a}"
