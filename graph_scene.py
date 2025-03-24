from manim import *
import numpy as np

class GraphSceneExample(Scene):
    def construct(self):
        self.camera.background_color = WHITE  

        ax = Axes(
            x_range=[-1.3, 1.3, .5],
            y_range=[-1.8, 1.8, .5],
            tips=False,
            axis_config={"color": BLACK, "stroke_width": 2}  
        )

        coordinates = ax.add_coordinates()
        coordinates.set_color(BLACK)  

        labels = ax.get_axis_labels(x_label="t", y_label="g(t)").set_color(BLACK)

        def func(x):
            # return (4 / np.pi) * np.sin(2 * np.pi * 0.5 * x)
            return (4 / np.pi) * (np.sin(2* np.pi * 0.5 * x) + 1/3 * np.sin(6 * np.pi * 0.5 * x))

        graph = ax.plot(func, color=BLACK, stroke_width=3)

        # Create the function label and position it inside the plot
        function_label = MathTex(r"f=0.5", color=BLACK)
        function_label.move_to(ax.get_corner(UR) + LEFT * 1.5 + DOWN * 0.5)

        # Add elements with animations
        self.play(Create(ax), Write(labels), Create(graph), Write(function_label))
        self.wait(2)
