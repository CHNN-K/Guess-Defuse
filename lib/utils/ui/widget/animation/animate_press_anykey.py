from customtkinter import *
from lib.utils.ui import Color, Font

class Animate_PressAnykey(CTkFrame):
    def __init__(self, master, mainApp, blinkingTime : float, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        self.blinkingTime = blinkingTime  # Second
        
        # Setting
        self.widget_width = 400
        self.widget_height = 20
        
        # UI
        self.build_ui()
        self.animateProcessText()
        
        self.master.bind("<Key>", lambda event : self.close_widget())
        self.master.bind("<Button-1>", lambda event : self.close_widget())
    
    def build_ui(self):
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        self.configure(fg_color = Color().transparent)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure((0,1), weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0)

        self.frame_text = CTkFrame(self.frame_main, fg_color = Color().transparent)
        self.frame_text.grid_rowconfigure((0,1), weight = 0)
        self.frame_text.grid_columnconfigure(0, weight = 1)
        self.frame_text.grid(row = 0, column = 0)

        self.label_pressAnyKey = CTkLabel(self.frame_text, text = "...Press anykey...",
                                        font = (Font().font_bold, 20),
                                        text_color = Color().white)
        self.label_pressAnyKey.grid(row = 0, column = 0)
    
    def animateProcessText(self):
        if self.label_pressAnyKey.cget("text") == "...Press anykey...":
            self.label_pressAnyKey.configure(text = "")
            timer = self.blinkingTime
        elif self.label_pressAnyKey.cget("text") == "":
            self.label_pressAnyKey.configure(text = "...Press anykey...")
            timer = self.blinkingTime * 2
        self.process_animation_text = self.after(timer, self.animateProcessText)
    
    def set_callback(self, callback):
        self.callback = callback
    
    def close_widget(self):
        if self.callback:
            self.callback()
        
        self.master.unbind("<Key>")
        self.master.unbind("<Button-1>")
        self.grab_release()
        self.destroy()