from turtle import Turtle

SEGMENT_SIZE = 20
START_SNAKE_SIZE = 3

RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_size = START_SNAKE_SIZE
        self.segments = []
        self.draw_snake()
        self.head = self.segments[0]

    def draw_snake(self):
        x_coord = 0
        y_coord = 0
        for _ in range(self.snake_size):
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.goto(x_coord, y_coord)
            self.segments.append(t)
            x_coord -= SEGMENT_SIZE

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(SEGMENT_SIZE)

    def right(self):
        if self.head.heading() == LEFT:
            return
        self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() == DOWN:
            return
        self.head.setheading(UP)

    def left(self):
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() == UP:
            return
        self.head.setheading(DOWN)
