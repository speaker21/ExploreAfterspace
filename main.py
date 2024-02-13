import sys
from PyQt5.QtWidgets import QApplication
from logic.game_state import GameState
import threading
from logic.main_loop import main_loop
from ui.frames.main_frame import MainFrame
from ui.widgets.star_info import StarInfo


if __name__ == '__main__':
    
    game_state = GameState()
    app = QApplication(sys.argv)
    main_frame = MainFrame(game_state, app)
    star_info = StarInfo()
    game_state.star_info_frame = star_info

    logic_thread = threading.Thread(target=main_loop, args=(game_state, main_frame.header.label), daemon=True)
    logic_thread.start()

    sys.exit(app.exec_())
    