from tkinter import *
from tkinter import ttk
import random

class GUI:
    def __init__(self, master=None):

        #Master Window 
        master.geometry('640x480')

        master.resizable(False, False)
        menubar = Menu(master)
        master.config(menu=menubar)
        file = Menu(menubar)
        settings = Menu(menubar)

        # Cascades
        menubar.add_cascade(menu=file, label='File')
        menubar.add_cascade(menu=settings, label='Settings')

        # File Menu
        file.add_command(label='Open')
        file.add_command(label='Save')
        file.add_command(label='Save as')

        # Settings Menu

        # Resolution Menu
        res = Menu(settings)
        settings.add_cascade(menu=res, label='Resolution')
        res.add_command(label='480x360', command=lambda: self.change_resolution('1', master))
        res.add_command(label='640x480', command=lambda: self.change_resolution('2', master))
        res.add_command(label='1280x720', command=lambda: self.change_resolution('3', master))
        res.add_command(label='1600x900', command=lambda: self.change_resolution('4', master))
        res.add_command(label='Custom')

        # Colour Menu

        colour = Menu(settings)
        settings.add_cascade(menu=colour, label="Colour")
        colour.add_command(label='First', command=lambda: self.change_colour('1', master))
        colour.add_command(label='Second', command=lambda: self.change_colour('2', master))
        colour.add_command(label='Third', command=lambda: self.change_colour('3', master))
        colour.add_command(label='Custom')#, command = lambda: self.change_colour())

        # Window Frames

        frame_dice = ttk.Frame(master)
        frame_dice.config(height=150, width=640)
        frame_dice.place(x=640, anchor='ne')
        
        frame_history = ttk.Frame(master)
        frame_history.config(height=330, width=150)
        frame_history.place(relx=0, rely=0.3)

        frame_main = ttk.Frame(master)
        frame_main.config(height=200, width=200)
        frame_main.place(relx=0.3, rely=0.3)


        

    
    
    def rolldice(self, range):
        return random.randrange(range)
    def change_resolution(self, res, master):
        if res == '1':
            master.geometry('480x360')
        elif res == '2':
            master.geometry('640x480')
        elif res == '3':
            master.geometry('1280x720')
        elif res == '4':
            master.geometry('1600x900')
    def change_colour(self, colour, master):
        if colour == '1':
            master.config(background = 'red')
        elif colour == '2':
            master.config(background = 'white')
        elif colour == '3':
            master.config(background = 'green')
        else:
            master.config(background = 'black')

def main():            
    
    root = Tk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__": main()