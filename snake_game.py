import random
import turtle
import time

# إعداد نافذة اللعبة
screen = turtle.Screen()
screen.title("Snake Game with Hamza El Asly")
screen.bgcolor("orange")
s_width, s_height = 600, 600
screen.setup(width=s_width, height=s_height)
screen.tracer(0)

# النتيجة
score = 0
high_score = 0
delay=0

# إعداد رأس الثعبان
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# جسم الثعبان
snake = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-290,270)
pen.write("Score: 0  High Score: 0", font=("Courier", 20, "normal"))

# إعداد الطعام
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(  random.randint(-s_width//2 + 20, s_width//2 - 20) ,
            random.randint(-s_height//2 + 20, s_height//2 - 20)
          )

#  التحكم
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# ربط مفاتيح التحكم
screen.listen()
screen.onkeypress(go_up, "z")
screen.onkeypress(go_down, "x")
screen.onkeypress(go_left, "q")
screen.onkeypress(go_right, "d")

# اللعبة الرئيسية
while True:
    screen.update()
    # فحص الاصطدام مع حواف الشاشة
    if (head.xcor() > s_width//2 - 10 or head.xcor() < -s_width//2 + 10 or
        head.ycor() > s_height//2 - 10 or head.ycor() < -s_height//2 + 10):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score),font=("Courier", 20, "normal")) 
   
    # فحص اصطدام الثعبان مع نفسه
    for segment in snake:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in snake:
                segment.goto(1000, 1000)
            snake.clear()
            score = 0
            # Reset the delay
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score),font=("Courier", 20, "normal")) 

            
    # فحص إذا أكل الثعبان الطعام
    if head.distance(food) < 20:
        # نقل الطعام إلى مكان جديد
        x = random.randint(-s_width//2 + 20, s_width//2 - 20)
        y = random.randint(-s_height//2 + 20, s_height//2 - 20)
        food.goto(x, y)
        
        # إضافة قطعة جديدة لجسم الثعبان
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("grey")
        new_body.penup()
        snake.append(new_body)
        
        delay -= 0.001
        # Incrementation dyal score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score),font=("Courier", 20, "normal")) 


    # تحريك جسم الثعبان
    for index in range(len(snake) - 1, 0, -1):
        x = snake[index - 1].xcor()
        y = snake[index - 1].ycor()
        snake[index].goto(x, y)

    if len(snake) > 0:
        x = head.xcor()
        y = head.ycor()
        snake[0].goto(x, y)
    move()
    
    time.sleep(0.1)

# __________________________ Game Snake with Curses __________________________

# import random
# import curses
# screen = curses.initscr()
# curses.curs_set(0)
# s_height , s_width =screen.getmaxyx()
# window = curses.newwin(s_height , s_width , 0 , 0)
# window.keypad(0)
# window.timeout(125)
# snk_x = s_height //2
# snk_y = s_width // 2
# snake = [
#     [snk_x , snk_y],
#     [snk_x , snk_y -1],
#     [snk_x , snk_y -2]
# ]
# food = [s_height //5 ,s_width // 3]
# window.addch(food[0],food[1], curses.ACS_PI)
# key = curses.KEY_RIGHT
# while True:
#     next_Key = window.getch()
#     if next_Key == -1 :
#         key = key  
#     else :
#         key = next_Key
#     if snake[0][0] in [0 , s_height] or  snake[0][0] in [0 , s_width] or snake[0] in snake[1 : ] :
#         curses.endwin()
#         quit()
#     new_Head = [ snake[0][0] , snake[0][1] ]
#     if key == curses.KEY_UP :
#         new_Head[0] =1
#     if key == curses.KEY_DOWN :
#         new_Head[0] +=1
#     if key == curses.KEY_LEFT :
#         new_Head[1] -=1
#     if key == curses.KEY_RIGHT :
#         new_Head[1] +=1
#     snake.insert(0 , new_Head)
#     if snake[0] ==food :
#         food = None
#         while food is None :
#             new_food = [random.randint(1 , s_height -1) , random.randint( 1 , s_width -1)]
#             if food not in snake :
#                 food = new_food 
#             else :
#                 food = None
#             window.addch(food[0],food[1], curses.ACS_PI)
#     else :
#         tail = snake.pop()
#         window.addch(tail[0] , tail[1] , ' ')
#     window.addch( snake[0][0], snake[0][1] , curses.ACS_PI)
    
