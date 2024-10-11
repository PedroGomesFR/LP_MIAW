import turtle
import random
import math

# Screen setup
screen = turtle.Screen()
screen.title("Simple FPS Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Player setup
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Weapon (bullet)
bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("yellow")
bullet.penup()
bullet.speed(0)
bullet.hideturtle()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)

# Bullet state (ready to fire or moving)
bullet_speed = 20
bullet_state = "ready"

# Enemy setup
enemy = turtle.Turtle()
enemy.shape("square")
enemy.color("red")
enemy.penup()
enemy.speed(0)
enemy.setposition(random.randint(-300, 300), random.randint(100, 250))

enemy_speed = 2

# Player movement
player_speed = 15

def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)

# Fire the bullet
def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

# Check for bullet collision with enemy
def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False

# Game loop
def game_loop():
    global bullet_state
    
    # Move the enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    # Reverse enemy direction if it hits screen border
    if enemy.xcor() > 380 or enemy.xcor() < -380:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check if the bullet has gone out of screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

    # Check for collision
    if is_collision(bullet, enemy):
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.setposition(0, -400)
        # Reset enemy
        enemy.setposition(random.randint(-300, 300), random.randint(100, 250))
        
    # Call game_loop again
    screen.ontimer(game_loop, 50)

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(fire_bullet, "space")

# Start game loop
game_loop()

# Keep the window open
turtle.done()
