from turtle import Turtle

SEGMENT_SIZE = 20
START_SNAKE_SIZE = 3

RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_size = START_SNAKE_SIZE
        self.segments = []
        self.draw_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def draw_snake(self):
        x_coord = 0
        y_coord = 0
        for _ in range(self.snake_size):
            self.add_segment((x_coord, y_coord))
            x_coord -= SEGMENT_SIZE

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.draw_snake()
        self.head = self.segments[0]

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(SEGMENT_SIZE)

    def extend(self):
        self.add_segment(self.tail.position())

    def add_segment(self, position):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.segments.append(t)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def tail_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 5:
                return True
