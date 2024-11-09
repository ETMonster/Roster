import pages.start_window
import pages.onboard_window
import pages.match_window

class Window:
    def __init__(self, file):
        self.file = file

    def initiate_window(self, window, callback_function):
        for widget in window.winfo_children():
            widget.destroy()

        self.file.create_widgets(window, callback_function)

start_window = Window(pages.start_window)
onboard_window = Window(pages.onboard_window)
match_window = Window(pages.match_window)