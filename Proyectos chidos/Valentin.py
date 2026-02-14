import turtle
import time

mensaje = "Este 14 de febrero...\nQuiero preguntarte algo muy especial 💕\n¿Te gustaría ser mi San Valentín? 💌"

pantalla = turtle.Screen()
pantalla.bgcolor("lavender")

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-250, 50)

for linea in mensaje.split("\n"):
    t.write(linea, font=("Comic Sans MS", 20, "bold"))
    t.goto(-250, t.ycor() - 50)
    time.sleep(1.30)

turtle.done()
