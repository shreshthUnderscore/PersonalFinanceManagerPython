from tkinter import *
import sqlite3


root = Tk()
root.title("Finance Manager")
#root.iconbitmap("icon.ico")

w_screen = 450
h_screen= 620
screen_width= root.winfo_screenwidth()
screen_height= root.winfo_screenheight()

x_cor= (screen_width/2) - (w_screen/2)
y_cor= (screen_height/2) - (h_screen/2)

root.geometry("%dx%d+%d+%d" % (w_screen,h_screen, x_cor, y_cor))
root.wm_resizable(width=False,height=False)

bg = PhotoImage(file="Images/loginwindow.png")

imgbg = Canvas(root)
imgbg.pack(fill="both", expand=True)
imgbg.create_image(225, 310, image=bg)

imgbg.create_text(225, 150, text="Username", font=("Louis George Café bold", 25),fill="#ffffff" )
imgbg.create_text(225, 270, text="Password", font=("Louis George Café bold", 25),fill="#ffffff" )

user_value = StringVar()
pass_value = StringVar()
                
user_entry= Entry(root, textvariable=user_value, font=("Louis George Café bold",15),justify='center', bg="#00bbcc", relief= FLAT,fg="#000000")
pass_entry= Entry(root, textvariable=pass_value, font=("Bahnschrift Light",15),justify='center',show="*", bg="#00bbcc", relief= FLAT,fg="#000000")

imgbg.create_window(225,200, window=user_entry, height=30, width=200)
imgbg.create_window(225,320, window=pass_entry, height=30, width=200)

root.mainloop()