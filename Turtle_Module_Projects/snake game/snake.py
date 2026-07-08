from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.pos = 0 
        self.all_turtles = []
        self.create_snake() # whenever a snake object is made crate_-snake method will automatically be made in init
        self.head = self.all_turtles[0] # after snake object is made the first square will be called head
        
    def create_snake(self):
        
        for i in range(3):      # creates three block for snake to start
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.setpos(-(self.pos),0)
            (self.pos) += 20
            self.all_turtles.append(tim)
            
    def extend(self):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        last_segment = self.all_turtles[-1]
        tim.goto(last_segment.position())
        self.all_turtles.append(tim)
            
            
    def move(self):        
        for seg in range(len(self.all_turtles) - 1, 0, -1):  # method to move the snake 
            new_x = self.all_turtles[seg - 1].xcor()    # start at lastend at 0 and take -1 steps at atime
            new_y = self.all_turtles[seg - 1].ycor()
            self.all_turtles[seg].setposition(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)  # we made the logic in loop such that only doing anything--
                                          # to the first object the restt follows the first
    
    def reset_snake(self):
        for seg in self.all_turtles:
            seg.goto(1000,1000)
            
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]
        
    
    def up(self):
        if self.head.heading() != DOWN: # we fnid square heading direction and check if its NOT DOWN
            self.head.setheading(UP)    # then we can set head direction UP/90
        
    def down(self):
        
         if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def right(self):
        
         if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    def left(self):
        
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)