import pages.window_manager as window_manager
import user_info
from constants import *

user_info.load_users()

def start_roster():
    window_manager.start_window.create_window()
    #user_info.create_new_user(attempt_signup_information)

start_roster()