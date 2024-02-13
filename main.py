import sys
from PyQt5.QtWidgets import QApplication
from logic.game_state import GameState
import threading
from logic.main_loop import main_loop
from ui.frames.main_frame import MainFrame
from ui.widgets.star_info import StarInfo
from ui.widgets.planet_info import PlanetInfo
from logic.celestials_init import celestials_init
from PyQt5.QtCore import pyqtSignal, QObject

class Signaller(QObject):
    progress_changed = pyqtSignal(GameState)

if __name__ == '__main__':
    
    game_state = GameState()
    app = QApplication(sys.argv)
    celestials = celestials_init(game_state)
    main_frame = MainFrame(game_state, app)
    star_info = StarInfo()
    planet_info = PlanetInfo()
    game_state.star_info_frame = star_info
    game_state.planet_info_frame = planet_info

    signaller = Signaller()
    signaller.progress_changed.connect(star_info.update_info)
    logic_thread = threading.Thread(target=main_loop, args=(game_state, main_frame.header.label, signaller), daemon=True)
    logic_thread.start()

    sys.exit(app.exec_())
    