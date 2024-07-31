import turtle as t
import random as r
import time
import math as m
screen=t.Screen()
screen.setup(1000,700)
a=t.Turtle()
t.speed(0)
t.bgcolor('lightgreen')
a.speed(0)
a.penup()
a.pencolor('red')
a.goto(400,250)
a.pendown()
a.fillcolor('lightblue')
a.begin_fill()
a.goto(-400,250)
a.goto(-400,-300)
a.goto(400,-300)
a.goto(400,250)
a.end_fill()
a.shape('circle')
pc12=t.Turtle()
pc12.speed(0)
pc12.penup()
pc12.shape('turtle')
a.penup()
t.color('blue')
t.shape('turtle')
t.penup()
b=t.Turtle()
b.speed(0)
b.penup()
b.goto(-100,300)
f1=t.Turtle()
f1.speed(0)
f1.penup()
f1.goto(100,300)
f1.pencolor('blue')
f1.write('high score',align='center',font=100)
b.pencolor('yellow')
b.write('current score',align='center',font=100)
f2=t.Turtle()
f2.speed(0)
f2.penup()
f2.goto(100,280)
f2.pencolor('white')
f=t.Turtle()
f.speed(0)
f.penup()
f.goto(-100,280)
f.pencolor('white')
def d1():
    global t
    t.setheading(0)
def w1():
    global t
    t.setheading(90)
def ab1():
    global t
    t.setheading(180)
def s1():
    global t
    t.setheading(270)
d=True
c=0
f3=open('f11.txt')
w=f3.read()
f3.close()
f3=open('f11.txt')
e=r.randint(-375,375),r.randint(-275,225)
a.color('black')
a.goto(e)
a.color('white')
a.pencolor('black')
color='white'
xc=0
ad1=0
time.sleep(1)
pc12.color('red')
end=0
pc12.goto(-375,185)
ds1=False
end1=21
while 2:
    end+=1
    if end==75:
        pc12.color('black')
        pc12.pencolor('red')
        pc12.goto(-375,r.randint(-275,225))
        end=0
        ds1=True
    pc12.clear()
    if ds1:
        end1-=1
        if end==20:
            end1=21
            pc12.color('red')
            ds1=False
    else:
        pc12.fd(10)
    if xc<=5:
        ad1+=0.05
        xc+=.005
    ds=False
    s=t.pos()
    s2=pc12.pos()
    if (m.sqrt((s2[1]-s[1])**2+(s2[0]-s[0])**2))//1<16+ad1:
        if end>20:
            t.goto(0,0)
            pc12.goto(-375,r.randint(-275,225))
            ds=True
    if s[0]>=400-ad1 or s[0]<=-400+ad1 or s[1]>=250-ad1 or s[1]<=-300+ad1:
        t.goto(0,0)
        pc12.goto(0,185)
        ds=True
    if ds:
        c=0
        t.shapesize(1)
        xc=0
        ad1=0
        time.sleep(1)
        f.clear()
    f.write('{}'.format(c),align='center',font=100)
    f2.write('{}'.format(w),align='center',font=100)
    if (m.sqrt((e[1]-s[1])**2+(e[0]-s[0])**2))//1<16+ad1:
        e=r.randint(-375,375),r.randint(-275,225)
        rand=r.randint(1,30)
        if color=='yellow':
            c+=2500
        if color=='blue':
            c+=300
        if color=='red':
            c+=600
        if color=='white':
            c+=100
        a.color('black')
        a.goto(e)
        if rand==4 or rand==20 or rand==26 or rand==18 or rand==11:
            a.color('blue')
            a.pencolor('black')
            color='blue'
        elif rand==24 or rand==12 or rand==30 :
            a.color('red')
            a.pencolor('black')
            color='red'
        elif rand==5:
            drand=r.randint(1,3)
            if drand==2:
                a.color('yellow')
                a.pencolor('black')
                color='yellow'
        else:
            a.color('white')
            a.pencolor('black')
            color='white'
        t.shapesize(1+xc)
        f.clear()
        f2.clear()
        if c>int(w):
            f3.close()
            f3=open('f11.txt','w')
            f3.write('{}'.format(c))
            f3.close()
            f3=open('f11.txt')
            w=f3.read()
    t.fd(10)
    t.onkey(d1, 'd')
    t.onkey(ab1, 'a')
    t.onkey(w1, 'w')
    t.onkey(s1, 's')
    t.listen()
