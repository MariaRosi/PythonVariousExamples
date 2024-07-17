import random
import turtle
import time

# Screen setup
wn = turtle.Screen()
wn.title("Snake Game For Rishan")
wn.bgcolor("green")
wn.setup(height=600, width=600)
wn.tracer(1)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

segments = []

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)



# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_right():
    head.direction = "right"

def go_left():
    head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")



# Main Game Loop
while True:
    wn.update()

    # Check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() >290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for each_segment in segments:
            each_segment.goto(1000, 1000)

        # Clear the segments
        segments.clear()

    # Check for collision with food
    if head.distance(food) < 20:
        # Move to random place
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the segment
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    time.sleep(0.2)


wn.mainloop()