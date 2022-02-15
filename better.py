import tkinter as tk
from tkinter import ttk

chosen = None

def bet_turtle():
    root = tk.Tk()
    root.title("Make your bet")
    root.geometry("310x132")
    root.resizable(False, False)

    txt = ttk.Label(root, text="Which turtle will win the race? Enter a color ", padding=10)
    txt.grid(row=0, columnspan=2, sticky='ewns')
    # txt.config(font=("Helvetica", 11))

    colors = [("red", "orange"), ("yellow", "green"), ("blue", "purple")]
    for row in range(3):
        for col in range(2):
            def wrapper(param):
                def inner():
                    global chosen
                    chosen = param
                    root.destroy()
                return inner
            color_picker = wrapper(colors[row][col])

            tk.Button(
                root,
                text=str(colors[row][col]).upper(),
                background=colors[row][col],
                command=color_picker
            ).grid(row=row+1, column=col, sticky="ewns")

    root.mainloop()

    return chosen


# print(bet_turtle())
