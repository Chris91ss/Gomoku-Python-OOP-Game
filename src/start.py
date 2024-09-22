import sys
from src.ui.ui import UI
from src.gui.gui import GomokuGUI

if __name__ == "__main__":
    # Check if user passed an argument for GUI or UI
    if len(sys.argv) > 1 and sys.argv[1] == "--ui":
        gomoku_game = UI(size=10)
    else:
        gomoku_game = GomokuGUI(size=10)
        
    gomoku_game.run()