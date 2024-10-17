from customtkinter import *
from lib.utils.ui import Color, Font
from lib.utils.function import Game_Statistic

class Widget_Menu_Main(CTkFrame):
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
        self.frame_main_menu.grid_rowconfigure((0,2,4), weight = 0)
        self.frame_main_menu.grid_rowconfigure((1,3), weight = 0, minsize = 5)
        self.frame_main_menu.grid(row = 0, column = 0, sticky = NSEW)
        
        self.btn_start = CTkLabel(self.frame_main_menu, text = "Start Game",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.btn_start.grid(row = 0, column = 0, sticky = EW, ipadx = 5, ipady = 5)
        
        self.btn_statistic = CTkLabel(self.frame_main_menu, text = "Game Statistic",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.btn_statistic.grid(row = 2, column = 0, sticky = EW, ipadx = 5, ipady = 5)
        
        self.btn_exit = CTkLabel(self.frame_main_menu, text = "Exit",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.btn_exit.grid(row = 4, column = 0, sticky = EW, ipadx = 5, ipady = 5)
    
    def bind_mouse_over(self):
        self.btn_start.bind("<Enter>", lambda event : self.highlight(self.btn_start))
        self.btn_statistic.bind("<Enter>", lambda event : self.highlight(self.btn_statistic))
        self.btn_exit.bind("<Enter>", lambda event : self.highlight(self.btn_exit))
    
    def bind_mouse_leave(self):
        self.btn_start.bind("<Leave>", lambda event : self.unhighlight(self.btn_start))
        self.btn_statistic.bind("<Leave>", lambda event : self.unhighlight(self.btn_statistic))
        self.btn_exit.bind("<Leave>", lambda event : self.unhighlight(self.btn_exit))
    
    def bind_mouse_click(self):
        self.btn_start.bind("<Button-1>", lambda event : self.btn_start_callback())
        self.btn_statistic.bind("<Button-1>", lambda event : self.btn_statistic_callback())
        self.btn_exit.bind("<Button-1>", lambda event : self.btn_exit_callback())
    
    def highlight(self, label : CTkLabel):
        label.configure(text_color = Color().black, fg_color = Color().white)
    
    def unhighlight(self, label : CTkLabel):
        label.configure(text_color = Color().white, fg_color = Color().transparent)
        
    def set_callback(self, callback):
        self.callback = callback
    
    def btn_start_callback(self):
        print("Start")
        
    def btn_statistic_callback(self):
        print("Statistic")
        
    def btn_exit_callback(self):
        self.master.destroy()
    
    def set_btn_start_callback(self, callback):
        self.btn_start_callback = callback
        
    def set_btn_statistic_callback(self, callback):
        self.btn_statistic_callback = callback