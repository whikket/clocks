### START CODE BLOCK ###
import tkinter as tk
import tkinter.filedialog 
import time

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self)
        self.withdraw()

class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
       
        bgColor = "#222"
        frColor = "#3BB9FF"#"#38ACEC"
       

        self.grip = tk.Label(self, text="01\n23",font=("Rubik Light", 24))
        self.day  = tk.Label(self, text="0123",font=("Rubik Light", 8))
        self.grip.pack(side="top", fill="y")
        self.day.pack(side="bottom", fill="x")
        self.configure(background=bgColor)
        self.config(highlightbackground=frColor)
        self.config(highlightthickness = "1")
        self.config(highlightcolor=frColor)
        self.grip.configure(background=bgColor)
        self.day.configure(background=bgColor)
        self.grip.configure(foreground=frColor)
        self.day.configure(foreground=frColor)
        # Grab the time to move #
        self.grip.bind("<ButtonPress-1>", self.StartMove)
        self.grip.bind("<ButtonRelease-1>", self.StopMove)
        self.grip.bind("<B1-Motion>", self.OnMotion)
        # middle click to close #
        self.grip.bind("<ButtonRelease-2>", self.close)
        self.updateTime()

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))

    def close(self, event):
        self.master.destroy()
       

    def updateTime(self):
        now = time.strftime("%I\n%M")
        days = time.strftime("%a %d")
        self.grip.configure(text=now)
        self.day.configure(text=days)
        self.after(5000, self.updateTime)

app=App()
app.mainloop()
### END CODE BLOCK ###