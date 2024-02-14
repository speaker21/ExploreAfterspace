def game_tick(game_state, label, signaller):
    game_state.day+=1
    label.setText(str(game_state.day))

    for star in game_state.stars_list:
        star.calculate_population()
        for planet in star.planets:
            planet.calculate_population()

    signaller.progress_changed.emit(game_state)