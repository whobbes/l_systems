import turtle
import random as rd

def draw(turtle):
        turtle.pendown()
        turtle.forward(50)
        turtle.penup()
        turtle.forward(100)

if __name__ == "__main__":

        # Create objects
        t = turtle.Turtle()
        wn = turtle.Screen()

        # Setup pen
        t.pencolor((rd.random(), rd.random(), rd.random()))
        t.shape("turtle")

        # Draw message
        draw(t)
        t.write("Job done :)  ", True, font=("Arial", 24, "normal"))

        # Keep window open until user click or close it
        wn.exitonclick()