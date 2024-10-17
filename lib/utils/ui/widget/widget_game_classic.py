from customtkinter import *
from lib.utils.ui import Color, Font
from lib.utils.ui import Widget_Game_Bombtime_Vertical, Widget_Game_Bombtime_Horizontal
from lib.utils import BombStatus

class Widget_Game_Classic(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        # Setting
        self.widget_width = 300
        self.widget_height = 50
        
        # UI
        self.build_ui()
        self.test_button_ui()
        
    def FixedUpdate(self):
        self.after(10, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        
        self.bar_bombtime = Widget_Game_Bombtime_Vertical(self, self)
        self.bar_bombtime.place(relx = 0.3, rely = 0.5, anchor = CENTER)
    
    def test_button_ui(self):
        self.test_frame_main = CTkFrame(self.frame_main, fg_color = Color().transparent)
        self.test_frame_main.place(relx = 1, rely = 0, anchor = NE)
        self.test_label_bombtime = CTkLabel(self.test_frame_main, text = "Bombtime Bar Debug")
        self.test_label_bombtime.pack()
        self.test_btn_bombtime_green = CTkButton(self.test_frame_main, text = "Green",
                                                 command = lambda : self.bar_bombtime.changeBombColorByStatus(BombStatus.GREEN))
        self.test_btn_bombtime_green.pack()
        self.test_btn_bombtime_yellow = CTkButton(self.test_frame_main, text = "Yellow", 
                                                  command = lambda : self.bar_bombtime.changeBombColorByStatus(BombStatus.YELLOW))
        self.test_btn_bombtime_yellow.pack()
        self.test_btn_bombtime_red = CTkButton(self.test_frame_main, text = "Red", 
                                               command = lambda : self.bar_bombtime.changeBombColorByStatus(BombStatus.RED))
        self.test_btn_bombtime_red.pack()
        self.test_btn_bombtime_defused = CTkButton(self.test_frame_main, text = "Defused", 
                                                   command = lambda : self.bar_bombtime.changeBombColorByStatus(BombStatus.DEFUSED))
        self.test_btn_bombtime_defused.pack()
        self.test_btn_bombtime_explode = CTkButton(self.test_frame_main, text = "Explode", 
                                                   command = lambda : self.bar_bombtime.changeBombColorByStatus(BombStatus.EXPLODE))
        self.test_btn_bombtime_explode.pack()
    
    def highlight(self, label : CTkLabel):
        label.configure(text_color = Color().black, fg_color = Color().white)
    
    def unhighlight(self, label : CTkLabel):
        label.configure(text_color = Color().white, fg_color = Color().transparent)