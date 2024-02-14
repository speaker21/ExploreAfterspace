from time import sleep
from logic.game_tick import game_tick

def main_loop(game_state, day_label, signaller):
    print('loop works')
    while True:
        if game_state.pause is False:
            if game_state.speed_up is False:
                game_tick(game_state, day_label, signaller)
            elif game_state.speed_up is True:
                for _ in range(5):
                    game_tick(game_state, day_label, signaller)
            print(game_state.day)
        sleep(1)