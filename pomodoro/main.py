from tkinter import *
from tkinter import font
from math import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global timer
    global reps
    reps=0
    window.after_cancel(timer)
    title_text.config(text="TIMER")
    canvas.itemconfig(time_text, text="00:00")
    text_ticks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        countdown(long_break_sec)
        title_text.config(text="LONG BREAK", fg=RED)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
    elif reps%2==0:
        countdown(short_break_sec)
        title_text.config(text="SHORT BREAK", fg=PINK)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
    else:
        countdown(work_sec)
        title_text.config(text="WORK", fg=GREEN)
        window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count): 

    count_min = floor(count/60)
    count_sec = count%60

    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count>=0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = "" 
        for _ in range(floor(reps/2)):
            mark+="✔"
        text_ticks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100,pady=50, bg=YELLOW)

title_text = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
title_text.grid(row=0,column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
time_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,25,"bold"))
canvas.grid(row=1,column=1)

button_start=Button(text="START",command=start_timer, highlightthickness=0)
button_reset=Button(text="RESET", highlightthickness=0, command=reset)

button_start.grid(row=2, column=0)
button_reset.grid(row=2, column=2)

text_ticks=Label(fg=GREEN, bg=YELLOW)
text_ticks.grid(row=3, column=1)

window.mainloop()
