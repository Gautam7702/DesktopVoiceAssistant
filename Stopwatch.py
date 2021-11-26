from math import inf
import turtle
import time

startV =1
def func():
    global startV 
    startV =0




def start ():
        # A screen is created
    wn  = turtle.Screen()
    wn  = turtle.Screen()
    wn.listen()
    wn.onkeypress(func,"0")
    wn.title("Stop Watch")
    wn.bgcolor("white")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    # A pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("black")
    pen.penup()
    pen.goto(-250,-70)
    pen.write(arg="00 : 00 : 00", align="left", font=("Comic Sans MS", 100, "normal"))
    pen.hideturtle()
    hour =0
    second = 0
    minute = 0
    global startV
    # Next pen
    pen2 = turtle.Turtle()
    pen2.speed(0)
    pen2.color("black")
    pen2.penup()
    pen2.goto(-50,-150)
    pen2.write(arg="Press 0 to quit ", align="left", font=("Courier", 10, "normal"))
    pen2.hideturtle()
    wn.update()
    while startV:

        pen.clear()
        pen.write(f"{hour} : {minute} : {second}", align="left", font=("Comic Sans MS", 100, "normal"))
        time.sleep(1) 
        second+=1
        if second > 59:
            second = 0
            minute+=1
        if minute>59:
            hour +=1
            second =0
            minute = 0
    wn.bye()