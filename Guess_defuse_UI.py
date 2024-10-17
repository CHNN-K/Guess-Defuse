from customtkinter import *
from lib.utils import ApplicationConfiguration
from lib.utils.ui import Color, Animate_PressAnykey, Widget_Title_Game, Widget_Menu_Gamemode, Widget_Menu_Main, Widget_Menu_Statistic
from lib.utils.ui import Widget_Game_Classic
from lib.utils.function import Game_Statistic

class MainApp(CTk):
    def __init__(self):
        super().__init__()

        """ Variable """
        self.game_statistic = Game_Statistic()
        
        """ Screen Setting """
        screen_width = 400 
        screen_height = 400
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        self.resizable(False, False)
        
        set_appearance_mode("Dark")

        self.title("Guess Defuse")
        
        self.bind("<Escape>", lambda event : self.destroy())
        
        ApplicationConfiguration().checkDirectoryExist()
        ApplicationConfiguration().create_json_game_statistic()
        ApplicationConfiguration().create_json_game_setting()

        # UI
        self.Page_1()
    
    def FixedUpdate(self):
        self.after(10, self.FixedUpdate)
    
    def Page_1(self):
        self.configure(fg_color = Color().background)
        
        self.game_title = Widget_Title_Game(self, self)
        self.game_title.place(relx = 0.5, rely = 0.4, anchor = CENTER)
        # self.game_title.set_animator_locomotion_callback(self.Menu_main)
        self.game_title.set_animator_locomotion_callback(self.Game_Scene) # Testing Game scene
        
        self.animate_PressAnyKey = Animate_PressAnykey(self, self, 500)
        self.animate_PressAnyKey.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        self.animate_PressAnyKey.set_callback(lambda : self.game_title.animator_locomotion(0.5, 0.3))
    
    def Menu_main(self):
        self.menu_main = Widget_Menu_Main(self, self)
        self.menu_main.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        self.menu_main.set_btn_start_callback(self.Menu_gamemode)
        self.menu_main.set_btn_statistic_callback(self.Menu_statistic)
    
    def Menu_gamemode(self):
        self.menu_gamemode = Widget_Menu_Gamemode(self, self)
        self.menu_gamemode.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    
    def Menu_statistic(self):
        self.game_statistic.json_read_record()
        self.menu_statistic = Widget_Menu_Statistic(self, self, self.game_statistic)
        self.menu_statistic.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
    def Start_Menu(self):
        pass
    
    def Game_Scene(self):
        self.scene_game_classic = Widget_Game_Classic(self, self)
        self.scene_game_classic.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
app = MainApp()
app.mainloop()