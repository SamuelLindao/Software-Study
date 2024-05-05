import customtkinter as ck
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
actualTheme = True
value = []
valueNews = []
def SetTheme():
    plt.clf()

    global value
    oldValue = value

    global valueNews

    value.append(int(typeBox.get()))
    valueNews.append(len(value))
    label = ck.CTkLabel(left, text = typeBox.get())
    label.pack(padx=50, pady=5)

    plt.plot(valueNews, value)
    canvas.draw()
    print("Worked?")

ck.set_appearance_mode("system")


root = ck.CTk()
root.geometry("1280x720")

middle = ck.CTkFrame(root)
left = ck.CTkFrame(root)
right = ck.CTkFrame(root)

fig = plt.figure(figsize = (6,4),dpi=100)
x = np.linspace(0,10,100)
y = np.sin(x)

plt.plot(x,y)
canvas = FigureCanvasTkAgg(fig, master=middle)
canvas.draw()
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

middle.grid_rowconfigure(1, weight=1)
middle.grid_columnconfigure(1, weight=1)

typeBox = ck.CTkEntry(middle)
canvas.get_tk_widget().grid(row =0, column = 1, pady = 50, columnspan = 2)
typeBox.grid(column=1,row=2,sticky="nsew", columnspan=3, pady = 10, padx = 10 )
typeBox.configure(fg_color="#5d5d5d", font=("Arial", 18),height=45, text_color="#c8c8c8")
button = ck.CTkButton(middle, text="Envia Ae", command=SetTheme)
button.grid(column=2, row=2, padx = 20)
button.configure(width=10)
middle.grid(row = 0, column=1, padx=5,sticky="nsew",rowspan=3)
left.grid(row = 0, column=0, padx=5,sticky="nsew",rowspan=3)
right.grid(row = 0, column=2, padx=5,sticky="nsew",rowspan=3)

root.mainloop()