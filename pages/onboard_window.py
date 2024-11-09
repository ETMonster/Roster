from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import shutil
import os

from constants import *
import user_info
from compatibility import MBTI

def create_widgets(window, callback):
    combobox_style = ttk.Style(window)
    combobox_style.theme_use('clam')
    combobox_style.configure(
        'TCombobox',
        foreground = 'black',
        fieldbackground = background_color,
        background = background_color,
        font = body_font,
        bd = 0
    )

    def pack_page():
        roster_logo.grid(row = 0, column = 0)
        title.grid(row = 1, column = 0)
        title_username.grid(row = 2, column = 0)

        horizontal_line.grid(row = 3, column = 0, pady = (30, 0))

        header.pack()

        first_name_label.grid(row = 1, column = 0, padx = (0, 5))
        last_name_label.grid(row = 2, column = 0, padx = (0, 5))
        first_name_entry.grid(row = 1, column = 1)
        last_name_entry.grid(row = 2, column = 1)

        name_frame.grid(row = 0, column = 0)

        profile_picture.grid(row = 0, column = 0)
        upload_profile_button.grid(row = 1, column = 0, pady = (10, 0))

        upload_frame.grid(row = 1, column = 0, pady = (30, 0))

        age_label.grid(row = 0, column = 0, padx = (0, 5))
        age_entry.grid(row = 0, column = 1)

        age_frame.grid(row = 2, column = 0, pady = (30, 0))

        gender_label.grid(row = 0, column = 0, padx = (0, 5))
        preferred_gender_label.grid(row = 1, column = 0, padx = (0, 5))
        gender_dropdown.grid(row = 0, column = 1)
        preferred_gender_dropdown.grid(row = 1, column = 1)

        gender_frame.grid(row = 3, column = 0, pady = (10, 0))

        mbti_label.grid(row = 0, column = 0, padx = (0, 5))
        mbti_entry.grid(row = 0, column = 1)

        mbti_frame.grid(row = 4, column = 0, pady = (10, 0))

        music_label.grid(row = 0, column = 0, padx = (0, 5))
        music_dropdown.grid(row = 0, column = 1)

        music_frame.grid(row = 5, column = 0, pady = (20, 0))

        movie_label.grid(row=0, column=0, padx=(0, 5))
        movie_dropdown.grid(row=0, column=1)

        movie_frame.grid(row=6, column=0, pady=(10, 0))

        hobby_label.grid(row=0, column=0, padx=(0, 5))
        hobby_dropdown.grid(row=0, column=1)

        hobby_frame.grid(row=7, column=0, pady=(10, 0))

        submit_button.grid(row = 8, column = 0, pady = (30, 0))

        body.pack(pady = (30, 40))

        canvas.create_window((window_x // 2, 0), window = canvas_frame, anchor = 'n')

        canvas.pack(side = LEFT, fill = BOTH, expand = True)
        scrollbar.pack(side = RIGHT, fill = Y)

        main_frame.pack(fill = BOTH)

    def upload_profile_picture(profile_picture_label):
        # Open file dialog to select an image file
        system_file_path = filedialog.askopenfilename(
            title = 'Select a Profile Picture',
            filetypes = [('Image Files', ';'.join([x for x in profile_picture_extensions]))]
        )

        if system_file_path:
            if not os.path.exists(profile_destination):
                os.makedirs(profile_destination)

            destination_file_path = os.path.join(profile_destination, os.path.basename(system_file_path))

            file_name, file_extension = os.path.splitext(os.path.basename(destination_file_path))

            counter = 1
            while os.path.exists(destination_file_path):
                destination_file_path = os.path.join(profile_destination, f'{file_name} ({counter}){file_extension}')
                file_name = f'{file_name} ({counter})'

                counter +=  1

            try:
                shutil.copy(system_file_path, destination_file_path)

                updated_file_path = user_info.current_user.login_information.username + file_extension
                updated_file_path = os.path.join(profile_destination, updated_file_path)

                for file in os.listdir(profile_destination):
                    if file.startswith(user_info.current_user.login_information.username):
                        os.remove(os.path.join(profile_destination, file))
                    else:
                        continue

                os.rename(destination_file_path, updated_file_path)

                destination_file_path = updated_file_path
            except:
                throw_error('BadProfile')
                return None

            user_info.current_user.profile_picture_path = destination_file_path
            user_info.write_users()

            _profile_picture_image = Image.open(destination_file_path)
            _profile_picture_image = prepare_image(_profile_picture_image, (256, 256))

            _profile_picture_tkinter_image = ImageTk.PhotoImage(_profile_picture_image)

            profile_picture_label.configure(image = _profile_picture_tkinter_image)
            profile_picture_label.photo = _profile_picture_tkinter_image

    def submit():
        for entry in entries:
            if entry.get() == '' or entry.get() is None:
                throw_error('NoCharacters')
                return

        if not age_entry.get().isdigit():
            throw_error('BadAge')
            return
        if mbti_entry.get() not in MBTI.matrix_indices:
            throw_error('BadMBTI')
            return
        if len(first_name_entry.get()) > login_maximum_length or len(last_name_entry.get()) > login_maximum_length:
            throw_error('Length')
            return

        callback.change_user_information(
            user_info.User(
                None,
                first_name_entry.get(),
                last_name_entry.get(),
                None,
                None,
                user_info.User_Attributes(
                    gender_dropdown.get(),
                    preferred_gender_dropdown.get(),
                    age_entry.get(),
                    mbti_entry.get(),
                    music_dropdown.get(),
                    movie_dropdown.get(),
                    hobby_dropdown.get()
                )
            )
        )

    main_frame = Frame(master = window, width = window_x)

    canvas = Canvas(master = main_frame, height = window_y)
    scrollbar = Scrollbar(master = main_frame, orient = VERTICAL, command = canvas.yview)

    canvas_frame = Frame(master = canvas)

    header = Frame(master = canvas_frame)
    body = Frame(master = canvas_frame)

    # Header
    roster_logo_image = PhotoImage(file = 'images/logo_256.png')
    roster_logo = Label(master = header, image = roster_logo_image, anchor = 'center')
    roster_logo.image = roster_logo_image

    title = Label(text = f'Welcome to ROSTER,',
                  master = header, font = (title_font, title_font_size), anchor = 'center', fg = primary_color)
    title_username = Label(text = f'{user_info.current_user.login_information.username}!',
                           master = header, font = (subtitle_font, subtitle_font_size), anchor = 'center')

    horizontal_line_image = PhotoImage(file = 'images/horizontal_line_512.png')
    horizontal_line = Label(master = header, image = horizontal_line_image, anchor = 'center')
    horizontal_line.image = horizontal_line_image

    # Body
    name_frame = Frame(master = body)

    first_name_label = Label(text = 'First Name',
                                 master = name_frame, font = (body_font, body_font_size), anchor = 'center')
    last_name_label = Label(text = 'Last Name',
                                 master = name_frame, font = (body_font, body_font_size), anchor = 'center')
    first_name_entry = Entry(master = name_frame, width = 24, font = (body_font, body_font_size),
                                 bg = background_color, bd = 0, highlightthickness = 1, highlightcolor = primary_color)
    last_name_entry = Entry(master = name_frame, width = 24, font = (body_font, body_font_size),
                                 bg = background_color, bd = 0, highlightthickness = 1, highlightcolor = primary_color)

    upload_frame = Frame(master = body)

    profile_picture_image = Image.open('images/profiles/admin.jpg')
    profile_picture_image.thumbnail(size = (256, 256))

    profile_picture_tkinter_image = ImageTk.PhotoImage(profile_picture_image)

    profile_picture = Label(master = upload_frame, image = profile_picture_tkinter_image, anchor = 'center')
    profile_picture.image = profile_picture_tkinter_image

    upload_profile_button = Button(text = 'Upload profile picture',
                          master = upload_frame, font = (body_font, body_font_size), bg = background_color, bd = 0, anchor = 'center',
                          cursor = 'hand2', activebackground = primary_color, command = lambda: upload_profile_picture(profile_picture))

    age_frame = Frame(master = body)

    age_label = Label(text = 'Age',
                      master = age_frame, font = (body_font, body_font_size), anchor = 'center')
    age_entry = Entry(master = age_frame, width = 3, font = (body_font, body_font_size),
                      bg = background_color, bd = 0, highlightthickness = 1, highlightcolor = primary_color)


    gender_frame = Frame(master = body)

    gender_label = Label(text = '     Your gender',
                         master = gender_frame, font = (body_font, body_font_size), anchor = 'center')
    gender_dropdown = ttk.Combobox(state = 'readonly', values = gender_options,
        master = gender_frame, style = 'TCombobox')
    preferred_gender_label = Label(text = 'Preferred gender',
                         master = gender_frame, font = (body_font, body_font_size), anchor = 'center')
    preferred_gender_dropdown = ttk.Combobox(state = 'readonly', values = preferred_gender_options,
        master = gender_frame, style = 'TCombobox')


    mbti_frame = Frame(master = body)

    mbti_label = Label(text = 'MBTI Test Personality',
                       master = mbti_frame, font = (body_font, body_font_size), anchor = 'center')
    mbti_entry = Entry(master = mbti_frame, width = 4, font = (body_font, body_font_size),
                      bg = background_color, bd = 0, highlightthickness = 1, highlightcolor = primary_color)


    music_frame = Frame(master = body)

    music_label = Label(text='Choose a music genre',
                         master=music_frame, font=(body_font, body_font_size), anchor='center')
    music_dropdown = ttk.Combobox(state='readonly', values=music_options,
                                   master=music_frame, style='TCombobox')

    movie_frame = Frame(master=body)

    movie_label = Label(text='Choose a movie',
                        master=movie_frame, font=(body_font, body_font_size), anchor='center')
    movie_dropdown = ttk.Combobox(state='readonly', values=movie_options,
                                  master=movie_frame, style='TCombobox')

    hobby_frame = Frame(master=body)

    hobby_label = Label(text='Choose a hobby',
                        master=hobby_frame, font=(body_font, body_font_size), anchor='center')
    hobby_dropdown = ttk.Combobox(state='readonly', values=hobby_options,
                                  master=hobby_frame, style='TCombobox')


    submit_button = Button(text = 'Find your matches!',
                                 master=body, font=(body_font, body_font_size), bg=background_color, bd=0, anchor='center',
                                 cursor='hand2', activebackground=primary_color, command=submit
                           )

    entries = [
        first_name_entry,
        last_name_entry,
        gender_dropdown,
        preferred_gender_dropdown,
        age_entry,
        mbti_entry,
        music_dropdown,
        movie_dropdown,
        hobby_dropdown
    ]

    # Configure actions

    canvas.configure(yscrollcommand = scrollbar.set)
    canvas.bind('<Configure>', lambda event: canvas.configure(scrollregion = canvas.bbox('all')))

    window.bind_all("<MouseWheel>", lambda event: on_mousewheel(event, canvas))

    upload_profile_button.bind('<Enter>', lambda button: widget_hover(upload_profile_button))
    submit_button.bind('<Enter>', lambda button: widget_hover(submit_button))

    upload_profile_button.bind('<Leave>', lambda button: widget_unhover(upload_profile_button))
    submit_button.bind('<Leave>', lambda button: widget_unhover(submit_button))

    pack_page()