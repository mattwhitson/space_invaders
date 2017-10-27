#Import functions
import turtle
import math

#Global Variables
window_height = 300
window_width = 300
playerspeed = 15
enemyspeed = 15
bulletspeed = 20
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
points = 0


#Basic Enemy
enemy = turtle.Turtle()
enemy.hideturtle()
enemy.penup()
enemy.speed(0)
enemy.setposition(200,200)
enemy.setheading(180)

#player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle

bulletspeed = 20

#define bulletstate
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

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
    #declare bulletstate
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 20
        bullet.setposition(x,y)
        bullet.showturtle()
    
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

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2)+math.pow(t1.ycor() - t2.ycor(),2)) 
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

    #move the bullet
    y = bullet.ycor()
    y +=bulletspeed
    bullet.sety(y)

    #check to see if bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    
    if isCollision(bullet, enemy,):
        #reset bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        #reset enemy
        enemy.setposition(200, 250)
        points = (points + 1)
        score_keeper.undo()
        score_keeper.write((points), False, align="left", font=("Arial",14, "normal"))
        print(points)
            
    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break

if points == 3:
        score_keeper.undo()
        score_keeper.write(("You Won!"), False, align="left", font=("Arial",14, "normal"))



print ("Done")
wn.exitonclick()

