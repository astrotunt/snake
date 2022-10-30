import turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.speed = 0.1
        for position in self.starting_positions:
            self.snake_segment = turtle.Turtle("square")
            self.snake_segment.color("white")
            self.snake_segment.penup()
            self.snake_segment.setposition(position)
            self.segments.append(self.snake_segment)

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            self.segments[segment_index].setposition(self.segments[segment_index - 1].position())
        self.segments[0].forward(MOVE_DISTANCE)

    def go_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def go_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def go_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def go_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def extend(self):
        self.snake_segment = turtle.Turtle("square")
        self.snake_segment.color("white")
        self.snake_segment.penup()
        self.snake_segment.setposition(self.segments[-1].position())
        self.segments.append(self.snake_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.speed = 0.1
        for position in self.starting_positions:
            self.snake_segment = turtle.Turtle("square")
            self.snake_segment.color("white")
            self.snake_segment.penup()
            self.snake_segment.setposition(position)
            self.segments.append(self.snake_segment)
