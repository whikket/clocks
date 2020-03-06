import tkinter as tk
import tkinter.filedialog 
import time
from pprint import pprint

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self)
        #pprint (vars(self))
        self.withdraw()

class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
        
        bgColor = "#222"
        frColor = "#c00"#"#3BB9FF"#"#38ACEC"
        
        #pprint (vars(self))

        self.grip = tk.Label(self, text="01\n23",font=("Share Tech Mono", 12))
        #self.day  = tk.Label(self, text="0123",font=("Share Tech Mono", 12))
        self.grip.pack(side="top")
        #self.day.pack(side="bottom")
        self.configure(background=bgColor)
        self.config(highlightbackground=frColor)
        self.config(highlightthickness = "2")
        self.config(highlightcolor=frColor)
        self.attributes('-alpha', 0.8)
        self.grip.configure(background=bgColor)
        #self.day.configure(background=bgColor)
        self.grip.configure(foreground=frColor)
        #self.day.configure(foreground=frColor)
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
        #self.destroy()
        

    def updateTime(self):
        h = int(time.strftime("%H"))
        m = int(time.strftime("%M"))
        w = int(time.strftime("%w"))
        d = int(time.strftime("%d"))
        h1 = int(h/10)
        h2 = h%10
        m1 = int(m/10)
        m2 = m%10
        d1 = int(d/10)
        d2 = d%10
        self.grip.configure(text=" %s %s %s %s 0000 %s %s %s "%('{0:04b}'.format(h1),'{0:04b}'.format(h2),'{0:04b}'.format(m1),'{0:04b}'.format(m2),'{0:04b}'.format(w),'{0:04b}'.format(d1),'{0:04b}'.format(d2)))
        #self.day.configure(text="%s %s"%('{0:04b}'.format(m1),'{0:04b}'.format(m2)))
        self.after(5000, self.updateTime)

app=App()
app.mainloop()