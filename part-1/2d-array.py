from manim import *

class BinaryGrid(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        grid_size = 8
        unit_size = 1
        grid_width = grid_size * unit_size

        unit_squares = VGroup()

        binary_pattern = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]

        for i, row in enumerate(binary_pattern):
            for j, value in enumerate(row):
                square = Square(side_length=unit_size)
                square.move_to(np.array([j - grid_size / 2 + 0.5, grid_size / 2 - i - 0.5, 0]))
                if value == 1:
                    square.set_fill(BLACK, opacity=1)
                else:
                    square.set_fill(WHITE, opacity=1)
                square.set_stroke(color=BLACK, width=3)
                unit_squares.add(square)

        unit_squares.move_to(ORIGIN)

        self.add(unit_squares)
