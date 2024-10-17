from typing import Any, Tuple
from customtkinter import *
from lib.utils.ui import Color, Font
from lib.utils.function import Game_Statistic

class Widget_Menu_Statistic(CTkFrame):
    def __init__(self, master, mainApp, game_statistic : Game_Statistic, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.game_statistic = game_statistic
        self.callback = None
        
        # Setting
        self.widget_width = 300
        self.widget_height = 50
        
        # UI
        self.build_ui()
        self.bind_mouse_over()
        self.bind_mouse_leave()
        self.bind_mouse_click()
        self.update_value()
        
    def FixedUpdate(self):
        self.after(10, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure((0,2,6), weight = 0)
        self.frame_main.grid_rowconfigure(4, weight = 1)
        self.frame_main.grid_rowconfigure((1,3,5), weight = 0, minsize = 10)
        
        self.label_select_gamemode = CTkLabel(self.frame_main, text = "Game Statistic",
                                    height = 20,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 28),
                                    text_color = Color().white)
        self.label_select_gamemode.grid(row = 0, column = 0, sticky = EW, ipadx = 5, ipady = 5)
        
        self.underline = CTkFrame(self.frame_main,
                                  height = 3,
                                  fg_color = Color().white)
        self.underline.grid(row = 2, column = 0, sticky = EW)
        
        self.frame_statistic = CTkScrollableFrame(self.frame_main, fg_color = Color().transparent,
                                                    height = 250,
                                                    border_color = Color().white,
                                                    border_width = 0,
                                                    corner_radius = 0,
                                                    scrollbar_button_color = Color().white)
        self.frame_statistic.grid_columnconfigure(0, weight = 1)
        self.frame_statistic.grid_rowconfigure((0,1,2,3,4,5), weight = 0)
        self.frame_statistic.grid(row = 4, column = 0, sticky = EW)
        
        self.classic_statistic_title = CTkLabel(self.frame_statistic, text = "Classic",
                                    height = 20,
                                    fg_color = Color().white,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().black)
        self.classic_statistic_title.grid(row = 0, column = 0, sticky = EW, ipadx = 2, ipady = 2)
        
        self.classic_statistic = Widget_Statistic(self.frame_statistic)
        self.classic_statistic.grid(row = 1, column = 0, sticky = EW, padx = 5, pady = 5)
        
        self.challenge_statistic_title = CTkLabel(self.frame_statistic, text = "Challenge",
                                    height = 20,
                                    fg_color = Color().white,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().black)
        self.challenge_statistic_title.grid(row = 2, column = 0, sticky = EW, ipadx = 2, ipady = 2)
        
        self.challenge_statistic = Widget_Statistic(self.frame_statistic)
        self.challenge_statistic.grid(row = 3, column = 0, sticky = EW, padx = 5, pady = 5)
        
        self.notimeleft_statistic_title = CTkLabel(self.frame_statistic, text = "No time left",
                                    height = 20,
                                    fg_color = Color().white,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().black)
        self.notimeleft_statistic_title.grid(row = 4, column = 0, sticky = EW, ipadx = 2, ipady = 2)
        
        self.notimeleft_statistic = Widget_Statistic(self.frame_statistic)
        self.notimeleft_statistic.grid(row = 5, column = 0, sticky = EW, padx = 5, pady = 5)
        
        self.btn_back = CTkLabel(self.frame_main, text = "Back",
                                    height = 20,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.btn_back.grid(row = 6, column = 0, sticky = EW, ipadx = 5, ipady = 5)
    
    def bind_mouse_over(self):
        self.btn_back.bind("<Enter>", lambda event : self.highlight(self.btn_back))
    
    def bind_mouse_leave(self):
        self.btn_back.bind("<Leave>", lambda event : self.unhighlight(self.btn_back))
    
    def bind_mouse_click(self):
        self.btn_back.bind("<Button-1>", lambda event : self.btn_back_callback())
    
    def highlight(self, label : CTkLabel):
        label.configure(text_color = Color().black, fg_color = Color().white)
    
    def unhighlight(self, label : CTkLabel):
        label.configure(text_color = Color().white, fg_color = Color().transparent)
    
    def update_value(self):
        self.game_statistic.json_read_record()
        self.classic_statistic.win = self.game_statistic.record_classic[0]
        self.classic_statistic.lose = self.game_statistic.record_classic[1]
        self.classic_statistic.winrate = self.game_statistic.winrate_classic()
        self.classic_statistic.update_value()
        
        self.challenge_statistic.win = self.game_statistic.record_challenge[0]
        self.challenge_statistic.lose = self.game_statistic.record_challenge[1]
        self.challenge_statistic.winrate = self.game_statistic.winrate_challenge()
        self.challenge_statistic.update_value()
        
        self.notimeleft_statistic.win = self.game_statistic.record_notimeleft[0]
        self.notimeleft_statistic.lose = self.game_statistic.record_notimeleft[1]
        self.notimeleft_statistic.winrate = self.game_statistic.winrate_notimeleft()
        self.notimeleft_statistic.update_value()
    
    def btn_back_callback(self):
        self.destroy()

class Widget_Statistic(CTkFrame):
    def __init__(self, master, win = 0, lose = 0, winrate = 0, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.win = win
        self.lose = lose
        self.winrate = winrate
        
        self.build_ui()
        
    def build_ui(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        
        self.frame_classic = CTkFrame(self, fg_color = Color().transparent)
        self.frame_classic.grid(row = 0, column = 0, sticky = NSEW, padx = 1, ipadx = 10)
        self.frame_classic.grid_columnconfigure(0, weight = 1)
        self.frame_classic.grid_rowconfigure(0, weight = 0)
        
        self.label_total_title = CTkLabel(self.frame_classic, text = "Total :",
                                    height = 10,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.label_total_title.grid(row = 0, column = 0, sticky = W)
        
        self.label_total = CTkLabel(self.frame_classic, text = "0",
                                    height = 10,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.label_total.grid(row = 0, column = 0, sticky = E)
        
        self.label_win_title = CTkLabel(self.frame_classic, text = "Win :",
                                    height = 10,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.label_win_title.grid(row = 1, column = 0, sticky = W)
        
        self.label_win = CTkLabel(self.frame_classic, text = "0",
                                    height = 10,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.label_win.grid(row = 1, column = 0, sticky = E)
        
        self.label_lose_title = CTkLabel(self.frame_classic, text = "Lose :",
                                    height = 10,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.label_lose_title.grid(row = 2, column = 0, sticky = W)
        
        self.label_lose = CTkLabel(self.frame_classic, text = "0",
                                    height = 10,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.label_lose.grid(row = 2, column = 0, sticky = E)
        
        self.label_winrate_title = CTkLabel(self.frame_classic, text = "Winrate :",
                                    height = 10,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.label_winrate_title.grid(row = 3, column = 0, sticky = W)
        
        self.label_winrate = CTkLabel(self.frame_classic, text = "0.00%",
                                    height = 10,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().white)
        self.label_winrate.grid(row = 3, column = 0, sticky = E)
    
    def update_value(self):
        self.label_total.configure(text = f"{self.win + self.lose}")
        self.label_win.configure(text = f"{self.win}")
        self.label_lose.configure(text = f"{self.lose}")
        self.label_winrate.configure(text = f"{self.winrate}")