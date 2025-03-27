from manim import *

class WireframeCubeWithCells(ThreeDScene):
    def construct(self):
        # Set the background color to white
        self.camera.background_color = WHITE

        arr_d = 2
        arr_w = 8
        arr_h = 8
        # Create the outer wireframe cube
        outer_cube = Cube(side_length=1)
        outer_cube.scale([arr_d, arr_w, arr_h])  # depth x width x height
        outer_cube.set_fill(opacity=0)  # Make the faces transparent

        # Binary pattern for the smiley face
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

        # Create the individual inner cubes using loops
        cells = VGroup()
        depth_range = [0.5 - i for i in range(arr_d)]  # Depth range: 2 cubes
        width_range = [-3.5 + i for i in range(arr_w)]  # Width range: 8 cubes
        height_range = [-3.5 + i for i in range(arr_h)]  # Height range: 8 cubes

        for x in depth_range:
            for i, y in enumerate(width_range):
                for j, z in enumerate(height_range):
                    cell = Cube(side_length=1)
                    if x == 0.5 and binary_pattern[7 - j][i] == 1:  # Flip vertically
                        cell.set_fill(color=GOLD, opacity=0.2)  # Highlight smiley face
                    elif x == 0.5:
                        cell.set_fill(color=GREEN, opacity=0.2)  # Default to gray
                    else:
                        cell.set_fill(opacity=0)
                    cell.set_stroke(color=BLACK, width=1, opacity=0.1)  # Set edge color to black
                    cell.move_to([x, y, z])  # Position the cell
                    cells.add(cell)

                    # Only add text at the depth index -0.5
                    bool_value = 1 if binary_pattern[7 - j][i] == 1 else 0
                    if x == .5:
                        text = Text(f"({bool_value})", font="JetBrainsMono Nerd Font", color=BLACK)
                        text.scale(0.15)  # Scale down the text
                        text.move_to([x+.5, y, z])  # Center the text inside the cube
                        self.add_fixed_orientation_mobjects(text)
                        self.add(text)
                    if x == -0.5:
                        bool_value = 1 if binary_pattern[7 - j][i] == 1 else 0
                        hex_value = "#F0AC5F" if bool_value == 1 else "#83C167"
                        text = Text(f"({hex_value})", font="JetBrainsMono Nerd Font", color=BLACK)
                        text.scale(0.15)  # Scale down the text
                        text.move_to([x-.5, y, z])  # Center the text inside the cube
                        self.add_fixed_orientation_mobjects(text)
                        self.add(text)


        # Add the outer cube and inner cells to the scene
        self.add(outer_cube, cells)

        # Camera settings
        self.camera.set_zoom(0.8)  # Adjust the zoom factor
        self.set_camera_orientation(phi=75 * DEGREES, theta=45* DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)  # Optional: Rotate the camera for better visualization
