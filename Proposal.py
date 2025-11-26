import turtle
import time
import math

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#0c0032")
screen.title("خواستگاری ویژه")

# قلم انیمیشن قلب
heart_pen = turtle.Turtle()
heart_pen.speed(0)
heart_pen.hideturtle()

# قلم پیام عاشقانه
message_pen = turtle.Turtle()
message_pen.color("white")
message_pen.hideturtle()
message_pen.speed(0)

# تابع رسم قلب با تنظیم اندازه و موقعیت
def draw_heart(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.setheading(140)
    t.forward(size)
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.0175)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.0175)
    t.forward(size)
    t.end_fill()

# انیمیشن پالس قلب مرکزی
def heartbeat_animation(t, x, y):
    scale = 1.0
    direction = 0.05
    for _ in range(60):
        t.clear()
        draw_heart(t, x, y - 20, 100 * scale, "red")
        scale += direction
        if scale > 1.3 or scale < 1.0:
            direction = -direction
        screen.update()
        time.sleep(0.05)

# نوشتن پیام به صورت تدریجی با افکت تایپ
def typewriter_effect(t, message, x, y, font_size=24):
    t.penup()
    t.goto(x, y)
    t.color("white")
    t.pendown()
    for i in range(len(message) + 1):
        t.clear()
        t.write(message[:i], align="center", font=("Arial", font_size, "bold"))
        time.sleep(0.15)

# پیام‌هایی که نمایش داده می‌شود
messages = [
    "سلام عزیزم...",
    "از وقتی دیدمت دلم پر از امید شد",
    "می‌خوام تا ابد کنارت باشم",
    "با من ازدواج می‌کنی؟ 💍"
]

def main():
    screen.tracer(0)
    # قلب وسط صفحه
    heartbeat_animation(heart_pen, 0, 0)
    screen.update()

    # نمایش پیام‌ها با تایپ تدریجی
    y_pos = 120
    for msg in messages:
        typewriter_effect(message_pen, msg, 0, y_pos, 28)
        y_pos -= 50
        time.sleep(1)

    # قلب‌های کوچک اطراف
    colors = ["#ff4d6d", "#ff1a43", "#ff6680", "#cc0044"]
    positions = [(-200, 100), (200, 100), (-180, -80), (180, -80)]
    heart_pen.color("red")
    for i in range(40):
        heart_pen.clear()
        for pos, color in zip(positions, colors):
            scale = 0.5 + abs(math.sin(i * 0.2)) * 0.5
            draw_heart(heart_pen, pos[0], pos[1], 40 * scale, color)
        screen.update()
        time.sleep(0.07)

    # نگه داشتن صفحه باز
    screen.mainloop()

if __name__ == "__main__":
    main()


#Produce by AmirHossein Taghizadeh
