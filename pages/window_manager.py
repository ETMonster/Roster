import pages.start_window
import pages.onboard_window

class Window:
    def __init__(self, file, return_value):
        self.file = file
        self.return_value = return_value

    def initiate_window(self, window, callback_function):
        for widget in window.winfo_children():
            widget.destroy()

        self.file.create_widgets(window, callback_function)

start_window = Window(pages.start_window, None)
onboard_window = Window(pages.onboard_window, None)