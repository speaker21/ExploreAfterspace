class GameState:
    def __init__(self) -> None:
        self.pause = True
        self.day = 0
        self.speed_up = False
        self.frames = []
        self.stars_list = []

    def changeState(self, button):
        if self.pause == True:
            self.pause = False
            button.setText('||')

        elif self.pause == False:
            self.pause = True
            button.setText('>')
        print(f'now pause is {self.pause}')
    
    def change_speed_up(self, button):
        if self.speed_up == True:
            self.speed_up = False
            button.setText('Скорость х1')

        elif self.speed_up == False:
            self.speed_up = True
            button.setText('Скорость х5')
        print(f'now speed_up is {self.speed_up}')

    def change_frame(self, name):
        for frame in self.frames:
            if (frame.name != name) and (frame.isVisible()):
                frame.hide()
        for frame in self.frames:
            if (frame.name == name) and not (frame.isVisible()):
                frame.show()

    def get_star_info_frame(self):
        for frame in self.frames:
            if frame.name == 'star_info':
                return frame
            
    def show_star_info(self, star):
        star_info_frame = self.get_star_info_frame()
        star_info_frame.set_data(star)
        self.change_frame('star_info')