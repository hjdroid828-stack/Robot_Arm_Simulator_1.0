import tkinter as tk
from PIL import Image, ImageTk


class SplashScreen:

    def __init__(self):

        self.root = tk.Tk()

        self.root.overrideredirect(True)

        image = Image.open("assets/splash.png")
        self.photo = ImageTk.PhotoImage(image)

        width = self.photo.width()
        height = self.photo.height()

        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()

        x = (screen_w - width) // 2
        y = (screen_h - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

        label = tk.Label(self.root, image=self.photo)
        label.pack()

    def show(self):

        self.root.after(2500, self.root.destroy)

        self.root.mainloop()