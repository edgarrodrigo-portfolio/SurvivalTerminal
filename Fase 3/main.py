import turtle
import random
import time

AMPLADA_FINESTRA = 800
ALTURA_FINESTRA = 700

LIMIT_ESQUERRA = -360
LIMIT_DRETA = 360
LIMIT_SUPERIOR = 300
LIMIT_INFERIOR = -300

VELOCITAT = 20

salut = 100
energia = 100
dies = 0
joc_actiu = True
contador = 0

pantalla = turtle.Screen()
pantalla.title("Survival Prototype millorado")
pantalla.bgcolor("lightyellow")
pantalla.setup(width=AMPLADA_FINESTRA, height=ALTURA_FINESTRA)
pantalla.tracer(0)

hud = turtle.Turtle()
hud.hideturtle()
hud.penup()
hud.color("black")
hud.goto(-380, 320)

def actualitzar_hud():
    hud.clear()
    hud.write(
        f"Salut: {salut}   Energia: {energia}   Dies: {dies}",
        font=("Arial", 14, "bold")
    )

final = turtle.Turtle()
final.hideturtle()
final.penup()
final.color("red")

def mostrar(text):
    final.clear()
    final.goto(0, 0)
    final.write(text, align="center", font=("Arial", 24, "bold"))

marc = turtle.Turtle()
marc.hideturtle()
marc.speed(0)
marc.pensize(3)
marc.penup()
marc.goto(LIMIT_ESQUERRA, LIMIT_SUPERIOR)
marc.pendown()

for _ in range(2):
    marc.forward(LIMIT_DRETA - LIMIT_ESQUERRA)
    marc.right(90)
    marc.forward(LIMIT_SUPERIOR - LIMIT_INFERIOR)
    marc.right(90)

obstacles = [
    (-120, 120, 120, 40),
    (120, 80, 40, 140),
    (-220, -80, 160, 40),
    (60, -140, 180, 40),
    (220, 200, 80, 40),
    (-20, -20, 60, 120),
]

def dibuixar_obstacle(x, y, ample, alt):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(x - ample // 2, y + alt // 2)
    t.pendown()
    t.fillcolor("dimgray")
    t.begin_fill()
    for _ in range(2):
        t.forward(ample)
        t.right(90)
        t.forward(alt)
        t.right(90)
    t.end_fill()

for obs in obstacles:
    dibuixar_obstacle(*obs)

def colisio_obstacles(x, y):
    for obs in obstacles:
        marge = 14
        ox, oy, ample, alt = obs
        esquerra = ox - ample / 2 - marge
        dreta = ox + ample / 2 + marge
        dalt = oy + alt / 2 + marge
        baix = oy - alt / 2 - marge
        if esquerra <= x <= dreta and baix <= y <= dalt:
            return True
    return False

def posicio_valida(x, y):
    if x < LIMIT_ESQUERRA + 15 or x > LIMIT_DRETA - 15:
        return False
    if y < LIMIT_INFERIOR + 15 or y > LIMIT_SUPERIOR - 15:
        return False
    if colisio_obstacles(x, y):
        return False
    return True

jugador = turtle.Turtle()
jugador.shape("turtle")
jugador.color("darkgreen")
jugador.penup()
jugador.goto(-300, 240)

menjars = []

def crear_menjar():
    menjar = turtle.Turtle()
    menjar.shape("circle")
    menjar.shapesize(0.7, 0.7)
    menjar.color("green")
    menjar.penup()

    while True:
        x = random.randint(LIMIT_ESQUERRA + 30, LIMIT_DRETA - 30)
        y = random.randint(LIMIT_INFERIOR + 30, LIMIT_SUPERIOR - 30)
        if posicio_valida(x, y):
            menjar.goto(x, y)
            break

    return menjar

for _ in range(5):
    menjars.append(crear_menjar())

def mou(dx, dy):
    global energia

    if not joc_actiu:
        return

    nou_x = jugador.xcor() + dx
    nou_y = jugador.ycor() + dy

    if posicio_valida(nou_x, nou_y):
        jugador.goto(nou_x, nou_y)
        energia -= 0.3
        if energia < 0:
            energia = 0

def amunt():
    jugador.setheading(90)
    mou(0, VELOCITAT)

def avall():
    jugador.setheading(270)
    mou(0, -VELOCITAT)

def esquerra():
    jugador.setheading(180)
    mou(-VELOCITAT, 0)

def dreta():
    jugador.setheading(0)
    mou(VELOCITAT, 0)

pantalla.listen()
pantalla.onkeypress(amunt, "w")
pantalla.onkeypress(avall, "s")
pantalla.onkeypress(esquerra, "a")
pantalla.onkeypress(dreta, "d")
pantalla.onkeypress(amunt, "Up")
pantalla.onkeypress(avall, "Down")
pantalla.onkeypress(esquerra, "Left")
pantalla.onkeypress(dreta, "Right")

def recolocar_menjar(menjar):
    while True:
        x = random.randint(LIMIT_ESQUERRA + 30, LIMIT_DRETA - 30)
        y = random.randint(LIMIT_INFERIOR + 30, LIMIT_SUPERIOR - 30)
        if posicio_valida(x, y):
            menjar.goto(x, y)
            return

actualitzar_hud()

while joc_actiu:
    pantalla.update()
    time.sleep(0.02)
    contador += 1

    if contador % 250 == 0:
        dies += 1
        energia -= 2
        if energia < 0:
            energia = 0

    for menjar in menjars:
        if jugador.distance(menjar) < 20:
            energia += 12
            if energia > 100:
                energia = 100
            recolocar_menjar(menjar)

    if energia <= 0 and contador % 80 == 0:
        salut -= 5

    if salut < 0:
        salut = 0

    if salut <= 0:
        joc_actiu = False
        mostrar("GAME OVER")

    elif dies >= 15:
        joc_actiu = False
        mostrar("HAS GUANYAT!")

    actualitzar_hud()

pantalla.update()
turtle.done()