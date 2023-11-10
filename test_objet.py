class window():
    
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('Space Invaders Ju2 version')
        self.Canevas = Canvas(self.main_window, width = 1280, height = 720, background = 'white')
