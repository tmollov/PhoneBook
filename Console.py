import Enum
import os
import Validate
from msvcrt import getch
from colorama import init
init(convert=True)
from colorama import Fore, Back, Style
from Enum import StringFore

def Clear(): return os.system('cls')

def GetInput():
    while True:
        keycode = ord(getch())
        if keycode == 13: #Enter
            return Enum.Enter
        elif keycode == 80: #Down arrow
            return Enum.DownArrow
        elif keycode == 72: #Up arrow
            return Enum.UpArrow

def Print(content):
    print(content, end="")

def PrintError(content):
    print(f"{Fore.RED}{content}{Fore.RED}{Fore.WHITE}")

def GetPersonName(IsClear=False,regex=None):
    Print(Enum.EnterName if not IsClear else "")
    name = input()
    res = None
    if regex == None:
        res = Validate.Name(name)
    else:
        res = Validate.Name(name,regex)

    if not res:
        PrintError(Enum.InvalidName)
        return GetPersonName(IsClear,regex)
    return name

def GetCityName(IsClear=False,regex=None):
    Print(Enum.EnterCity if not IsClear else "")
    city = input()
    res = None
    if regex==None:
        res = Validate.City(city)
    else:
        res = Validate.City(city,regex)

    if not res:
        PrintError(Enum.InvalidCity)
        return GetCityName(IsClear,regex)
    return city

def GetPhoneNumber(IsClear=False,regex=None):
    Print(Enum.EnterPhoneNumber if not IsClear else "")
    number = input()
    res = None
    if regex==None:
        res = Validate.Number(number)
    else:
        res = Validate.Number(number,regex)

    if not res:
        PrintError(Enum.InvalidPhone)
        return GetPhoneNumber(IsClear,regex)
    return number

def SearchByInputInfo(selection):
    if selection == Enum.SearchByName:
        Print(Enum.SearchName)
    elif selection == Enum.SearchByCity:
        Print(Enum.SearchCity)
    elif selection == Enum.SearchByNumber:
        Print(Enum.SearchNumber)

def IsntSuchAContact(sOption):
    string = f"There isn't such a contact with given {sOption}!"
    print(StringFore.LIGHTCYAN_EX(string))

def PrintSelectedSearch(db,selectionIndex):
    for i in range(len(db)):
        if i == selectionIndex:
            print(StringFore.GREEN(db[i]))
        else:
            print(db[i])

def PrintSelectedContact(db,selectionIndex):
    for i in range(len(db)):
        if i == selectionIndex:
            PrintSelectedPerson(db[i])
        else:
            PrintPerson(db[i])

def PrintPerson(personObj):
    print(f"{personObj.name} - {personObj.phoneNumber} | {personObj.city}")

def PrintSelectedPerson(personObj):
    print(f"{Fore.GREEN}{personObj.name} - {personObj.phoneNumber} | {personObj.city}{Fore.GREEN}{Fore.WHITE}")

def WaitForEnter():
    while True:
        key = GetInput()
        if key == Enum.Enter:
            return

def ConfirmDelete(person): 
    string = f"{person.name} / {person.phoneNumber} ({person.city})"
    print(f"Do you really want to delete contact:\n {StringFore.LIGHTCYAN_EX(string)} ? [yes/no]",end="")
    while True:
        decition = input().lower()
        if decition in ["yes",'y']:
            return True
        elif decition in ["no",'n']:
            return False
        else:
            print(Enum.InvalidComfirmation)

def ConfirmUpdate(person,name,city,phoneNumber):
    print("=" * 20)
    print(f"Do you really want to update contact:{Enum.NewLine}")
    print(f"Name from {StringFore.LIGHTCYAN_EX(person.name)} to * {StringFore.CYAN(name)} *")
    print(f"City from {StringFore.LIGHTCYAN_EX(person.city)} to * {StringFore.CYAN(city)} *")
    print(f"Phone Number from {StringFore.LIGHTCYAN_EX(person.phoneNumber)} to * {StringFore.CYAN(phoneNumber)} *")
    print(f"Type [yes/no] ",end="")
    while True:
        decition = input().lower()
        if decition in ["yes",'y']:
            return True
        elif decition in ["no",'n']:
            return False
        else:
            print(Enum.InvalidComfirmation)


