import turtle
import random as rd

if __name__ == "__main__":

        # Create objects
        t = turtle.Turtle()
        wn = turtle.Screen()

        # Setup pen
        t.pencolor((rd.random(), rd.random(), rd.random()))
        t.shape("turtle")

        # Draw message
        t.pendown()
        t.forward(50)
        t.penup()
        t.forward(100)
        t.write("Job done :)  ", True, font=("Arial", 24, "normal"))

        # Keep window open until user click or close it
        wn.exitonclick()