def change_label_value(game_state, label):
    game_state.day+=1
    label.setText(str(game_state.day))

    for star in game_state.stars_list:
        star.calculate_population()

    game_state.get_star_info_frame().update_info()