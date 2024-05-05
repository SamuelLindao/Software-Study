import tkinter
def login():
    print("------------------------")
    print(username_entry.get())
    print(password_entry.get())

window = tkinter.Tk()
window.title('Hello World')
window.geometry('340x440')
window.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')
#pack, place, grid

login_label = tkinter.Label(frame, text = "Login",bg='#333333', fg="#FF3399", font=("Arial",30 ))
username_label = tkinter.Label(frame, text = "Username",bg='#333333', fg="#FFFFFF", font=("Arial",16 ))
username_entry = tkinter.Entry(frame, textvariable=username_label, font=("Arial",16 ))
password_label = tkinter.Label(frame, text = "Password",bg='#333333', fg="#FFFFFF", font=("Arial",16 ))
password_entry = tkinter.Entry(frame, show="*", font=("Arial",16 ))
login_button = tkinter.Button(frame, text = "Login", bg = "#FF3399", fg="#FFFFFF", font=("Arial",16 ), width=20, command=login)


login_label.grid(row=0, column=0,columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=5)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=5)
login_button.grid(row=3, column=0, columnspan=2,pady=5)

frame.pack()
window.mainloop()
