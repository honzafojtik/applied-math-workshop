from manim import *

class WireframeCubeWithCells(ThreeDScene):
    def construct(self):
        # Set the background color to white
        self.camera.background_color = WHITE

        # Create the outer wireframe cube
        outer_cube = Cube(side_length=1)
        outer_cube.scale([2, 8, 8])  # Scale the cube to 8x8x2 units
        outer_cube.set_fill(opacity=0)  # Make the faces transparent
        outer_cube.set_stroke(color=BLACK, width=1)  # Set edge color to black

        # Create the individual cells
        cells = VGroup()
        cell = Cube(side_length=1)
        cell.scale([1, 1, 1])
        cell.set_fill(color=BLACK, opacity=0.2)  # Make the faces transparent
        cell.set_stroke(color=BLACK, width=1)  # Set edge color to black
        cell.move_to([.5, -3.5, -3.5])  # Position the cell
        cells.add(cell)

        cell = Cube(side_length=1)
        cell.scale([1, 1, 1])
        cell.set_fill(color=RED, opacity=0.2)  # Make the faces transparent
        cell.set_stroke(color=RED, width=1)  # Set edge color to black
        cell.move_to([.5, -2.5, -3.5])  # Position the cell
        cells.add(cell)

        cell = Cube(side_length=1)
        cell.scale([1, 1, 1])
        cell.set_fill(color=GREEN, opacity=0.2)  # Make the faces transparent
        cell.set_stroke(color=GREEN, width=1)  # Set edge color to black
        cell.move_to([.5, -3.5, -2.5])  # Position the cell
        cells.add(cell)

        cell = Cube(side_length=1)
        cell.scale([1, 1, 1])
        cell.set_fill(color=BLUE, opacity=0.2)  # Make the faces transparent
        cell.set_stroke(color=BLUE, width=1)  # Set edge color to black
        cell.move_to([-.5, -3.5, -3.5])  # Position the cell
        cells.add(cell)

        # for x in range(2):  # 2 units deep
        #     for y in range(8):  # 8 units high
        #         for z in range(8):  # 8 units wide
        #             cell = Cube(side_length=cell_size)
        #             cell.set_fill(opacity=0)  # Make the faces transparent
        #             cell.set_stroke(color=BLACK, width=1)  # Set edge color to black
        #             cell.move_to([x - 0.5, y - 2, z - 2])  # Position the cell
        #             cells.add(cell)

        # Add the outer cube and cells to the scene
        self.add(outer_cube, cells)

        # self.camera.set_focal_distance(5)  # Set the focal distance
        self.camera.set_zoom(0.8)  # Adjust the zoom factor
        # Set the initial camera orientation
        self.set_camera_orientation(phi=90 * DEGREES, theta=45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)  # Optional: Rotate the camera for better visualization

