from typing_extensions import runtime
from manim import *
from numpy import square

class Sq(Scene):
    def construct(self):            
        # points for lines
        point = (1,0,0)
        start1 = (-1.5,0,0)
        stop1 = (3.5,0,0)
        start2 = (1,0,0)
        stop2 = (1,2.5,0)
        start3 = (1,1.25,0)
        stop3 = (3.5,1.25,0)
        start4 = (2.25,1.25,0)
        stop4 = (2.25,2.5,0)

        # Shape and text Definitions
        square1 = Square()
        square2 = Square()
        line1 = Line(start1, stop1)
        line2 = Line(start2, stop2)
        line3 = Line(start3, stop3)
        line4 = Line(start4, stop4)  
        area_total = Text("Total area = 2")
        br = Brace(area_total, sharpness = 1)
        br.move_to(3*UP + LEFT).rotate(PI).scale(1)
        area_total.move_to(3.4*UP + LEFT).scale(0.6)
        k = Group(square1, square2, line1, line2, line3, line4, area_total, br)
        

        # The code that creates the text's and shapes
        square1.move_to(4*LEFT)
        square2.move_to(4*LEFT)
        self.play(Create(square1.set_width(5)))
        self.play(Create(square2.set_width(5)), runtime = 0.5)
        square2.move_to(point)
        self.play(Create(square2), runtime = 0.5)
        self.play(Create(line1), runtime = 0.5)
        self.play(Create(line2), runtime = 0.5)
        self.play(Create(line3), runtime = 0.5)
        self.play(Create(line4), runtime = 0.5)
        self.play(DrawBorderThenFill(br), runtime = 0.5)
        self.play(Write(area_total), runtime = 0.5)
        self.wait(2)

        self.play(FadeOut(k))
        
        # Second part

        sum = Tex(r"$\text{The sum of all the squares} = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... + \frac{2}{2^n}$")
        reasoning = Text("Which is going to be equal to 2 since both the areas of the large squares combined will give us 2")
        Conclusion = Tex(r"Therefore $1 + \frac{1}{2} + \frac{1}{4} ...$ = 2")
        l = Group(sum, reasoning,Conclusion)
        self.play(Write(sum))
        self.play(ApplyMethod(sum.shift, 3*UP + LEFT))
        self.play(ApplyMethod(sum.scale, 0.6))
        self.play(Write(reasoning.scale(0.5)))
        self.wait(1)
        Conclusion.scale(0.8).to_edge(DOWN)
        self.play(Write(Conclusion))
        self.wait(3)
        self.play(FadeOut(l))

class Proof(Scene):
    def construct(self):
        proof = ImageMobject("media/Assets/Images/Sum of geometric series.png")
        self.add(proof.scale(0.9))
        self.wait(5)
        self.play(ApplyMethod(proof.scale, 0.5))
        self.wait(.5)
        self.play(ApplyMethod(proof.shift, 1.45*UP))
        Step1 = Tex(r"Here the slope of OP is $x$ or we can say that $\frac{PN}{NO}$ is $x$")
        Step2 = Tex(r"Let $1 + x + x^2 + x^3 + ... x^{n-1}$ be S")
        Step3 = Tex(r"PN $= x + x^2 + x^3 + ... + x^n = x(1 + x + x^2 + x^3 ... x^{n-1}) = xS$ ")
        Step4 = Tex(r"ON $= 1 + x + x^2 + x^3 + ... + x^{n-1} = S$")
        

        self.play(Write(Step1.shift(2*DOWN)))
        self.wait(1)
        self.play(Write(Step2.shift(2.5*DOWN)))
        self.wait(1)        
        self.play(Write(Step3.shift(3*DOWN)))
        self.wait(1)
        self.play(Write(Step4.shift(3.5*DOWN)))
        self.play(ApplyMethod(proof.scale, 0))
        f4steps = Group(Step1, Step2, Step3, Step4)
        self.play(ApplyMethod(f4steps.to_edge, UP))
        lines = VGroup(
            Tex("$S$", " - ", "1 ", "= ", "$x$", "S"),
            Tex("$S$", " - ", "$x$", "$S $", "=", " 1"),
            Tex("$S$", "$(1-x) $", "=", " 1"),
            Tex("$S$", " = ", r"$\frac{1}{1 - x}$")
        )
        pt = {"run_time": 1}
        self.play(Write(lines[0]))
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1].shift(DOWN),
                path_arc=90 * DEGREES,
            ),
            **pt
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2].shift(2*DOWN),
                path_arc=90 * DEGREES,
            ),
            **pt
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(
                lines[2].copy(), lines[3].shift(3*DOWN),
                path_arc=90 * DEGREES,
            ),
            **pt
        )
        self.play(FadeOut(lines[0], lines[1], lines[2], Step1, Step2, Step3, Step4))
        self.play(ApplyMethod(lines[3].shift, 3*UP))
        self.play(ApplyMethod(lines[3].scale, 6))
        self.wait(3)

        

    
