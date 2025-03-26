from manim import *

class BinaryGrid(Scene):
    def construct(self):
        # Set the background color to white
        self.camera.background_color = WHITE

        # Define grid parameters
        grid_size = 8
        unit_size = 1
        grid_width = grid_size * unit_size

        # Create a VGroup to hold the grid squares
        unit_squares = VGroup()

        # Define the binary pattern (0s and 1s)
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

        # Create the grid squares based on the binary pattern
        for i, row in enumerate(binary_pattern):
            for j, value in enumerate(row):
                # Create a square
                square = Square(side_length=unit_size)
                # Set the square's position
                square.move_to(np.array([j - grid_size / 2 + 0.5, grid_size / 2 - i - 0.5, 0]))
                # Set the square's color based on the binary value
                if value == 1:
                    square.set_fill(BLACK, opacity=1)
                else:
                    square.set_fill(WHITE, opacity=1)
                # Set the border color
                square.set_stroke(color=BLACK, width=3)
                # Add the square to the VGroup
                unit_squares.add(square)

        # Center the grid
        unit_squares.move_to(ORIGIN)

        # Add the grid to the scene
        self.add(unit_squares)

# To render this scene, save the script as 'binary_grid.py' and run:
# manim -ql -s binary_grid.py BinaryGrid
