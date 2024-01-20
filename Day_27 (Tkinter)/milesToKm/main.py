from tkinter import *
FONT = ("Arial", 15, "bold")

# Creating the window
window = Tk()
window.title("Miles to Km")
window.config(padx=20, pady=20)
window.iconphoto(True, PhotoImage(file="miles_km.png"))

# Entries
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="1")
entry.grid(row=0, column=1, pady=2)

# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2, pady=2)

# ----------------------------------------------
# Labels
is_equal_label = Label(text="is equal to = ", font=FONT)
is_equal_label.grid(row=1, column=0, pady=2)

# Labels
km_label_o = Label(text="0", font=FONT)
km_label_o.grid(row=1, column=1, pady=2)

# Labels
km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2, pady=2)


# ----------------------------------------------
# Buttons
def calculate():
    miles = entry.get()
    km = round(float(miles) * 1.60934, 3)
    km_label_o.config(text=km)


# calls action() when pressed
button = Button(text="Calculate", command=calculate, font=FONT)
button.config(padx=10, pady=10)
button.grid(row=2, column=1, pady=20)

window.mainloop()
