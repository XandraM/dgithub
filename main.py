import tkinter
import random

colours = ['Red', 'Blue', 'Purple', 'Orange', 'White',
           'Green', 'Black', 'Yellow', 'Pink']

score = 0

timeleft = 30

def startGame(event):
    if timeleft == 30:
        countdown()

    nextColour()

def nextColour(event):
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1

    e.delete(e, tkinter.END)

    random.shuffle(colours)
    label.config(fg = str(colours[1]), text = str(colours[0]))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = 'Time left: ' + str(timeleft))
        timeLabel.after(1000, countdown)

root = tkinter.Tk()

root.title('Colour game')

root.geometry('375x200')

instructions = tkinter.Label(root, text = 'Type in the coulor'
                             'of the word, not the word text.',
                                          font=('Halvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text = 'Press enter to start',
                           font=('Helvetica', 12))
scoreLabel.pack()

timeLabel =  tkinter.Label(root, text = 'Time left: ' +
                           str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()
