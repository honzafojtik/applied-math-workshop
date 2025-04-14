from manim import *
import numpy as np

# run with: 
# manim -ql -s graph-scene.py GraphScene

class GraphScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE  

        ax = Axes(
            x_range=[-1.3, 1.3, .5],
            y_range=[-1.8, 1.8, .5],
            # x_range=[-.9, .9, 1],
            # y_range=[-.9, .9, 1],
            tips=False,
            axis_config={"color": BLACK, "stroke_width": 2}  
        )

        coordinates = ax.add_coordinates()
        coordinates.set_color(BLACK)  

        labels = ax.get_axis_labels(x_label=r"t", y_label=r"S_{10}(t)").set_color(BLACK)

        # uncomment a function definition before you render
        def func(x):
            # first term function
            # return (4 / np.pi) * np.sin(np.pi * x)
            
            # second term function
            # return (4 / np.pi) * (1/3) * (np.sin(3 * np.pi * x))

            # sum of the first two terms
            # return (4 / np.pi) * (
            #     np.sin(np.pi * x)
            #     + 1/3 * np.sin(3 * np.pi * x))

            # tenth term function
            # return (4 / np.pi) * (1/19) * (np.sin(19 * np.pi * x))
            
            # sum of ten terms
            # return (4 / np.pi) * (
            #     np.sin(np.pi * x) 
            #     + (1/3) * np.sin(3 * np.pi * x) 
            #     + (1/5) * np.sin(5 * np.pi * x) 
            #     + (1/7) * np.sin(7 * np.pi * x) 
            #     + (1/9) * np.sin(9 * np.pi * x) 
            #     + (1/11) * np.sin(11 * np.pi * x) 
            #     + (1/13) * np.sin(13 * np.pi * x) 
            #     + (1/15) * np.sin(15 * np.pi * x) 
            #     + (1/17) * np.sin(17 * np.pi * x) 
            #     + (1/19) * np.sin(19 * np.pi * x) 
            # )
            return x**2





        graph = ax.plot(func, color=BLACK, stroke_width=3)

        function_label = MathTex(r"f=0.5", color=BLACK)
        function_label.move_to(ax.get_corner(UR) + LEFT * 1.5 + DOWN * 0.5)

        self.play(Create(ax), Write(labels), Create(graph), Write(function_label))
        # self.play(Create(ax), Create(graph))
        self.wait(2)
