import tkinter as tk

window = tk.Tk()
window.geometry("640x480")
window.title("First GUI!")

midTitle = tk.Label(window, text="Hello, World!", font="none 18 bold")
midTitle.place(anchor=tk.CENTER, relx = 0.5, rely = 0.5)

window.mainloop()