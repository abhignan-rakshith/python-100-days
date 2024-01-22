import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "serif"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, marks
    reps = 0
    marks = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", font=(FONT_NAME, 25, "bold"))  # Re-setting Timer Text
    label_timer.config(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "normal"))  # Re-setting Title Text
    label_tick.config(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # LONG BREAK: Called when it's the 8th rep
    if reps % 8 == 0:
        label_timer.config(text="Unwind Unleashed", fg=RED, font=(FONT_NAME, 23, "normal"))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        # SHORT BREAK: Called when it's the 2nd/4th/6th rep
        label_timer.config(text="Tea  Break", fg=PINK)
        count_down(short_break_sec)
    else:
        # WORK: Called when it's the 1st/3rd/5th/7th rep
        label_timer.config(text="Flow State", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, marks, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # changing the format of the timer using Dynamic Typing(Python Specific)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks += "✔ "
            label_tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("POMODORO")
window.iconphoto(True, tk.PhotoImage(file="tomato.png"))
window.config(padx=100, pady=50, bg=YELLOW)

# ------------Timer Label------------
label_timer = tk.Label(text="Timer")
label_timer.config(font=(FONT_NAME, 30, "normal"), fg=GREEN, bg=YELLOW)
label_timer.grid(row=0, column=1)

# ------------CANVAS------------
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=my_tomato_img)
timer_text = canvas.create_text(105, 135, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

# ------------Start and Reset Buttons------------

# calls start_timer() when pressed
button_start = tk.Button(text="Start", command=start_timer)
button_start.config(bg=GREEN, highlightthickness=0)
button_start.grid(row=2, column=0)

# calls reset() when pressed
button_start = tk.Button(text="Reset", command=reset_timer)
button_start.config(bg=PINK, highlightthickness=0)
button_start.grid(row=2, column=2)

# ------------tick label------------
label_tick = tk.Label()
label_tick.config(padx=10, pady=10, font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
label_tick.grid(row=3, column=1)

window.mainloop()
