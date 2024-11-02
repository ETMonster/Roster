from tkinter import messagebox

window_x = 800 #px
window_y = 800 #px

title_font_size = 50
subtitle_font_size = 25
body_font_size = 14

title_font = 'Franklin Gothic Medium'
subtitle_font = 'Franklin Gothic Medium'
body_font = 'Calibri'

primary_color = '#ff7373'
secondary_color = '#faa0a0'

background_color = 'lightgrey'

login_prohibited_characters = [
    ' ', "'", '"'
]
login_minimum_length = 2
login_maximum_length = 24

profile_destination = 'images/profiles'

def widget_hover(widget):
    widget.config(bg = secondary_color)

def widget_unhover(widget):
    widget.config(bg = background_color)

def throw_error(reason):
    if reason == 'Character':
        messagebox.showinfo(title='Error', essage=f'Your username or password contains prohibited characters.')
    elif reason == 'Information':
        messagebox.showinfo(title='Error', message='Username or password is incorrect.')
    elif reason == 'Length':
        messagebox.showinfo(title='Error', message=f'Your username and password must be a minimum of {login_minimum_length} and a maximum of {login_maximum_length} characters long.')
    elif reason == 'Exists':
        messagebox.showinfo(title='Error', message=f'Your desired username is already in use.')
    elif reason == 'BadProfile':
        messagebox.showinfo(title='Error', message='There was an unexpected error while uploading your profile picture."')