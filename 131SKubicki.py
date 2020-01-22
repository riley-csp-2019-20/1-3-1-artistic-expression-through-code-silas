import turtle as trtl
from playsound import playsound
import winsound
#variables
sound = trtl.Turtle()
sound.pensize(5)


harp = "harp.mp3"

#playsound('/path/to/a/sound/file/you/want/to/play.mp3')
def note1():
    winsound.PlaySound("harp.mp3", winsound.SND_ALIAS)
    sound.penup()
    sound.goto(0,0)
    sound.pendown()
    sound.pencolor("blue")
    sound.circle(20)

def note2():
    winsound.PlaySound("", winsound.SND_ALIAS)
    sound.penup()
    sound.goto(0,0)
    sound.pendown()
    sound.pencolor("red")
    sound.circle(20)

def note3():
    winsound.PlaySound("", winsound.SND_ALIAS)
    sound.penup()
    sound.goto(0,0)
    sound.pendown()
    sound.pencolor("green")
    sound.circle(20)

def note4():
    winsound.PlaySound("", winsound.SND_ALIAS)
    sound.penup()
    sound.goto(0,0)
    sound.pendown()
    sound.pencolor("yellow")
    sound.circle(20)

def note5():
    winsound.PlaySound("", winsound.SND_ALIAS)
    sound.penup()
    sound.goto(0,0)
    sound.pendown()
    sound.pencolor("orange")
    sound.circle(20)

def note6():
    winsound.PlaySound("", winsound.SND_ALIAS)
    sound.penup()
    sound.goto(0,0)
    sound.pendown()
    sound.pencolor("purple")
    sound.circle(20)

def clear():
    sound.clear()


wn = trtl.Screen()
wn.onkeypress( note1, "1")
wn.onkeyrelease(clear, "1")
wn.onkeypress( note2, "2")
wn.onkeyrelease(clear, "2")
wn.onkeypress( note3, "3")
wn.onkeyrelease(clear, "3")
wn.onkeypress( note4, "4")
wn.onkeyrelease(clear, "4")
wn.onkeypress( note5, "5")
wn.onkeyrelease(clear, "5")
wn.onkeypress( note6, "6")
wn.onkeyrelease(clear, "6")
wn.listen()
wn.mainloop()