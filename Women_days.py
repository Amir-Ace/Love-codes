import turtle
import math
import time

# تنظیمات صفحه
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Women's Day")
screen.setup(width=800, height=600)
screen.tracer(0)

# رسم گلبرگ با منحنی لوگاریتمی
def draw_petal(t, radius, angle, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)
    t.end_fill()

# رسم گل کامل با انیمیشن چند گلبرگ
def draw_flower(t, petals, radius, angle, colors):
    for i in range(petals):
        t.penup()
        t.goto(0,0)
        t.setheading(i * (360 / petals))
        t.forward(radius)
        t.pendown()
        draw_petal(t, radius, angle, colors[i % len(colors)])
        screen.update()
        time.sleep(0.1)

# رسم ساقه
def draw_stem(t):
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.color("green")
    t.width(10)
    t.setheading(90)
    t.forward(200)

# نوشتن پیام تبریک به صورت تدریجی
def write_message(t, message, x, y):
    t.penup()
    t.goto(x,y)
    t.color("pink")
    t.write("", align="center", font=("Arial", 24, "bold"))
    t.pendown()
    for char in message:
        t.write(char, align="center", font=("Arial", 24, "bold"))
        time.sleep(0.2)
        t.clear()
        t.penup()
        t.goto(x,y)
        t.pendown()
    t.write(message, align="center", font=("Arial", 24, "bold"))

# اجرای برنامه
def main():
    flower = turtle.Turtle()
    flower.speed(0)
    flower.hideturtle()
    
    stem = turtle.Turtle()
    stem.speed(0)
    stem.hideturtle()
    
    message_pen = turtle.Turtle()
    message_pen.hideturtle()
    message_pen.speed(0)
    
    draw_stem(stem)
    draw_flower(flower, petals=8, radius=100, angle=60, colors=["magenta","pink","red","purple"])
    write_message(message_pen, "Happy Women's Day", 0, 180)
    
    screen.mainloop()

if __name__ == "__main__":
    main()


#Produce by AmirHossein Taghizadeh
