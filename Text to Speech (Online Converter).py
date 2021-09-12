import os
from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry('350x350')
root.resizable(0, 0)
root.title('Online Text to Speech Converter')


lf = LabelFrame(root, text="Narrator", font='Arial 20 bold', labelanchor="n", bd=10, fg='white', bg="blue2",
                width=600, height=50, cursor="arrow")
lf.pack(expand=True, fill=BOTH)

Label(lf, text='Enter Text', font='arial 15 bold', fg='blue2', bg='white').place(x=10, y=60)
Msg = StringVar()
entry_field = Entry(lf, textvariable=Msg, width='50')
entry_field.place(x=10, y=100)


def Text_to_speech():
    message = entry_field.get()
    speech = gTTS(text=message, lang='en-IN')
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
    os.remove('DataFlair.mp3')


def Exit():
    bye = gTTS(text='Thank you very much.')
    bye.save('Bye.mp3')
    playsound('Bye.mp3')
    os.remove('Bye.mp3')
    root.destroy()


def Reset():
    Msg.set("")


Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, fg='blue2').place(x=40, y=180)
Button(root, text='EXIT', font='arial 15 bold', command=Exit, bg='red2', fg='white').place(x=250, y=270)
Button(root, text='RESET', font='arial 15 bold', command=Reset, fg='blue2').place(x=215, y=180)

root.mainloop()
