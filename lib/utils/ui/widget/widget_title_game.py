from customtkinter import *
from lib.utils.ui import Color, Font
from lib.utils import __version__

class Widget_Title_Game(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        self.animator_locomotion_callback = None
        
        # Setting
        self.widget_width = 300
        self.widget_height = 50
        
        # UI
        self.build_ui()
        
    def FixedUpdate(self):
        self.after(10, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        
        self.label_game_title = CTkLabel(self.frame_main, text = "Guess Defuse",
                                        height = 50,
                                        fg_color = Color().white,
                                        font = (Font().font_bold, 40),
                                        text_color = Color().black)
        self.label_game_title.grid(row = 0, column = 0, sticky = EW, ipadx = 10)
        
        self.lower_border = CTkFrame(self.frame_main, fg_color = Color().transparent,
                                     border_width = 1,
                                     border_color = Color().white,
                                     corner_radius = 0)
        self.lower_border.grid(row = 1, column = 0, sticky = EW, ipadx = 5, ipady = 5)
        self.lower_border.grid_rowconfigure(0, weight = 1)
        self.lower_border.grid_columnconfigure(0, weight = 1)
        
        self.label_version = CTkLabel(self.lower_border, text = f"{__version__}",
                                    height = 20,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 12),
                                    text_color = Color().white)
        self.label_version.grid(row = 0, column = 0, sticky = E, padx = 5)
    
    def set_callback(self, callback):
        self.callback = callback
    
    def animator_locomotion(self, stop_relx, stop_rely):
        self.isAnimate = True
        self.moveStep = 0.0005    # percentage (0.0-1.0) = (0-100%)

        posx = float(self.place_info()["relx"])
        posy = float(self.place_info()["rely"])
        dirx = 0
        diry = 0
        
        refreshRate = 1    # ms/times
        precision = len(str(self.moveStep).split(".")[1])

        if (posx == stop_relx and posy == stop_rely):
            self.isAnimate = False
            
            if self.animator_locomotion_callback:
                self.animator_locomotion_callback()
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
            
            if self.animator_locomotion_callback:
                self.animator_locomotion_callback()
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
    
    def set_animator_locomotion_callback(self, callback):
        self.animator_locomotion_callback = callback