from tkinter import *
from module1 import *
import time

def jdpopupWarning():
    popupBonusWindow = Tk()
    popupBonusWindow.wm_title("Warning")
    labelBonus = Label(popupBonusWindow, text = "Warning: Please make sure pump 1 is in vodka, pump 2 is in lemonade, and pump 3 is in iced tea!")
    labelBonus.pack()
    def dual():
        popupBonusWindow.destroy()
        john_daley()
    B1 = Button(popupBonusWindow, text = "Okay", command = dual)
    B1.pack()

def vspopupWarning():
    popupBonusWindow = Tk()
    popupBonusWindow.wm_title("Warning")
    labelBonus = Label(popupBonusWindow, text = "Warning: Please make sure pump 1 is in vodka and pump 2 is in sprite!")
    labelBonus.pack()
    def dual():
        popupBonusWindow.destroy()
        vodka_sprite()  
    B1 = Button(popupBonusWindow, text = "Okay", command = dual)
    B1.pack()


class BTGUI:
    
    def __init__ (self, master):
        
        self.master = master
        master.title("Bartender GUI")
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
   
        self.label = Label(master, text = "Smart Bartender.  Pick a drink below!")
        self.label.pack()

        self.jdbutton = Button(master, text = "John Daley", command = jdpopupWarning)
        self.jdbutton.pack(side = TOP)

        self.vspritebutton = Button(master, text = "Vodka Sprite", command = vspopupWarning)
        self.vspritebutton.pack(side = TOP)
    
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
    

root = Tk()
bartender_gui = BTGUI(root)
root.configure(background = 'red')
root.mainloop()

#let's see if this works

