import Enum
import os
import Validate
from msvcrt import getch
from colorama import init
init(convert=True)
from colorama import Fore, Back, Style


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

def GetPersonName():
    Print(Enum.EnterName)
    name = input()
    if not Validate.Name(name):
        PrintError(Enum.InvalidName)
        return GetPersonName()
    return name

def GetCityName():
    Print(Enum.EnterCity)
    city = input()
    if not Validate.City(city):
        PrintError(Enum.InvalidCity)
        return GetCityName()
    return city

def PrintSelectedContact():
    pass

def GetPhoneNumber():
    Print(Enum.EnterPhoneNumber)
    number = input()
    if not Validate.Number(number):
        PrintError(Enum.InvalidPhone)
        return GetPhoneNumber()
    return number

def PrintPerson(personObj):
    print(f"{personObj.phoneNumber} | {personObj.name} - {personObj.city}")
