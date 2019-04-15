import turtle
import random as rd

class L_systemDrawer():
    '''Provide ways to build a L-system and draw it with a turtle'''

    def __init__(self, instructions='F-G-G', iterations=5, distance=10, angle=120):
        self.t = turtle.Turtle()
        self.wn = turtle.Screen()
        self.instructions = instructions
        self.iterations = iterations
        self.distance = distance
        self.angle = angle
        self._iterate_instructions()
        self.t.pencolor((rd.random(), rd.random(), rd.random()))
        self.t.speed('fastest')
        self.t.shape("turtle")

    def _iterate_instructions(self):
        for _ in range(self.iterations):
            next_instructions = ''
            for instruction in self.instructions:
                if instruction == 'F':
                    next_instructions += 'F-G+F+G-F'
                elif instruction == 'G':
                    next_instructions += 'GG'
                elif instruction == 'A':
                    next_instructions += 'B-A-B'
                elif instruction == 'B':
                    next_instructions += 'A+B+A'
                elif instruction == '1':
                    next_instructions += '1+2-11+1+11+12+11-2+11-1-11-12-111'
                elif instruction == '2':
                    next_instructions += '222222'
                if instruction == '3':
                    next_instructions += '3+3-3-3+3'
                else:
                    next_instructions += instruction

            self.instructions = next_instructions
        print(self.instructions)

    def draw(self):
        for instruction in self.instructions:

            self.t.pencolor((rd.random(), rd.random(), rd.random()))

            if (instruction == 'F'
             or instruction =='G'
             or instruction =='A'
             or instruction =='B'
             or instruction =='1'
             or instruction == '3'):
                self.t.pendown()
                self.t.forward(self.distance)
            elif instruction == '-':
                self.t.left(self.angle)
            elif instruction == '+':
                self.t.right(self.angle)
            elif instruction == '2':
                self.t.penup()
                self.t.forward(self.distance)

    def finish_and_wait(self):
        self.t.up()
        self.t.forward(100)
        self.t.pencolor((0, 0.5, 0.5))
        self.t.write("Job done :)  ", True, font=("Arial", 24, "normal"))
        self.wn.exitonclick() # keep window open until user click or close it

if __name__ == "__main__":
    #l_sys = L_systemDrawer() # Task 1, 2, 3
    #l_sys = L_systemDrawer(instructions='A', iterations=5, angle=60, distance=10) # Task 4
    #l_sys = L_systemDrawer(instructions='-3', iterations=1, angle=90, distance=30) # Optional Task
    # l_sys = L_systemDrawer(instructions='1-1-1-1', iterations=2, angle=90, distance=10) # Task Z: Islands!
    l_sys.draw()
    l_sys.finish_and_wait()