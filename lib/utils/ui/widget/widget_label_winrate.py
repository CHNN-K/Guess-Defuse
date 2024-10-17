from customtkinter import *
from lib.utils.ui import Color, Font
from lib.utils.function import Game_Statistic

class Widget_Label_Winrate(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        # Setting
        self.widget_width = 300
        self.widget_height = 25
        
        # UI
        self.build_ui()
        self.bind_mouse_over()
        self.bind_mouse_leave()
        self.bind_mouse_click()
        
    def FixedUpdate(self):
        self.after(10, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main_menu = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main_menu.grid_columnconfigure(0, weight = 1)
        self.frame_main_menu.grid_rowconfigure(0, weight = 0)
        self.frame_main_menu.grid(row = 0, column = 0, sticky = EW)
        
        self.label_winrate = CTkLabel(self.frame_main_menu, text = "Winrate : 100.00%",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.label_winrate.grid(row = 0, column = 0, sticky = EW, ipadx = 5, ipady = 5)
    
    
    def bind_mouse_over(self):
        self.label_winrate.bind("<Enter>", lambda event : self.highlight(self.label_winrate))
    
    def bind_mouse_leave(self):
        self.label_winrate.bind("<Leave>", lambda event : self.unhighlight(self.label_winrate))
    
    def bind_mouse_click(self):
        self.label_winrate.bind("<Button-1>", lambda event : self.label_winrate_callback())
        
    def highlight(self, label : CTkLabel):
        label.configure(text_color = Color().black, fg_color = Color().white)
    
    def unhighlight(self, label : CTkLabel):
        label.configure(text_color = Color().white, fg_color = Color().transparent)
    
    def label_winrate_callback(self):
        print("Click")
        pass