from manim import *

class BinaryRectangle(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        grid_size = 8
        unit_size = 1

        rect = Rectangle(width=grid_size, height=unit_size, color=BLACK, fill_opacity=0.1)

        binary_string = "00101011"
        unit_width = rect.width / len(binary_string)

        unit_squares = VGroup(*[
            Square(side_length=unit_width, color=BLACK, fill_color=BLACK if digit == "1" else WHITE, fill_opacity=1)
            for digit in binary_string
        ])

        for i, square in enumerate(unit_squares):
            square.move_to(rect.get_left() + unit_width * (i + 0.5) * RIGHT)

        self.add(rect)
        self.add(unit_squares)
