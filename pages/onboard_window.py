from tkinter import *
from constants import *
import user_info

callback = ['First name', 'Last name', 'Profile picture path', user_info.User_Attributes(None, None, None, None, None, None)]

def pack_page():
    window_title.pack()

    header.pack()
    body.pack()


window = Tk()
window.geometry(f'{window_x}x{window_y}')
window.title('Roster')

header = Frame(master = window, width = 512)
body = Frame(master = window, width = 512)


window_title = Label(text = f'Welcome to ROSTER, {user_info.current_user}!',
                     master = header, font = (title_font, title_font_size), anchor = 'center', fg = primary_color)

pack_page()