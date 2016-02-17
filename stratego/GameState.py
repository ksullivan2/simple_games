from enum import Enum

class GameState(Enum):
    player_setup = -2
    start = -1
    setup_no_piece = 0
    setup_selected_piece = 1
    pieces_placed = 2
    gameplay_no_piece = 3
    game_selected_piece = 4
    conflict = 5
    win = 6
