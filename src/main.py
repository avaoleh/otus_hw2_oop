from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle

if __name__ == "__main__":
    my_rectangle = Rectangle(3, 5)
    my_square = Square(5)
    my_circle = Circle(5)
    my_triangle = Triangle(3, 4, 5)

    geom = [my_rectangle, my_square, my_circle, my_triangle]
    for g in geom:
        print(g)
        print(f"perimeter:{g.get_perimeter()}")
        print(f"area:{g.get_area()}")
