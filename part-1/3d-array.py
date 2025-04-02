from manim import *

class SmileyFace3D(ThreeDScene):
    def construct(self):
        self.camera.background_color = "WHITE"
        # define a three dimensional array to draw smiley face + colors
        # this array is structured as a depth-first array
        three_d_arr = [
            # front layer, stores pixel state
            [
                # second pixel can be set to 1 as a control pixel as manim has goofy coord system I couldn't wrap my head around so I just went around it a little
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            # back layer, stores pixel color in case it should be turned on
            [
                [None,      "#74DB84",  None,       None,       None,       None,       None,       None],
                [None,      None,       "#DC75CD",  None,       None,       "#E8C11C",  None,       None],
                [None,      None,       "#DC75CD",  None,       None,       "#E8C11C",  None,       None],
                [None,      None,       "#DC75CD",  None,       None,       "#E8C11C",  None,       None],
                [None,      None,       None,       None,       None,       None,       None,       None],
                [None,      "#236B8E",  None,       None,       None,       None,       "#236B8E",  None],
                [None,      None,       "#236B8E",  "#236B8E",  "#236B8E",  "#236B8E",  None,       None],
                [None,      None,       None,       None,       None,       None,       None,       None],
            ],
        ]

        # prism dimensions
        screen_w = 8
        screen_h = 8

        # generate ranges to represent each coordinate
        w_range = [-3.5 + i for i in range(screen_w)]
        h_range = [3.5 - i for i in range(screen_h)]

        # set up camera for 3D view
        self.set_camera_orientation(zoom=0.8)

        # manim group to store all cubes
        cubes = VGroup()

        # iterate over pixels
        # first, iterate over the "columns" of the display
        for h_index, h_coord in enumerate(h_range):
            # iterate over the "rows" of the display
            for w_index, w_coord in enumerate(w_range):
                # extract state of pixel at given position in the array by addressing 0th index of the 3d-array, i.e. our back layer
                pixel_state = three_d_arr[0][h_index][w_index]

                # create an empty cube object
                cube = Cube(side_length=1)
                cube.move_to([w_coord, h_coord, 0])

                # create an empty cube object to store color if required for demo
                cube_back_layer = Cube(side_length=1)
                cube_back_layer.move_to([w_coord, h_coord, -1])
                                
                # if pixel is supposed to be on, check the color to fill it with, we do this by addressing the 1st index of the 3d-array, i.e. our front layer
                if pixel_state == 1:

                    # get color from back layer
                    pixel_color = three_d_arr[1][h_index][w_index]

                    # set front layer cube color to retrieved color
                    cube.set_fill(pixel_color, opacity=1)
                    cube.set_stroke(color = "BLACK", width = 1)

                    # position and render back layer cube
                    cube_back_layer.set_fill(color = "WHITE", opacity = 0)
                    cube_back_layer.set_stroke(color = "BLACK", width = 1)
                    print(f"cube @ w ={w_coord:>4.1f}, h ={h_coord:>4.1f}, color={pixel_color:<8}")
                
                # if pixel is supposed to be off, make it transparent 
                else:
                    cube.set_fill(opacity = 0)
                    cube.set_stroke(width = 0)
                    
                    cube_back_layer.set_fill(opacity = 0)
                    cube_back_layer.set_stroke(color = "BLACK", width = .1)
                    print(f"cube @ w ={w_coord:>4.1f}, h ={h_coord:>4.1f}, color={'none':<8}")

                cubes.add(cube)
                cubes.add(cube_back_layer)

        cubes.rotate(-0 * DEGREES,
                     axis=UP,
                     about_point=ORIGIN)
        cubes.rotate(0 * DEGREES,
                    axis=RIGHT,
                    about_point=ORIGIN)
        self.add(cubes)
        self.wait(3)

# To render this scene, save the script as '3d-array.py' and run:
# manim -qh -s 3d-array-render.py SmileyFace3D