import pages.start_window

class Window:
    def __init__(self, file, return_value):
        self.file = file
        self.return_value = return_value

    def create_window(self):
        self.file.mainloop()

    def set_return_value(self, value):
        self.return_value = value

start_window = Window(pages.start_window, """Return value here""")