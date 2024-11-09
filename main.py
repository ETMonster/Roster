import compatibility
import pages.window_manager as window_manager
from tkinter import *
import user_info
from constants import *
from pages.window_manager import match_window
from user_info import write_users

user_info.load_users()

window = Tk()
window.geometry(f'{window_x}x{window_y}')
window.title('Roster')

class callback:
    @staticmethod
    def start():
        window_manager.start_window.initiate_window(window, callback)

    @staticmethod
    def signup(signup_information):
        user_info.signup(signup_information)
        window_manager.onboard_window.initiate_window(window, callback)

    @staticmethod
    def login(user):
        user_info.login(user)

        for value in user.to_dictionary().values():
            if value is None:
                window_manager.onboard_window.initiate_window(window, callback)

        window_manager.match_window.initiate_window(window, callback)

    @staticmethod
    def change_user_information(user):
        for key, value in user.to_dictionary().items():
            if value is None:
                if key == 'profile_picture_path' and user_info.current_user.profile_picture_path is None:
                    user_info.current_user.profile_picture_path = 'images/profiles/admin.jpg'

                continue

            if key == 'login_information':
                user_info.current_user.login_information.to_object(value)
                continue
            if key == 'compatability_attributes':
                user_info.current_user.compatability_attributes.to_object(value)
                continue

            setattr(user_info.current_user, key, value)

        write_users()

        window_manager.match_window.initiate_window(window, callback)

def start_roster():
    window_manager.start_window.initiate_window(window, callback)

start_roster()

window.mainloop()