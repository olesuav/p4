import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('Menu Harjoittelu', (600, 400))


def set_difficulty(selected: Tuple, value: Any) -> None:
 

    print(f'Set difficulty to {selected[0]} ({value})')


def start_the_game() -> None:

    global user_name
    print(f'{user_name.get_value()}, Do the job here!')


menu = pygame_menu.Menu(
    height=400,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=600
)

user_name = menu.add.text_input('Name: ', default=' ', maxchar=15)
menu.add.selector('Difficulty: ', [('Easy', 1), ('Medium', 2), ("Hard", 3)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)