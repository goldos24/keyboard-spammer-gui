import keyboard
from tkinter import *

def spam(start_key : str, msg : str, n : int):
    keyboard.wait(start_key)
    for i in range(n):
        keyboard.write(msg + '\n')

window : Tk = Tk()

start_key : str = "Ctrl"
message : str = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
amount_of_messages : int = 100

start_key_label : Label = Label(window, text="Enter key to press to unload the spam messages: ")
start_key_label.grid(column=0, row=0)
start_key_input_field : Entry = Entry(window, width=10)
start_key_input_field.grid(column=1, row=0)
start_key_input_field.insert(0, start_key)

message_label : Label = Label(window, text="Enter spam message: ")
message_label.grid(column=0, row=2)
message_input_field : Entry = Entry(window, width=100)
message_input_field.grid(column=1, row=2)
message_input_field.insert(0, message)

amount_label : Label = Label(window, text="Enter the amount of spam messages: ")
amount_label.grid(column=0, row=3)
amount_input_field : Entry = Entry(window, width=10)
amount_input_field.grid(column=1, row=3)
amount_input_field.insert(0, str(amount_of_messages))

def startSpam():
    start_key = start_key_input_field.get()
    message = message_input_field.get()
    amount_of_messages = int(amount_input_field.get())
    spam(start_key, message, amount_of_messages)

ready_button : Button = Button(window, text="Start Spamming!", command=startSpam)
ready_button.grid(column=0, row=5)

window.mainloop()
