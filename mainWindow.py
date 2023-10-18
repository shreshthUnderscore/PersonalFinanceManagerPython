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
bbg = PhotoImage(file="Images/mainwindow.png")
imgbbg = Canvas(root)
imgbbg.pack(fill="both", expand=True)
imgbbg.create_image(225, 310, image=bbg)

gen_button = Button(root, text="Add Expenses", borderwidth=0, relief=FLAT, font=("Louis George Café bold", 20),bg='#c6f2c8',activebackground='#c6f2c8',fg='#094873') 
imgbbg.create_window(225, 255, window=gen_button, width=320, height= 50)

gen_button = Button(root, text="Add Income", borderwidth=0, relief=FLAT, font=("Louis George Café bold", 20),bg='#c6f2c8',activebackground='#c6f2c8',fg='#094873') 
imgbbg.create_window(225, 385, window=gen_button, width=320, height= 50)

saved_button= Button(root, text="View All Transactions",borderwidth=0, relief=FLAT, font=("Louis George Café bold", 20),bg='#c6f2c8',activebackground='#c6f2c8',fg='#094873')
imgbbg.create_window(225, 520, window=saved_button, width=320, height= 0)


root.mainloop()