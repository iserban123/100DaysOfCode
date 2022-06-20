# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pwd_letters = [random.choice(letters) for _ in range(nr_letters)]
    pwd_symb = [random.choice(symbols) for _ in range(nr_symbols)]
    pwd_num = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list= pwd_letters + pwd_symb + pwd_num
    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char
    entry3.insert(0, password)
    pyperclip.copy(password)
    #print(f"Your password is: {password}")

def search():
    website = entry1.get()
    try:
      with open("data.json", mode="r") as towrite:
        data = json.load(towrite)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No file available")
    else:
          if website in data:
             em = data[website]["email"]
             pwd = data[website]["password"]
             messagebox.showinfo(title=website, message=f"email:{em}\npassword:{pwd}")
          else:
              messagebox.showerror(title="Error", message="Site not in database")
    finally:
            entry1.delete(0, END)

def save():
    entryx=f"{entry1.get()} | {entry2.get()} | {entry3.get()}\n"
    data_dump = {
        entry1.get(): {
            "email": entry2.get(),
            "password": entry3.get(),
        }
    }
    if len(entry1.get()) == 0 or len(entry2.get()) == 0 or len(entry3.get()) == 0 :
        messagebox.showerror(message="Please insert a value")
    else:
       try:
         with open("data.json", mode="r") as towrite:
             data = json.load(towrite)
       except FileNotFoundError as x:
         print(x)
         with open("data.json", mode="w") as towrite:
             json.dump(data_dump, towrite, indent=4)
       else:
           #json.dump(data_dump, towrite, indent=4)

           data.update(data_dump)
           with open("data.json", mode="w") as towrite:
                json.dump(data, towrite, indent=4)
                #print(data)
       finally:
                entry1.delete(0,END)
                entry2.delete(0,END)
                entry2.insert(0, "iuliana.claudia.serban@gmail.com")
                entry3.delete(0,END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(60, 100, image=mypass_img)
canvas.grid(row=0, column=1, columnspan=3)

web = Label(text="Website:")
web.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

pwd = Label(text="Password:")
pwd.grid(row=3, column=0)

entry1 = Entry(width=20)
entry1.grid(row=1, column=1)
entry1.focus()
entry2 = Entry(width=40)
entry2.grid(row=2, column=1, columnspan=2)
entry2.insert(0, "iuliana.claudia.serban@gmail.com")
entry3 = Entry(width=20)
entry3.grid(row=3, column=1, columnspan=1)

search_button = Button(width=15, text="Search", command=search)
search_button.grid(row=1, column=2)

pwd_button = Button(width=15, text="Generate Password", command=generate_pwd)
pwd_button.grid(row=3, column=2)

add_button = Button(width=33, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=3)

window.mainloop()
