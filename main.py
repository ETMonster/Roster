from pages.start_window import start_window
import user_info
from constants import *

user_info.load_users()

def start_roster():
    start_window.mainloop()
    #user_info.create_new_user(attempt_signup_information)

start_roster()