def change_label_value(game_state, label, signaller):
    game_state.day+=1
    label.setText(str(game_state.day))

    for star in game_state.stars_list:
        star.calculate_population()

    signaller.progress_changed.emit(game_state)