window_x = 800 #px
window_y = 800 #px

title_font_size = 50
subtitle_font_size = 25
body_font_size = 12

title_font = 'Franklin Gothic Heavy'
subtitle_font = 'Franklin Gothic Medium'
body_font = 'Calibri'

primary_color = '#ff7373'
secondary_color = '#faa0a0'

background_color = 'lightgrey'

def widget_hover(widget):
    widget.config(bg = secondary_color)

def widget_unhover(widget):
    widget.config(bg = background_color)

login_prohibited_characters = [
    ' ', "'", '"'
]
login_minimum_length = 2
login_maximum_length = 24