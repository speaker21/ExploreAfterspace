import sys
from PyQt5.QtWidgets import QApplication
from logic.game_state import GameState
import threading
from logic.main_loop import main_loop
from ui.frames.main_frame import MainFrame


if __name__ == '__main__':
    
    game_state = GameState()
    app = QApplication(sys.argv)
    main_frame = MainFrame(game_state)
    logic_thread = threading.Thread(target=main_loop, args=(game_state, main_frame.header.label), daemon=True)
    logic_thread.start()

    sys.exit(app.exec_())
    