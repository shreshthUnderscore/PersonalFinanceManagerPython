from tkinter import *
import sqlite3

root = Tk()
root.title("Finance Manager")
#root.iconbitmap("icon.ico")
w_screen = 450
h_screen = 620
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


x_cor = (screen_width / 2) - (w_screen / 2)
y_cor = (screen_height / 2) - (h_screen / 2)

root.geometry("%dx%d+%d+%d" % (w_screen, h_screen, x_cor, y_cor))
root.wm_resizable(width=False, height=False)


bg = PhotoImage(file="Images/signup.png")

imgbg = Canvas(root)
imgbg.pack(fill="both", expand=True)
imgbg.create_image(225, 310, image=bg)

imgbg.create_text(225, 50, text="Name", font=("Louis George Café light", 25),fill="#1566c2")
imgbg.create_text(225, 150, text="Username", font=("Louis George Café light", 25),fill="#1566c2")
imgbg.create_text(225, 250, text="Password", font=("Louis George Café light", 25),fill="#1566c2")

name_value = StringVar()
user_value = StringVar()
pass_value = StringVar()

name_entry = Entry(root, textvariable=name_value, font=("Louis George Café light", 15),justify='center',relief=FLAT, bg="#e5a8c9",) 
user_entry = Entry(root, textvariable=user_value, font=("Louis George Café light", 15),justify='center',relief=FLAT, bg="#e5a8c9")
pass_entry = Entry(root, textvariable=pass_value, font=("Bahnschrift Light", 15),justify='center',relief=FLAT, bg="#e5a8c9",show="*")

imgbg.create_window(225, 100, window=name_entry, height=30, width=250)
imgbg.create_window(225, 200, window=user_entry, height=30, width=250)
imgbg.create_window(225, 300, window=pass_entry, height=30, width=250)

login_button = Button(root, text="LOGIN", command=root.destroy, borderwidth=0, relief=FLAT, font=("Louis George Café Bold", 15),bg='#5dbfe3',activebackground='#5dbfe3',fg='#000000')
imgbg.create_window(225, 555, window=login_button)

login_button.bind("<Return>", root.destroy)

signup_button = Button(root, text="SIGN UP", borderwidth=0, relief=FLAT, font=("Louis George Café Bold", 15),bg='#5dbfe3',activebackground='#5dbfe3',fg='#000000')
imgbg.create_window(225, 485, window=signup_button)

signup_button.bind("<Return>")

root.mainloop()
