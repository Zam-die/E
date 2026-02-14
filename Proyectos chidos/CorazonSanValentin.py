import turtle
import time

NOMBRE = "Eliza"
COLOR_CORAZON = "red"
COLOR_TEXTO = "darkred"

pantalla = turtle.Screen()
pantalla.bgcolor("pink")

t = turtle.Turtle()
t.speed(0)
t.color(COLOR_CORAZON)
t.begin_fill()
t.left(140)
t.forward(180)

for _ in range(200):
    t.right(1)
    t.forward(2)

t.left(120)

for _ in range(200):
    t.right(1)
    t.forward(2)

t.forward(180)
t.end_fill()

t.penup()
t.goto(-180, -50)
t.color(COLOR_TEXTO)
t.write(f"{NOMBRE}, ¿quieres ser mi San Valentín? 💘",
        font=("Arial", 18, "bold"))

turtle.done()
