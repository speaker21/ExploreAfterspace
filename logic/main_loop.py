from time import sleep
from logic.game_tick import change_label_value

def main_loop(game_state, day_label):
    print('loop works')
    while True:
        if game_state.pause == False:
            if game_state.speed_up == False:
                change_label_value(game_state, day_label)
            elif game_state.speed_up == True:
                for _ in range(5):
                    change_label_value(game_state, day_label)
            print(game_state.day)
        sleep(1)