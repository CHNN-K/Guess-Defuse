from customtkinter import *
from lib.utils.ui import Color, Font

class Widget_Menu_Gamemode(CTkFrame):
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
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure((0,2), weight = 0)
        self.frame_main.grid_rowconfigure(1, weight = 0, minsize = 10)
        
        self.label_select_gamemode = CTkLabel(self.frame_main, text = "Select Gamemode",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 28),
                                    text_color = Color().white)
        self.label_select_gamemode.grid(row = 0, column = 0, sticky = EW, ipadx = 5, ipady = 5)
        
        self.underline = CTkFrame(self.frame_main,
                                  height = 3,
                                  fg_color = Color().white)
        self.underline.grid(row = 1, column = 0, sticky = EW)
        
        self.frame_gamemode_menu = CTkFrame(self.frame_main, fg_color = Color().transparent)
        self.frame_gamemode_menu.grid_columnconfigure(0, weight = 1)
        self.frame_gamemode_menu.grid_rowconfigure((0,2,4,6), weight = 0)
        self.frame_gamemode_menu.grid_rowconfigure((1,3,5), weight = 0, minsize = 5)
        self.frame_gamemode_menu.grid(row = 2, column = 0, sticky = EW)
        
        self.btn_gamemode_classic = CTkLabel(self.frame_gamemode_menu, text = "Classic",
                                    height = 20,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.btn_gamemode_classic.grid(row = 0, column = 0, sticky = EW, ipadx = 5, ipady = 5)
        
        self.btn_gamemode_challenge = CTkLabel(self.frame_gamemode_menu, text = "Challenge",
                                    height = 20,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.btn_gamemode_challenge.grid(row = 2, column = 0, sticky = EW, ipadx = 5, ipady = 5)
        
        self.btn_gamemode_no_time_left = CTkLabel(self.frame_gamemode_menu, text = "No time left",
                                    height = 20,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.btn_gamemode_no_time_left.grid(row = 4, column = 0, sticky = EW, ipadx = 5, ipady = 5)
        
        self.btn_back = CTkLabel(self.frame_gamemode_menu, text = "Back",
                                    height = 20,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.btn_back.grid(row = 6, column = 0, sticky = EW, ipadx = 5, ipady = 5)
    
    def bind_mouse_over(self):
        self.btn_gamemode_classic.bind("<Enter>", lambda event : self.highlight(self.btn_gamemode_classic))
        self.btn_gamemode_challenge.bind("<Enter>", lambda event : self.highlight(self.btn_gamemode_challenge))
        self.btn_gamemode_no_time_left.bind("<Enter>", lambda event : self.highlight(self.btn_gamemode_no_time_left))
        self.btn_back.bind("<Enter>", lambda event : self.highlight(self.btn_back))
    
    def bind_mouse_leave(self):
        self.btn_gamemode_classic.bind("<Leave>", lambda event : self.unhighlight(self.btn_gamemode_classic))
        self.btn_gamemode_challenge.bind("<Leave>", lambda event : self.unhighlight(self.btn_gamemode_challenge))
        self.btn_gamemode_no_time_left.bind("<Leave>", lambda event : self.unhighlight(self.btn_gamemode_no_time_left))
        self.btn_back.bind("<Leave>", lambda event : self.unhighlight(self.btn_back))
    
    def bind_mouse_click(self):
        self.btn_gamemode_classic.bind("<Button-1>", lambda event : self.btn_gamemode_classic_callback())
        self.btn_gamemode_challenge.bind("<Button-1>", lambda event : self.btn_gamemode_challenge_callback())
        self.btn_gamemode_no_time_left.bind("<Button-1>", lambda event : self.btn_gamemode_no_time_left_callback())
        self.btn_back.bind("<Button-1>", lambda event : self.btn_back_callback())
    
    def highlight(self, label : CTkLabel):
        label.configure(text_color = Color().black, fg_color = Color().white)
    
    def unhighlight(self, label : CTkLabel):
        label.configure(text_color = Color().white, fg_color = Color().transparent)
        
    def set_callback(self, callback):
        self.callback = callback
    
    def btn_gamemode_classic_callback(self):
        print("Classic")
        
    def btn_gamemode_challenge_callback(self):
        print("Challenge")
        
    def btn_gamemode_no_time_left_callback(self):
        print("No time Left")
    
    def btn_back_callback(self):
        self.destroy()