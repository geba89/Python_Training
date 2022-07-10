from codecs import backslashreplace_errors
from inspect import trace
from turtle import Screen
import paddle
import ball
import time

#setting up screen:
screen = Screen()
screen.screensize(800,600)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)

paddle_one = paddle.Paddle(40)
paddle_one.spawn(350, 0)
paddle_AI = paddle.Paddle(40)
paddle_AI.spawn(-350, 0)



#listen to player actions
screen.tracer(1)
screen.listen()
screen.onkey(paddle_one.move_down, 's')
screen.onkey(paddle_one.move_up, 'w')

#create ball and start game
ball_one = ball.Ball()

#game
game_on = True
ai_score = 0
player_score = 0

while game_on:
    ball_one.move()
    ball_one.bounce_of_paddle(paddle_AI.paddle)
    ball_one.bounce_of_paddle(paddle_one.paddle)
    ball_one.bounce_of_walls()
    # screen.update()
    # time.sleep(0.1)

    if ball_one.ball.xcor() > 380:
        screen.tracer(0)
        ball_one.ball.goto((0.00, 0.00))
        ball_one.x_move = ball_one.x_move * -1
        ai_score += 1
        screen.tracer(1)
    elif ball_one.ball.xcor() < -380:
        screen.tracer(0)
        ball_one.ball.goto((0.00, 0.00))
        ball_one.x_move = ball_one.x_move * -1
        player_score +=1
        screen.tracer(1)
    
    if player_score == 3:
        game_on = False
        print("You won!")
    elif ai_score == 3:
        game_on = False
        print("Game over!")

#exit
screen.exitonclick()
