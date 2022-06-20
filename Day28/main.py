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

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
# ---------------------------- UI SETUP ------------------------------- #
def start_timer():
    global reps
    reps +=1
    if reps % 2 == 1:
      count_down(WORK_MIN * 1)
      timer_label.config(text="Work", fg=RED)
    elif reps % 2 == 0 and reps < 8:
      count_down(SHORT_BREAK_MIN * 6)
      timer_label.config(text="BREAK", fg=PINK)
    elif reps == 8:
      count_down(LONG_BREAK_MIN * 6)
      timer_label.config(text="BREAK", fg=GREEN)

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        x = ""
        work_ses= math.floor(reps/2)
        for _ in range(work_ses):
            x += "✔"
        check_label.config(text=x)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(fg=GREEN, font=(FONT_NAME, 12, "bold"))
check_label.grid(row=3, column=1)


window.mainloop()