from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#40A578"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_checkmark.config(text="")
    button_reset.grid_remove()
    button_start.grid()


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    button_reset.grid(row=3, column=1)
    button_start.grid_remove()

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        label_checkmark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("400x450")


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50), width=5)
label_timer.grid(row=0, column=1)

button_start = Button(text="Start",relief="groove", highlightthickness=0, command=start_timer)
button_start.grid(row=3, column=1)

button_reset = Button(text="Reset", relief="groove",highlightthickness=0, command=reset_timer)


label_checkmark = Label(fg=GREEN, bg=YELLOW, padx=10, pady=10)
label_checkmark.grid(row=2, column=1)

window.mainloop()