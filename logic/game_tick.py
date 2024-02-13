def change_label_value(game_state, label):
    game_state.day+=1
    label.setText(str(game_state.day))