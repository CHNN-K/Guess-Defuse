from customtkinter import *
from lib.utils.ui import Color, Font

class Animate_Locomotion_Widget(CTkFrame):
    def __init__(self, master, ui : CTkFrame, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Variable
        self.ui = ui
        self.moveStep = 0.001    # percentage (0.0-1.0) = (0-100%)
        self.isAnimate = False

        # UI
        self.build_ui()

    def build_ui(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        
        # self.ui.grid(row = 0, column = 0, sticky = NSEW)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure((0,1), weight = 0)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        
        self.label1 = CTkLabel(self.frame_main, text = "Animated Widget")
        self.label1.grid(row = 0, column = 0)
        
    def animator_locomotion(self, stop_relx, stop_rely):
        # Learning https://www.youtube.com/watch?v=vVRrOi5LGSo

        self.isAnimate = True

        posx = float(self.place_info()["relx"])
        posy = float(self.place_info()["rely"])
        dirx = 0
        diry = 0
        
        refreshRate = 1    # ms/times
        precision = len(str(self.moveStep).split(".")[1])

        if (posx == stop_relx and posy == stop_rely):
            self.isAnimate = False
            return

        if (stop_relx > posx):
            dirx = 1
            nextPosX = round(posx + self.moveStep, precision)
            if (nextPosX > stop_relx):
                nextPosX = posx
        else:
            dirx = -1
            nextPosX = round(posx - self.moveStep, precision)
            if (nextPosX < stop_relx):
                nextPosX = posx

        if (stop_rely > posy):
            diry = 1
            nextPosY = round(posy + self.moveStep, precision)
            if (nextPosY > stop_rely):
                nextPosY = posy
        else:
            diry = -1
            nextPosY = round(posy - self.moveStep, precision)
            if (nextPosY < stop_rely):
                nextPosY = posy

        if (posx == nextPosX and posy == nextPosY):
            self.place(relx = nextPosX, rely = nextPosY, anchor = self.place_info()["anchor"])
            self.isAnimate = False
            return

        self.place(relx = nextPosX, rely = nextPosY, anchor = self.place_info()["anchor"])
        
        if (dirx == 1 and diry == 1):
            if (not posx > stop_relx or not posy > stop_rely):
                self.after(refreshRate, lambda : self.animator_locomotion(stop_relx, stop_rely))
        
        elif (dirx == -1 and diry == 1):
            if (not posx < stop_relx or not posy > stop_rely):
                self.after(refreshRate, lambda : self.animator_locomotion(stop_relx, stop_rely))
        
        elif (dirx == 1 and diry == -1):
            if (not posx > stop_relx or not posy < stop_rely):
                self.after(refreshRate, lambda : self.animator_locomotion(stop_relx, stop_rely))
        
        elif (dirx == -1 and diry == -1):
            if (not posx < stop_relx or not posy < stop_rely):
                self.after(refreshRate, lambda : self.animator_locomotion(stop_relx, stop_rely))

        return