import time
import Data
import Console

import Menus
import Enum
import Menus

menuIndex = 0

if __name__ == '__main__':
    Menus.ShowMainMenu()
    while True:
        keycode = Console.GetInput()
        if keycode == Enum.Enter: #Enter
            Console.Clear()
            Menus.ShowOption(menuIndex)
        elif keycode == Enum.DownArrow: #Down arrow
            menuIndex += 1
        elif keycode == Enum.UpArrow: #Up arrow
            menuIndex -= 1

        if menuIndex < 0:
            menuIndex = 0
        if menuIndex >= 4:
            menuIndex = 4
        Menus.ShowMainMenu(menuIndex)