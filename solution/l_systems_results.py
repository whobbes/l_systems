import turtle
import random as rd

class LsystemDrawer:
        
        def __init__(self, turtle, instructions, iterations=3, angle=120, size=40, 
                        forwardChars=['A','B','F','G'], 
                        leftChars=['-'], 
                        rightChars=['+'], 
                        replacements={'+':'+', '-':'-', 'A':"B-A-B", 'B':"A+B+A", 'G': "GG", 'F':"F-G+F+G-F"}):
                self.turtle = turtle
                self.angle = angle
                self.distance = size/(iterations**2)
                self.forwardChars = forwardChars
                self.leftChars = leftChars
                self.rightChars = rightChars
                self.instructions = instructions
                self.iterations = iterations
                self.replacements = replacements

        def calc_for_n_iterations(self):
                for n in range(0,self.iterations):
                        acc = ""
                        for instruction in self.instructions:
                                acc += self.replacements[instruction]
                        self.instructions = acc
                print(self.instructions)

        def draw(self):
                for instruction in self.instructions:

                        if instruction in self.forwardChars:
                                self.turtle.forward(self.distance)

                        elif instruction in self.leftChars:
                                self.turtle.left(self.angle)

                        elif instruction in self.rightChars:
                                self.turtle.right(self.angle)

if __name__ == "__main__":

        # Create objects
        t = turtle.Turtle()
        t.speed(0)
        wn = turtle.Screen()

        # Setup pen
        t.pencolor((rd.random(), rd.random(), rd.random()))
        t.shape("turtle")

        # Create system
        # l_sys = LsystemDrawer(t, 'F-G-G')
        l_sys = LsystemDrawer(t, 'A', angle=60)

        # Draw message
        l_sys.calc_for_n_iterations()
        l_sys.draw()

        t.penup()
        t.forward(100)
        t.write("Job done :)  ", True, font=("Arial", 24, "normal"))

        # Keep window open until user click or close it
        wn.exitonclick()