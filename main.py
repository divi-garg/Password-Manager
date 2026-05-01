from tkinter import *
from tkinter import messagebox
from random import randint,choice, shuffle
import pyperclip
import json
from click import command


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbol + password_number
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_dict = {
        website:    {
                    "email":email,
                     "password":password,
        },
    }

    if len(email)==0 or len(password)==0 or website ==0:
        messagebox.showwarning(title="Ops", message="Please don't leave any field empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                          f"Password: {password}\n Is it ok to save?")

    if is_ok:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w" ) as data_file:
                json.dump(new_dict,data_file,indent=4)
        else:
            data.update(new_dict)
            with open("data.json",'w')as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            messagebox.showinfo(title="Success",message="You saved your details successfully!")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_label = Label(text="Username/E-mail:")
email_label.grid(row=2,column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"gargdivisha21@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)
password_entry = Entry(width=25)
password_entry.grid(row=3,column=1)


generate_password_button = Button(text="Generate",command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="Add", width=34,command = save_password)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
