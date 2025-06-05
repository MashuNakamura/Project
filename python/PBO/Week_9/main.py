import tkinter as t
from window import PBOTestApp

if __name__ == "__main__":
    root = t.Tk()
    root.geometry("500x300")
    app = PBOTestApp(root)
    root.mainloop()