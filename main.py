from tkinter import *
import math

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
    app_window.after_cancel(timer)
    timer_label.config(text="timer")
    check_label.config(text="")
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def count_button_func():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down_func(LONG_BREAK_MIN * 60)
        timer_label.config(text="long break", fg=RED)
    elif reps % 2 == 0:
        count_down_func(SHORT_BREAK_MIN * 60)
        timer_label.config(text="break", fg=PINK)
    else:
        count_down_func(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down_func(count):
    count_min = math.floor(count / 60)
    count_sec = round(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = app_window.after(1000, count_down_func, count - 1)
    else:
        count_button_func()
        mark = ""
        if reps % 2 == 0:
            for i in range(int(reps / 2)):
                mark += "✔"
                check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
app_window = Tk()
app_window.title("work finish app")
app_window.minsize(500, 500)
app_window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=2, row=1)
timer_label.config(background=YELLOW, fg=GREEN)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoe_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoe_img)
timer_text = canvas.create_text(100, 125, text="00:00", font=(FONT_NAME, 30, "bold"), fill="White")
canvas.grid(column=2, row=2)

start_button = Button(text='Start', highlightthickness=0, command=count_button_func)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset",command=reset)
reset_button.grid(column=3, row=3)

check_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=2, row=4)

app_window.mainloop()
