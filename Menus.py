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

def ShowOption(index):
    Console.Clear()
    if index == 0:
        pass
    elif index == 1:
        AllContactsOption()
    elif index == 2:
        AddContactOption()
    elif index == 3:
        DeleteContactOption()
    elif index == 4:
        UpdateContactOption()
    ShowMainMenu()

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

def DeleteContactOption():
    print(Enum.DeleteInfo)
    data = Data.GetDb()
    selection = 0
    Console.PrintSelectedContact(data,selection)
    while True:
        keycode = Console.GetInput()
        if keycode == Enum.DownArrow: #Down arrow
            selection += 1
        elif keycode == Enum.UpArrow: #Up arrow
            selection -= 1
        elif keycode == Enum.Enter:
            if Console.DeleteComfirm(data[selection]):
                Data.DeleteContact(data[selection].guid)
                print(Enum.EnterForMainMenu)
                Console.WaitForEnter()
                return
            else:
                print(Enum.ContactNotDeleted)
                Console.WaitForEnter()
                return

        if selection < 0:
            selection = 0
        if selection >= len(data)-1:
            selection = len(data)-1
        Console.Clear()
        print(Enum.DeleteInfo)
        Console.PrintSelectedContact(data,selection)

def UpdateContactOption():
    print(Enum.UpdateContactInfo)
    data = Data.GetDb()
    selection = 0
    Console.PrintSelectedContact(data,selection)
    while True:
        keycode = Console.GetInput()
        if keycode == Enum.DownArrow:
            selection += 1
        elif keycode == Enum.UpArrow:
            selection -= 1
        elif keycode == Enum.Enter:
            Console.Clear()
            person = data[selection]

            print()
            nameUpdate = input()
            if Console.DeleteComfirm():
                Data.DeleteContact(data[selection].guid)
                print(Enum.EnterForMainMenu)
                Console.WaitForEnter()
                return
            else:
                print(Enum.ContactNotDeleted)
                Console.WaitForEnter()
                return

        if selection < 0:
            selection = 0
        if selection >= len(data)-1:
            selection = len(data)-1
        Console.Clear()
        print(Enum.DeleteInfo)
        Console.PrintSelectedContact(data,selection)

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

