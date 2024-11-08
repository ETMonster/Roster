from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

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
profile_picture_extensions = [
    '*.png', '*.jpg', '*.jpeg'
]

gender_options = [
    'Male', 'Female', 'Other'
]
preferred_gender_options = [
    'Male', 'Female', 'All'
]

music_options = [
    "Alternative", "Blues", "Classical", "Country", "Dance", "Disco", "Electronic", "Folk", "Funk", "Hip Hop",
    "Jazz", "Metal", "Pop", "Punk", "R&B", "Rap", "Reggae", "Rock", "Soul", "World"
]

hobby_options = [
    "Archery", "Baking", "Camping", "Cycling", "Drawing", "Fishing", "Gardening", "Hiking", "Jogging", "Knitting",
    "Painting", "Photography", "Reading", "Running", "Sculpting", "Sewing", "Swimming", "Traveling", "Woodworking", "Writing"
]

movie_options = [
    "Avatar", "Back to the Future", "Casablanca", "Die Hard", "Eternal Sunshine of the Spotless Mind", "Forrest Gump",
    "Gladiator", "Inception", "Jaws", "Kill Bill", "Lord of the Rings", "Mad Max: Fury Road", "Pulp Fiction",
    "Schindler's List", "Star Wars", "The Dark Knight", "The Godfather", "The Matrix", "The Shawshank Redemption", "Titanic"
]

def widget_hover(widget):
    widget.config(bg = secondary_color)

def widget_unhover(widget):
    widget.config(bg = background_color)

def on_mousewheel(event, canvas):
    canvas.yview_scroll(-1 * int(event.delta / 120), 'units')

def throw_error(reason):
    if reason == 'Character':
        messagebox.showinfo(title='Error', message=f'Your username or password contains prohibited characters.')
    elif reason == 'Information':
        messagebox.showinfo(title='Error', message='Username or password is incorrect.')
    elif reason == 'Length':
        messagebox.showinfo(title='Error', message=f'Your username and password must be a minimum of {login_minimum_length} and a maximum of {login_maximum_length} characters long.')
    elif reason == 'Exists':
        messagebox.showinfo(title='Error', message=f'Your desired username is already in use.')
    elif reason == 'BadProfile':
        messagebox.showinfo(title='Error', message='There was an unexpected error while uploading your profile picture.')
    elif reason == 'BadAge':
        messagebox.showinfo(title='Error', message='Age must be an integer number.')
    elif reason == 'BadMBTI':
        messagebox.showinfo(title='Error', message='MBTI personality must be a valid personality according to the MBTI')
    elif reason == 'NoCharacters':
        messagebox.showinfo(title='Error', message='All entries must have content.')


def prepare_image(image, target_size = (256, 256)):
    width, height = image.size
    min_dimension = min(width, height)

    left = (width - min_dimension) / 2
    top = (height - min_dimension) / 2
    right = (width + min_dimension) / 2
    bottom = (height + min_dimension) / 2

    return image.crop((left, top, right, bottom)).resize(target_size, Image.LANCZOS)