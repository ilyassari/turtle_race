import tkinter as tk
from tkinter import ttk

chosen = None

def choose_color():
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 310
    height = 132
    pos_x = (screen_width - width) // 2
    pos_y = (screen_height - height) // 2

    root.title("Make your bet")
    root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
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


# print(choose_color())
