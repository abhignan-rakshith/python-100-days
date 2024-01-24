from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = "serif"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def find_password():
    website = entry_website.get()
    if len(website) != 0:
        try:
            with open(file="C:/Users/abhig/Documents/imp/pass_bank.json", mode='r') as pass_file:
                data = json.load(pass_file)
        except FileNotFoundError:
            messagebox.showerror(title='FileNotFoundError', message="No Data File Found.")
        else:
            try:
                website_dict = data[website]
            except KeyError:
                messagebox.showerror(title='Website Not Found!', message="No details for the website exists.")
            else:
                messagebox.showinfo(title=website, message=f"Email: {website_dict['Email']} \n"
                                                           f"Password: {website_dict['Password']} \n")
                pyperclip.copy(website_dict['Password'])
        finally:
            entry_website.delete(0, END)
            entry_website.focus()


# ---------------------------- ADD PASSWORD ------------------------------- #


def add_password():
    email = entry_email.get()
    website = entry_website.get()
    pass_gen = entry_password.get()

    new_data = {
        website: {
            "Email": email,
            "Password": pass_gen,
        }
    }

    if len(website) == 0 or len(pass_gen) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email} \n"
                                                              f"Password: {pass_gen} \n"
                                                              f"Is it ok to save?")
        if is_ok:
            try:
                with open(file="C:/Users/abhig/Documents/imp/pass_bank.json", mode='r') as pass_file:
                    data = json.load(pass_file)
            except FileNotFoundError:
                with open(file="C:/Users/abhig/Documents/imp/pass_bank.json", mode='w') as pass_file:
                    json.dump(new_data, pass_file, indent=4)
            else:
                data.update(new_data)
                with open(file="C:/Users/abhig/Documents/imp/pass_bank.json", mode='w') as pass_file:
                    json.dump(data, pass_file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_website.focus()
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Bank")
window.iconphoto(True, PhotoImage(file="logo.png"))
window.config(padx=30, pady=50, bg="gray10")

# ------------CANVAS------------ #
canvas = Canvas(width=200, height=200, bg="gray10", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ------------Website------------ #
label_website = Label(text="Website:  ")
label_website.config(font=(FONT_NAME, 15, "normal"), bg="gray10", fg="azure")
label_website.grid(row=1, column=0)

entry_website = Entry(width=20)
entry_website.focus()
entry_website.config(bg="azure", fg="blue4", font=(FONT_NAME, 15, "bold"))
entry_website.grid(row=1, column=1, padx=(0, 10))

# calls find_password() when pressed
button_search = Button(text="Search")
button_search.config(font=(FONT_NAME, 11, "bold"), bg="lemon chiffon", fg="gray10",
                     command=find_password, padx=45)
button_search.grid(row=1, column=2)

# ------------Email/Username------------ #
label_email = Label(text="Email/Username:  ")
label_email.config(font=(FONT_NAME, 15, "normal"), bg="gray10", fg="azure")
label_email.grid(row=2, column=0)

entry_email = Entry(width=35)
entry_email.config(bg="azure", fg="blue4", font=(FONT_NAME, 15, "bold"))
entry_email.insert(END, string="abhignanrakshith@outlook.com")
entry_email.grid(row=2, column=1, columnspan=2, pady=(15, 0))

# ------------Password------------ #
label_password = Label(text="Password:  ")
label_password.config(font=(FONT_NAME, 15, "normal"), bg="gray10", fg="azure")
label_password.grid(row=3, column=0)

entry_password = Entry(width=20)
entry_password.config(bg="azure", fg="blue4", font=(FONT_NAME, 15, "bold"))
entry_password.grid(row=3, column=1, pady=(15, 0), padx=(0, 10))

# calls generate_password() when pressed
button_pass_gen = Button(text="Generate Password")
button_pass_gen.config(font=(FONT_NAME, 11, "bold"), bg="lemon chiffon", fg="gray10", command=generate_password)
button_pass_gen.grid(row=3, column=2, pady=(15, 0))
# ------------Add Entry------------ #
# calls add_password() when pressed
button_add = Button(text="Add", width=36)
button_add.config(font=(FONT_NAME, 12, "bold"), padx=12, bg="chartreuse3", fg="gray10", command=add_password)
button_add.grid(row=4, column=1, columnspan=2, pady=(30, 0))

window.mainloop()
