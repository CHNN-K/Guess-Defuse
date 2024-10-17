from customtkinter import *
from lib.utils.ui import Color, Font
from lib.utils import BombStatus

class Widget_Game_Bombtime_Vertical(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None

        self.bar_list = []
        
        self.isPlay_animation_defused = False
        self.isPlay_animation_explode = False
        
        # Setting
        self.widget_width = 30
        self.widget_height = 100
        
        self.bar_width = 20
        self.bar_height = 10
        self.bar_defualt_color = Color().gray
        
        # UI
        self.build_ui()
        
    def FixedUpdate(self):
        self.after(10, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_bar = CTkFrame(self, fg_color = Color().transparent)
        self.frame_bar.grid_columnconfigure(0, weight = 1)
        self.frame_bar.grid_rowconfigure((0,2,4,6,8,10,12,14,16), weight = 0)
        self.frame_bar.grid_rowconfigure((1,3,5,7,9,11,13,15), weight = 0, minsize = 5)
        self.frame_bar.grid(row = 0, column = 0, sticky = NSEW)
        
        for i in range(17):
            if i % 2 == 0:
                bar = CTkFrame(self.frame_bar, fg_color = self.bar_defualt_color, 
                               width = self.bar_width, 
                               height = self.bar_height,
                               corner_radius = 2)
                bar.grid(row = i, column = 0)
                self.bar_list.append(bar)
    
    def highlight(self, label : CTkLabel):
        label.configure(text_color = Color().black, fg_color = Color().white)
    
    def unhighlight(self, label : CTkLabel):
        label.configure(text_color = Color().white, fg_color = Color().transparent)

    def changeBombColorByStatus(self, status : BombStatus):
        self.isPlay_animation_defused = False
        self.isPlay_animation_explode = False
        
        if status == BombStatus.GREEN:
            for bar in self.bar_list:
                if self.bar_list.index(bar) < 3:
                    bar.configure(fg_color = Color().green)
                elif self.bar_list.index(bar)  < 6:
                    bar.configure(fg_color = Color().yellow)
                else:
                    bar.configure(fg_color = Color().red)
                
        elif status == BombStatus.YELLOW:
            for bar in self.bar_list:
                if self.bar_list.index(bar) < 3:
                    bar.configure(fg_color = Color().gray)
                elif self.bar_list.index(bar)  < 6:
                    bar.configure(fg_color = Color().yellow)
                else:
                    bar.configure(fg_color = Color().red)
        
        elif status == BombStatus.RED:
            for bar in self.bar_list:
                if self.bar_list.index(bar) < 3:
                    bar.configure(fg_color = Color().gray)
                elif self.bar_list.index(bar)  < 6:
                    bar.configure(fg_color = Color().gray)
                else:
                    bar.configure(fg_color = Color().red)
        
        elif status == BombStatus.DEFUSED:
            self.isPlay_animation_defused = True
            self.animate_bomb_defused()
        
        elif status == BombStatus.EXPLODE:
            self.isPlay_animation_explode = True
            self.animate_bomb_explode()
    
    def animate_bomb_defused(self, animation_frame = -1):
        def defualt_color():
            for bar in self.bar_list:
                bar.configure(fg_color = Color().gray)
        def full_color():
            for bar in self.bar_list:
                if self.bar_list.index(bar) < 3:
                    bar.configure(fg_color = Color().green)
                elif self.bar_list.index(bar)  < 6:
                    bar.configure(fg_color = Color().yellow)
                else:
                    bar.configure(fg_color = Color().red)
                    
        if not self.isPlay_animation_defused:
            return
        if animation_frame == -1:
            defualt_color()
        if animation_frame == 0:
            self.bar_list[-1].configure(fg_color = Color().red)
        if animation_frame == 2:
            self.bar_list[-2].configure(fg_color = Color().red)
        if animation_frame == 4:
            self.bar_list[-3].configure(fg_color = Color().red)
        if animation_frame == 6:
            self.bar_list[-4].configure(fg_color = Color().yellow)
        if animation_frame == 8:
            self.bar_list[-5].configure(fg_color = Color().yellow)
        if animation_frame == 10:
            self.bar_list[-6].configure(fg_color = Color().yellow)
        if animation_frame == 12:
            self.bar_list[-7].configure(fg_color = Color().green)
        if animation_frame == 14:
            self.bar_list[-8].configure(fg_color = Color().green)
        if animation_frame == 16:
            self.bar_list[-9].configure(fg_color = Color().green)
        if animation_frame == 20:
            defualt_color()
        if animation_frame == 25:
            full_color()
        if animation_frame == 30:
            defualt_color()
        if animation_frame == 35:
            full_color()
        if animation_frame == 40:
            defualt_color()
        if animation_frame == 45:
            full_color()
        if animation_frame == 50:
            defualt_color()
        if animation_frame == 52:
            animation_frame = -1
        self.after(100, lambda : self.animate_bomb_defused(animation_frame + 1))
    
    def animate_bomb_explode(self, animation_frame = -1):
        def defualt_color():
            for bar in self.bar_list:
                bar.configure(fg_color = Color().gray)
        def full_color():
            for bar in self.bar_list:
                bar.configure(fg_color = Color().red)
                
        if not self.isPlay_animation_explode:
            return
        
        if animation_frame == -1:
            defualt_color()
        if animation_frame == 0:
            full_color()
        if animation_frame == 2:
            defualt_color()
        if animation_frame == 4:
            full_color()
        if animation_frame == 6:
            defualt_color()
        if animation_frame == 8:
            full_color()
        if animation_frame == 10:
            defualt_color()
        if animation_frame == 12:
            full_color()
        if animation_frame == 17:
            self.bar_list[0].configure(fg_color = Color().gray)
        if animation_frame == 18:
            self.bar_list[1].configure(fg_color = Color().gray)
        if animation_frame == 19:
            self.bar_list[2].configure(fg_color = Color().gray)
        if animation_frame == 20:
            self.bar_list[3].configure(fg_color = Color().gray)
        if animation_frame == 21:
            self.bar_list[4].configure(fg_color = Color().gray)
        if animation_frame == 22:
            self.bar_list[5].configure(fg_color = Color().gray)
        if animation_frame == 23:
            self.bar_list[6].configure(fg_color = Color().gray)
        if animation_frame == 24:
            self.bar_list[7].configure(fg_color = Color().gray)
        if animation_frame == 25:
            self.bar_list[8].configure(fg_color = Color().gray)
        if animation_frame == 28:
            animation_frame = -1
        self.after(100, lambda : self.animate_bomb_explode(animation_frame + 1))