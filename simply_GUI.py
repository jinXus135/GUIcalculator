from tkinter import *

class MyFirstGui:
    def __init__(self,master):
        self.master = master
        master.title("a simple GUI")

        self.label = Label(master , text = "this is my second GUI")
        self.label.pack()

        self.greet_button = Button(master, text = 'greet', command = self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text = "close", command = master.quit)
        self.close_button.pack()

    def greet(self):
        print("whats up man!")

root = Tk()
gui = MyFirstGui(root)
root.mainloop()