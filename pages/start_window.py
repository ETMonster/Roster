from tkinter import *
from constants import *
import user_info

def create_widgets(window, callback):
    def pack_page():
        roster_logo.grid(row=0, column=0)

        header.pack()

        subtitle.grid(row=0, column=0)

        login_title.grid(row=1, column=0, pady=(20, 0))

        login.grid(row=2, column=0, pady=(10, 0))
        login_username_label.grid(row=0, column=0, padx=(0, 5))
        login_password_label.grid(row=1, column=0, padx=(0, 5))
        login_username_entry.grid(row=0, column=1)
        login_password_entry.grid(row=1, column=1)

        login_submit.grid(row=3, column=0, pady=(10, 0))

        signup_title.grid(row=4, column=0, pady=(40, 0))

        signup.grid(row=5, column=0, pady=(10, 0))
        signup_username_label.grid(row=0, column=0, padx=(0, 5))
        signup_password_label.grid(row=1, column=0, padx=(0, 5))
        signup_username_entry.grid(row=0, column=1)
        signup_password_entry.grid(row=1, column=1)

        signup_submit.grid(row=6, column=0, pady=(10, 0))

        body.pack()

    def attempt_login():
        attempt_login_information = user_info.User_Login(login_username_entry.get(), login_password_entry.get())

        if (len(attempt_login_information.username) < login_minimum_length or len(
                attempt_login_information.password) < login_minimum_length
                or len(attempt_login_information.username) > login_maximum_length or len(
                    attempt_login_information.password) > login_maximum_length):
            throw_error('Length')
            return

        for character in login_prohibited_characters:
            if character in attempt_login_information.username or character in attempt_login_information.password:
                throw_error('Character')
                return

        for user in user_info.users:
            if attempt_login_information.username == user.login_information.username and attempt_login_information.password == user.login_information.password:
                callback.login(user)
                return

        throw_error('Information')
        return

    def attempt_signup():
        attempt_signup_information = user_info.User_Login(signup_username_entry.get(), signup_password_entry.get())

        if (len(attempt_signup_information.username) < login_minimum_length or len(
                attempt_signup_information.password) < login_minimum_length
                or len(attempt_signup_information.username) > login_maximum_length or len(
                    attempt_signup_information.password) > login_maximum_length):
            throw_error('Length')
            return

        for character in login_prohibited_characters:
            if character in attempt_signup_information.username or character in attempt_signup_information.password:
                throw_error('Character')
                return

        for user in user_info.users:
            if attempt_signup_information.username == user.login_information.username:
                throw_error('Exists')
                return

        callback.signup(attempt_signup_information)

    header = Frame(master=window, width=512)
    body = Frame(master=window, width=512)

    # Header
    roster_logo_image = PhotoImage(file='images/logo_256.png')
    roster_logo = Label(master=header, image=roster_logo_image, anchor='center')
    roster_logo.image = roster_logo_image

    # Body
    subtitle = Label(text='Welcome to Roster, your quick and easy matchmaking app!',
                     master=body, font=(body_font, 15), anchor='center')

    login_title = Label(text='Log in',
                        master=body, font=(subtitle_font, subtitle_font_size), anchor='center')

    login = Frame(master=body)

    login_username_label = Label(text='Username',
                                 master=login, font=(body_font, body_font_size), anchor='center')
    login_password_label = Label(text='Password',
                                 master=login, font=(body_font, body_font_size), anchor='center')
    login_username_entry = Entry(master=login, width=24, font=(body_font, body_font_size),
                                 bg=background_color, bd=0, highlightthickness=1, highlightcolor=primary_color)
    login_password_entry = Entry(master=login, width=24, font=(body_font, body_font_size),
                                 bg=background_color, bd=0, highlightthickness=1, highlightcolor=primary_color,
                                 show='*')

    login_submit = Button(text='Submit',
                          master=body, font=(body_font, body_font_size), bg=background_color, bd=0, anchor='center',
                          cursor='hand2', activebackground=primary_color, command=attempt_login)

    signup_title = Label(text='Sign up',
                         master=body, font=(subtitle_font, subtitle_font_size), anchor='center')

    signup = Frame(master=body)

    signup_username_label = Label(text='Username',
                                  master=signup, font=(body_font, body_font_size), anchor='center')
    signup_password_label = Label(text='Password',
                                  master=signup, font=(body_font, body_font_size), anchor='center')
    signup_username_entry = Entry(master=signup, width=24, font=(body_font, body_font_size),
                                  bg=background_color, bd=0, highlightthickness=1, highlightcolor=primary_color)
    signup_password_entry = Entry(master=signup, width=24, font=(body_font, body_font_size),
                                  bg=background_color, bd=0, highlightthickness=1, highlightcolor=primary_color,
                                  show='*')

    signup_submit = Button(text='Submit',
                           master=body, font=(body_font, body_font_size), bg=background_color, bd=0, anchor='center',
                           cursor='hand2', activebackground=primary_color, command=attempt_signup)

    # Configure hover

    login_submit.bind('<Enter>', lambda button: widget_hover(login_submit))
    signup_submit.bind('<Enter>', lambda button: widget_hover(signup_submit))

    login_submit.bind('<Leave>', lambda button: widget_unhover(login_submit))
    signup_submit.bind('<Leave>', lambda button: widget_unhover(signup_submit))

    pack_page()