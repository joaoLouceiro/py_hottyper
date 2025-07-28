import tkinter as tk

WIDTH = 800
HEIGHT = 600
FONT = "Courier"



class Timer():
    def __init__(self, root) -> None:
        self.root = root
        self.sec = 5
        self.cent = 0
        self.str_len = 0
        self.label = tk.Label(master=root, text=self.__format_label__(), font=(FONT, 40, "bold"))
        self.text_area = tk.Text(master=root, state="disabled")
        self.text_area.bind("<Key>", lambda x: self.key_press())
        self.label.pack()

    def countdown(self) -> None:
        if self.cent == 0:
            self.cent = 99
            self.sec -= 1
        else:
            self.cent -= 1
        self.__update_label__()

        if self.sec > 0 or self.cent > 0:
            self.label.after(10, self.countdown)
        else:
            self.text_area.delete("1.0", "end")
            self.text_area.config(state="disabled")

    def key_press(self):
        str_len = len(self.text_area.get("1.0", "end-1c"))
        if str_len != self.str_len:
            self.str_len = str_len
            self.reset()

    def reset(self) -> None:
        self.sec = 5
        self.cent = 0
        self.__update_label__()

    def start_countdown(self):
        self.text_area.delete("1.0", "end")
        self.str_len = 0
        self.reset()
        self.text_area.config(state="normal")
        self.text_area.pack()
        self.text_area.focus()
        self.countdown()

    def __update_label__(self) -> None:
        self.label.config(text=self.__format_label__())

    def __format_label__(self) -> str:
        return f"{self.__format_time_unit__(self.sec)}:{self.__format_time_unit__(self.cent)}"

    def __format_time_unit__(self, time_unit):
        return time_unit if time_unit > 9 else f"0{time_unit}"



window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("Hot Typer")

window.update_idletasks()
timer = Timer(window)

start_button = tk.Button(window, text="start", command=timer.start_countdown)
start_button.pack()
window.mainloop()



