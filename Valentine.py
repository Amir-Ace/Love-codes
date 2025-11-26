import turtle
import time
import math

# تنظیمات صفحه
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Valentine's Day")
screen.setup(width=800, height=600)
screen.tracer(0)  # برای انیمیشن نرم

# تابع رسم قلب
def draw_heart(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    
    for angle in range(360):
        angle_rad = math.radians(angle)
        r = size * (1 - math.sin(angle_rad))
        x_pos = x + r * math.cos(angle_rad)
        y_pos = y + r * math.sin(angle_rad)
        t.goto(x_pos, y_pos)
    
    t.end_fill()

# تابع رسم قلب متحرک (پالس)
def animate_heart():
    heart = turtle.Turtle()
    heart.hideturtle()
    heart.speed(0)
    heart.penup()
    
    scale = 1.0
    direction = 1
    
    for _ in range(200):  # 200 فریم انیمیشن
        heart.clear()
        scale += 0.02 * direction
        if scale > 1.5:
            direction = -1
        elif scale < 0.8:
            direction = 1
        
        draw_heart(heart, 0, 0, 100 * scale, "red")
        screen.update()
        time.sleep(0.05)

# تابع نوشتن پیام
def write_message():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("white")
    pen.penup()
    
    # پیام اول: I love you
    pen.goto(0, 150)
    for char in "I love you":
        pen.write(char, align="center", font=("Arial", 30, "bold"))
        time.sleep(0.2)
        pen.clear()
        pen.goto(0, 150)
    
    pen.goto(0, 150)
    pen.write("I love you", align="center", font=("Arial", 30, "bold"))
    
    # پیام دوم: Happy Valentine's Day
    pen.goto(0, -200)
    pen.write("Happy Valentine's Day", align="center", font=("Arial", 20, "italic"))

# اجرای برنامه
try:
    animate_heart()
    write_message()
    screen.mainloop()  # صفحه باز بماند
except turtle.Terminator:
    pass


#Produce by AmirHossein Taghizadeh
