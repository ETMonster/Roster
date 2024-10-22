from tkinter import *
from pages.constants import *

start_window = Tk()
start_window.geometry(f'{window_x}x{window_y}')
start_window.title('Roster')

header = Frame(master = start_window, width = 512)
body = Frame(master = start_window, width = 512)

# Header
roster_logo_image = PhotoImage(file = 'images/logo_256.png')
roster_logo = Label(master = header, image = roster_logo_image, anchor = 'center')

roster_title = Label(text = 'ROSTER',
                     master = header, font = (title_font, 50), anchor = 'center', fg = primary_color)

horizontal_line_image = PhotoImage(file = 'images/horizontal_line_512.png')
horizontal_line = Label(master = header, image = horizontal_line_image, anchor = 'center')


roster_logo.grid(row = 0, column = 0)
roster_title.grid(row = 2, column = 0)

horizontal_line.grid(row = 3, column = 0, pady = (20, 20))

header.pack()

# Body
subtitle = Label(text = 'Welcome to Roster, your quick and easy matchmaking app!',
                 master = body, font = (body_font, 15), anchor = 'center')

login_title = Label(text = 'Log in',
                    master = body, font = (subtitle_font, 25), anchor = 'center')

login = Frame(master = body)

login_username_label = Label(text = 'Username',
                             master = login, font = (body_font, 12), anchor = 'center')
login_password_label = Label(text = 'Password',
                             master = login, font = (body_font, 12), anchor = 'center')
login_username_entry = Entry(master = login, width = 24, font = (body_font, 12), bg = background_color, bd = 0, highlightthickness = 1, highlightcolor = primary_color)
login_password_entry = Entry(master = login, width = 24, font = (body_font, 12), bg = background_color, bd = 0, highlightthickness = 1, highlightcolor = primary_color, show = '*')

login_submit = Button(text = 'Submit',
                      master = body, font = (body_font, 12), bg = background_color, bd = 0, anchor = 'center',
                      cursor = 'hand2', activebackground = primary_color)


subtitle.grid(row = 0, column = 0)

login_title.grid(row = 1, column = 0, pady = (20, 0))

login.grid(row = 2, column = 0, pady = (10, 0))
login_username_label.grid(row = 0, column = 0, padx = (0, 5))
login_password_label.grid(row = 1, column = 0, padx = (0, 5))
login_username_entry.grid(row = 0, column = 1)
login_password_entry.grid(row = 1, column = 1)

login_submit.grid(row = 3, column = 0, pady = (10, 0))

body.pack()