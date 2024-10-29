from tkinter import *
from tkinter import messagebox
from constants import *
import user_info

callback = ['Action', user_info.User_Login('Username', 'Password')]

# Page functionality
def pack_page():
    roster_logo.grid(row = 0, column = 0)
    roster_title.grid(row = 2, column = 0)

    header.pack()

    subtitle.grid(row = 0, column = 0)

    login_title.grid(row = 1, column = 0, pady = (20, 0))

    login.grid(row = 2, column = 0, pady = (10, 0))
    login_username_label.grid(row = 0, column = 0, padx = (0, 5))
    login_password_label.grid(row = 1, column = 0, padx = (0, 5))
    login_username_entry.grid(row = 0, column = 1)
    login_password_entry.grid(row = 1, column = 1)

    login_submit.grid(row = 3, column = 0, pady = (10, 0))

    signup_title.grid(row = 4, column = 0, pady = (40, 0))

    signup.grid(row = 5, column = 0, pady = (10, 0))
    signup_username_label.grid(row = 0, column = 0, padx = (0, 5))
    signup_password_label.grid(row = 1, column = 0, padx = (0, 5))
    signup_username_entry.grid(row = 0, column = 1)
    signup_password_entry.grid(row = 1, column = 1)

    signup_submit.grid(row = 6, column = 0, pady = (10, 0))

    body.pack()

def invalid_login(reason):
    if reason == 'Character':
        messagebox.showinfo(title = 'Error', message = f'You cannot use the characters {', '.join([f'"  {x}  "' for x in login_prohibited_characters])} in your username or password.')
    elif reason == 'Information':
        messagebox.showinfo(title = 'Error', message = 'Username or password is incorrect.')
    elif reason == 'Length':
        messagebox.showinfo(title = 'Error', message = f'Your username and password must be a minimum of {login_minimum_length} and a maximum of {login_maximum_length} characters long.')
    elif reason == 'Exists':
        messagebox.showinfo(title = 'Error', message = f'Your desired username is already in use.')

def attempt_login():
    global callback

    attempt_login_information = user_info.User_Login(login_username_entry.get(), login_password_entry.get())

    if (len(attempt_login_information.username) < login_minimum_length or len(attempt_login_information.password) < login_minimum_length
    or len(attempt_login_information.username) > login_maximum_length or len(attempt_login_information.password) > login_maximum_length):
        invalid_login('Length')
        return

    for character in login_prohibited_characters:
        if character in attempt_login_information.username or character in attempt_login_information.password:
            invalid_login('Character')
            return

    for user in user_info.users:
        print(vars(user))
        if attempt_login_information.username == user.login_information.username and attempt_login_information.password == user.login_information.password:
            callback = ['Login', user]

            window.destroy()
            return

    invalid_login('Information')
    return

def attempt_signup():
    global callback

    attempt_signup_information = user_info.User_Login(signup_username_entry.get(), signup_password_entry.get())

    if (len(attempt_signup_information.username) < login_minimum_length or len(attempt_signup_information.password) < login_minimum_length
    or len(attempt_signup_information.username) > login_maximum_length or len(attempt_signup_information.password) > login_maximum_length):
        invalid_login('Length')
        return

    for character in login_prohibited_characters:
        if character in attempt_signup_information.username or character in attempt_signup_information.password:
            invalid_login('Character')
            return

    for user in user_info.users:
        if attempt_signup_information.username == user.login_information.username:
            invalid_login('Exists')
            return

    callback = ['Signup', attempt_signup_information]
    window.destroy()

# Window
window = Tk()
window.geometry(f'{window_x}x{window_y}')
window.title('Roster')

header = Frame(master = window, width = 512)
body = Frame(master = window, width = 512)

# Header
roster_logo_image = PhotoImage(master = header, file = 'images/logo_256.png')
roster_logo = Label(master = header, image = roster_logo_image, anchor = 'center')

roster_title = Label(text = 'ROSTER',
                     master = header, font = (title_font, title_font_size), anchor = 'center', fg = primary_color)


# Body
subtitle = Label(text = 'Welcome to Roster, your quick and easy matchmaking app!',
                 master = body, font = (body_font, 15), anchor = 'center')

login_title = Label(text = 'Log in',
                    master = body, font = (subtitle_font, subtitle_font_size), anchor = 'center')


login = Frame(master = body)

login_username_label = Label(text = 'Username',
                             master = login, font = (body_font, body_font_size), anchor = 'center')
login_password_label = Label(text = 'Password',
                             master = login, font = (body_font, body_font_size), anchor = 'center')
login_username_entry = Entry(master = login, width = 24, font = (body_font, body_font_size),
                             bg = background_color, bd = 0, highlightthickness = 1, highlightcolor = primary_color)
login_password_entry = Entry(master = login, width = 24, font = (body_font, body_font_size),
                             bg = background_color, bd = 0, highlightthickness = 1, highlightcolor = primary_color, show = '*')

login_submit = Button(text = 'Submit',
                      master = body, font = (body_font, body_font_size), bg = background_color, bd = 0, anchor = 'center',
                      cursor = 'hand2', activebackground = primary_color, command = attempt_login)


signup_title = Label(text = 'Sign up',
                    master = body, font = (subtitle_font, subtitle_font_size), anchor = 'center')


signup = Frame(master = body)

signup_username_label = Label(text = 'Username',
                             master = signup, font = (body_font, body_font_size), anchor = 'center')
signup_password_label = Label(text = 'Password',
                             master = signup, font = (body_font, body_font_size), anchor = 'center')
signup_username_entry = Entry(master = signup, width = 24, font = (body_font, body_font_size),
                             bg = background_color, bd = 0, highlightthickness = 1, highlightcolor = primary_color)
signup_password_entry = Entry(master = signup, width = 24, font = (body_font, body_font_size),
                             bg = background_color, bd = 0, highlightthickness = 1, highlightcolor = primary_color, show = '*')

signup_submit = Button(text = 'Submit',
                      master = body, font = (body_font, body_font_size), bg = background_color, bd = 0, anchor = 'center',
                      cursor = 'hand2', activebackground = primary_color, command = attempt_signup)


# Configure hover

login_submit.bind('<Enter>', lambda button: widget_hover(login_submit))
signup_submit.bind('<Enter>', lambda button: widget_hover(signup_submit))

login_submit.bind('<Leave>', lambda button: widget_unhover(login_submit))
signup_submit.bind('<Leave>', lambda button: widget_unhover(signup_submit))

pack_page()