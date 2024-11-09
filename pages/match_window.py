from multiprocessing.spawn import prepare
from tkinter import *
from PIL import Image, ImageTk
import os

from constants import *
import compatibility
import user_info

def create_widgets(window, callback):
    def pack_page():
        roster_logo.grid(row=0, column=0)
        title.grid(row=1, column=0)
        title_username.grid(row=2, column=0)

        header.pack()

        for i, frame in enumerate(match_frames):
            user = user_info.get_user_from_id(top_matches[i].user_id)

            Label(text = f'{user.first_name} {user.last_name}',
                  master = frame, font = (subtitle_font, subtitle_font_size)).grid(row = 0, column = 0, pady = (0, 5))

            image = Image.open(user.profile_picture_path)
            image = prepare_image(image, (128, 128))

            tkinter_image = ImageTk.PhotoImage(image)

            image_label = Label(master = frame, image = tkinter_image, anchor = 'center')
            image_label.image = tkinter_image

            image_label.grid(row = 1, column = 0)

            Label(text = f'Gender: {user.compatability_attributes.gender}',
                  master = frame, font = (body_font, body_font_size)).grid(row = 2, column = 0)
            Label(text = f'Age: {user.compatability_attributes.age}',
                  master = frame, font = (body_font, body_font_size)).grid(row = 3, column = 0)
            Label(text=f'Compatability score:',
                  master=frame, font=(subtitle_font, body_font_size)).grid(row=4, column=0, pady = (5, 0))
            Label(text=f'{top_matches[i].compatability_score} / 33',
                  master=frame, font=(body_font, body_font_size)).grid(row=5, column=0)

            frame.grid(row = i // 3, column = i % 3, padx = (50, 50), pady = (0, 20))

        matches_frame.pack()

        back_button.pack(pady = (30, 40))

        body.pack(pady = (30, 0))

        canvas.create_window((window_x // 2, 0), window=canvas_frame, anchor='n')

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        main_frame.pack(fill=BOTH)

    def back():
        callback.start()

    main_frame = Frame(master=window, width=window_x)

    canvas = Canvas(master=main_frame, height=window_y)
    scrollbar = Scrollbar(master=main_frame, orient=VERTICAL, command=canvas.yview)

    canvas_frame = Frame(master=canvas)

    header = Frame(master = canvas_frame)
    body = Frame(master = canvas_frame)

    roster_logo_image = PhotoImage(file='images/logo_256.png')
    roster_logo = Label(master=header, image=roster_logo_image, anchor='center')
    roster_logo.image = roster_logo_image

    title = Label(text=f'Say hi your matches,',
                  master=header, font=(title_font, title_font_size), anchor='center', fg=primary_color)
    title_username = Label(text=f'{user_info.current_user.first_name}!',
                           master=header, font=(subtitle_font, subtitle_font_size), anchor='center')


    top_matches = compatibility.find_matches(user_info.current_user)[:amount_of_matches]

    matches_frame = Frame(master = body)

    match_frames = [Frame(master = matches_frame) for _ in range(amount_of_matches)]


    back_button = Button(text = 'Log out',
                         master=body, font=(body_font, body_font_size), bg=background_color, bd=0, anchor='center',
                         cursor='hand2', activebackground=primary_color, command=back
                        )

    # Configure actions

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda event: canvas.configure(scrollregion=canvas.bbox('all')))

    window.bind_all("<MouseWheel>", lambda event: on_mousewheel(event, canvas))

    back_button.bind('<Enter>', lambda button: widget_hover(back_button))

    back_button.bind('<Leave>', lambda button: widget_unhover(back_button))

    pack_page()