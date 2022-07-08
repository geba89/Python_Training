from turtle import Screen, Turtle, update
import time


class Snake:
    def __init__(self):
        self.snake = []
        self.initial_pos = 0.00
        self.last_part = None
        self.head = None
        self.create_snake()
        self.set_head()
    
    def set_head(self):
        self.head = self.snake[0]

    def create_snake(self):
        for _ in range(3):
            new_part = Turtle(shape="square")
            new_part.penup()
            new_part.color("white")
            new_part.setpos(x=(self.initial_pos, 0.00))
            self.initial_pos -= 20.00
            self.snake.append(new_part)

    def increase_snake_size(self):
        last_pos = self.snake[len(self.snake)-1].position()
        last = self.new_snake_part(last_pos)
        self.snake.append(last)
        self.set_last_part()

    def new_snake_part(self, last_pos):
        new_part = Turtle(shape="square")
        new_part.penup()
        new_part.color("white")
        new_part.setpos(last_pos)    
        return new_part

    def follow(self):    
        prev_follower = self.head
        new_position = prev_follower.position()
        self.head.forward(20)   
        for follower in self.snake:
            if follower == self.head:
                continue
            prev_position = follower.position()
            follower.goto(new_position)
            new_position = prev_position

    def turn_right(self):
        self.head.right(90)

    def turn_left(self):
        self.head.left(90)

    def set_last_part(self):
        self.last_part = self.snake[len(self.snake)-1]
        
    def get_head_position(self):
        return self.head.position()