import pages.start_window
import pages.onboard_window

class Window:
    def __init__(self, file):
        self.file = file

    def initiate_window(self):
        self.file.window.mainloop()

        return self.file.callback

start_window = Window(pages.start_window)
onboard_window = Window(pages.onboard_window)