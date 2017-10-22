#Import functions
import turtle
import math

#Global Variables
window_height = 300
window_width = 300
playerspeed = 15
enemyspeed = 10
collision_threshold = 50

points = 0


#Window Attributes
wn = turtle.Screen()
wn.screensize (window_height, window_width)


#Player attributes
player = turtle.Turtle()
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#The score keeper Attributes
score_keeper = turtle.Turtle()
score_keeper.penup()
score_keeper.ht()
score_keeper.setposition(-250, 250)
score_keeper.write(points, False, align="left", font=("Arial",14, "normal"))

#Basic Enemy
enemy = turtle.Turtle()
enemy.hideturtle()
enemy.penup()
enemy.speed(0)
enemy.setposition(200,200)
enemy.setheading(180)

#player bullet
bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape("triangle")
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)

x = player.xcor()
y = player.ycor()


#Player movement Attributes
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x +=playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    bullet.showturtle()
    x = player.xcor()
    y = player.ycor()
    print(x,y)
    bullet.setposition(x,y + 20)
    bullet.speed(1)
    bullet.forward(500)
    bullet.hideturtle()
    bullet.speed(0)

    
def player_pointX(x1):
    player.xcor()
    return player_pointX

def player_pointY(y1):
    player.ycor()
    return player_pointY

def bullet_pointX(x2):
    bullet.xcor()
    return player_pointX

def bullet_pointY(y2):
    bullet.ycor()
    return player_pointY

def enemy_pointX(x3):
    enemy.xcor()
    return enemy_pointX

def enemy_pointY(y3):
    enemy.ycor()
    return enemy_pointy

def is_collision(turtle1, turtle2):
    d = math.sqrt((turtle2.xcor() - turtle1.xcor())**2 + (turtle2.ycor() - turtle1.ycor())**2) 
    if d < collision_threshold:
        return True
    else:
        return False

def enemy_collision(turtle1, turtle3):
    d = math.sqrt((turtle3.xcor() - turtle1.xcor())**2 + (turtle3.ycor() - turtle1.ycor())**2) 
    if d < collision_threshold:
        return True
    else:
        return False


#User key commands
turtle.listen()		

turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "Up")


#Main game loop
while points < 3:
    enemy.speed(1)
    x = enemy.xcor()
    if x > 280:
        enemy.right(90)
        enemy.forward(30)
        enemy.right(90)
    if x < -280:
        enemy.left(90)
        enemy.forward(30)
        enemy.left(90)
    enemy.showturtle()
    enemy.forward(10)

    
    if is_collision(bullet, enemy): 
            points = (points + 1)
            score_keeper.undo()
            score_keeper.write((points), False, align="left", font=("Arial",14, "normal"))
            
    if enemy_collision (player, enemy):
        score_keeper.undo()
        score_keeper.write(("You Lost!"), False, align="left", font=("Arial",14, "normal"))
        print("Done")	
        wn.exitonclick()

if points == 3:
        score_keeper.undo()
        score_keeper.write(("You Won!"), False, align="left", font=("Arial",14, "normal"))



print ("Done")
wn.exitonclick()
