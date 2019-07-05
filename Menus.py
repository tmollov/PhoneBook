from colorama import init
init(convert=True)
from colorama import Fore, Back, Style
import Validate
from msvcrt import getch
import Console
import Enum
import Data
import pickle
from Exception import AddException

def ShowMainMenu(index=0):
    Console.Clear()
    color = Fore.WHITE
    welcome = f"{color}{Enum.Welcome}{color}"
    controls = f"{color}{Enum.Controls}{color}"
    strings = []
    strings.append(welcome.center(50))
    strings.append(controls.center(50))
    strings.append("\n")
    for i in range(len(Enum.MenuOptions)):
        if i == index:
            color = Fore.GREEN
            strings.append(f"> {color}{Enum.MenuOptions[i]}{color}".center(50))
            color = Fore.WHITE
        else:
            strings.append(f"{color}{Enum.MenuOptions[i]}{color}".center(50))
    strings.append("")
    print("\n".join(strings))


def ShowOption(index):
    Console.Clear()
    if index == 0:
        pass
    elif index == 1:
        AllContactsOption()
    elif index == 2:
        AddContactOption()
    elif index == 3:
        pass
    elif index == 4:
        pass
    ShowMainMenu()

def DeleteContact():
    pass

def AllContactsOption():
    contacts = Data.GetDb()
    for p in contacts:
        Console.PrintPerson(p)
    print(Enum.EnterForMainMenu)
    while True:
        if Console.GetInput() == Enum.Enter:
            return


def AddContactOption():
    Console.Clear()
    print(Enum.NameAndCityInfo)

    name = Console.GetPersonName()
    city = Console.GetCityName()
    number = Console.GetPhoneNumber()

    result = Data.AddContact(name,city,number)
    if result != type(AddException):
        print(Enum.ContactAdded)
        print(Enum.EnterForMainMenu)

        while True:
            if Console.GetInput() == Enum.Enter:
                return
    else:
        print(result.message)
        while True:
            if Console.GetInput() == Enum.Enter:
                return
