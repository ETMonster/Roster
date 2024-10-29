import pages.window_manager as window_manager
import user_info

def start_roster():
    user_action = window_manager.start_window.initiate_window()

    if user_action[0] == 'Login':
        user_info.login(user_action[1])
    elif user_action[0] == 'Signup':
        user_info.signup(user_action[1])
        onboarding()

def onboarding():
    user_attributes = window_manager.onboard_window.initiate_window()

start_roster()