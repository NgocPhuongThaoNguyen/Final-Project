
import turtle
import time
import random
import winsound

# Define frequence and duration for beep sound with winsound
freq = 500
duration = 500

score = 0
high_score = 0
level = 0
delay = 0.2

# Set up the screen
screen1 = turtle.Screen()
screen1.title("Snake Game - Thao Nguyen")
screen1.bgcolor("#001a00")
screen1.setup(width=600, height=600)
screen1.tracer(0)

# Create Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("orange")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Create Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Create Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("yellow")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Level: 0  Score: 0   High Score: 0", align="center", font=("ds-digital", 24, "normal"))


# Define Functions of keyboard's inputting for snake movement
def go_up():
    if snake.direction != "down":
        snake.direction = "up"
def go_down():
    if snake.direction != "up":
        snake.direction = "down"
def go_left():
    if snake.direction != "right":
        snake.direction = "left"
def go_right():
    if snake.direction != "left":
        snake.direction = "right"
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

#Keyboard Setup and Inputting

screen1.listen()
screen1.onkeypress(go_up, "Up")
screen1.onkeypress(go_down, "Down")
screen1.onkeypress(go_left, "Left")
screen1.onkeypress(go_right, "Right")

segments = []
while True:
    screen1.update()
    # Checking collision with border of screen
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        level = 0
        scoreboard.goto(0, 0)
        scoreboard.color("blue")
        scoreboard.write("Game Over", align="center", font=("Arial", 60, "bold"))
        time.sleep(2)
        scoreboard.clear()
        scoreboard.goto(0, 260)
        scoreboard.color("yellow")
        scoreboard.write("Level: {}  Score: {}   High Score:   {}".format(level, score, high_score), align="center",
                         font=("ds-digital", 24, "normal"))
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"

        # Hiding the segments
        for segment in segments:
            segment.goto(1000, 1000)  # This will be hidden
        segments.clear()

        score = 0
        delay = 0.2

        scoreboard.clear()
        scoreboard.write("Level: {}  Score: {}   High Score:   {}".format(level, score, high_score), align="center",
                         font=("ds-digital", 24, "normal"))

    if snake.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        winsound.Beep(freq, duration)

        delay -= 0.001
        score += 10
        # Updating level based on 50 points will increase one more level. Maximal 5 level
        if score > high_score:
            high_score = score
        scoreboard.clear()
        scoreboard.write("Level: {}  Score: {}   High Score:   {}".format(level, score, high_score), align="center",
                         font=("ds-digital", 24, "normal"))
        if score in range(50,100):
            if score == 50:
                level += 1
                scoreboard.clear()
                scoreboard.write("Level: {}  Score: {}   High Score:   {}".format(level, score, high_score), align="center",
                                 font=("ds-digital", 24, "normal"))
                delay = 0.15
        if score in range(100,150):
            if score == 100:
                level += 1
                scoreboard.clear()
                scoreboard.write("Level: {}  Score: {}   High Score:   {}".format(level, score, high_score), align="center",
                                 font=("ds-digital", 24, "normal"))
                delay = 0.1

        if score in range(150,200):
            if score == 150:
                level += 1
                scoreboard.clear()
                scoreboard.write("Level: {}  Score: {}   High Score:   {}".format(level, score, high_score), align="center",
                                 font=("ds-digital", 24, "normal"))
                delay = 0.07

        if score in range(200,250):
            if score == 200:
                level += 1
                scoreboard.clear()
                scoreboard.write("Level: {}  Score: {}   High Score:   {}".format(level, score, high_score), align="center",
                                 font=("ds-digital", 24, "normal"))
                delay = 0.05

        if score in range(250,300):
            if score == 250:
                level += 1
                scoreboard.clear()
                scoreboard.write("Level: {}  Score: {}   High Score:   {}".format(level, score, high_score), align="center",
                                 font=("ds-digital", 24, "normal"))
                delay = 0.02

    # Move segments to reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to beginning
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)
    move()

    # Checking collision with body
    for segment in segments:
        #scoreboard.goto(0, 260)
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"

            # hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.2
            scoreboard.clear()
            scoreboard.write("Level: {}  Score: {}   High Score:   {}".format(level, score, high_score), align="center",
                             font=("ds-digital", 24, "normal"))
            scoreboard.goto(0, 0)
            scoreboard.color("blue")
            scoreboard.write("Game Over", align="center", font=("Arial", 60, "bold"))
            time.sleep(2)
            scoreboard.clear()
            scoreboard.goto(0, 260)
            scoreboard.color("yellow")
            scoreboard.write("Level: {}  Score: {}   High Score:   {}".format(level, score, high_score), align="center",
                             font=("ds-digital", 24, "normal"))
            level = 0
    time.sleep(delay)
screen1.mainloop()