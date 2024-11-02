import pages.window_manager as window_manager
from tkinter import *
import user_info
from constants import *

user_info.load_users()

window = Tk()
window.geometry(f'{window_x}x{window_y}')
window.title('Roster')

class callback:
    @staticmethod
    def signup(signup_information):
        user_info.signup(signup_information)
        window_manager.onboard_window.initiate_window(window, callback)

    @staticmethod
    def login(user):
        user_info.login(user)

def start_roster():
    window_manager.start_window.initiate_window(window, callback)

start_roster()

window.mainloop()