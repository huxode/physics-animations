from manim import *

class Nudging(Scene):
    def construct(self):
        func = lambda pos: RIGHT
        vector_field = ArrowVectorField(
            func, color_scheme=lambda pos: 0.1*pos[1]
        )
        self.add(vector_field)
       