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

def PrintSelectedContact(db,selectionIndex):
    for i in range(len(db)):
        if i == selectionIndex:
            PrintSelectedPerson(db[i])
        else:
            PrintPerson(db[i])

def GetPhoneNumber():
    Print(Enum.EnterPhoneNumber)
    number = input()
    if not Validate.Number(number):
        PrintError(Enum.InvalidPhone)
        return GetPhoneNumber()
    return number

def PrintPerson(personObj):
    print(f"{personObj.phoneNumber} | {personObj.name} - {personObj.city}")

def PrintSelectedPerson(personObj):
    print(f"{Fore.GREEN}{personObj.phoneNumber} | {personObj.name} - {personObj.city}{Fore.GREEN}{Fore.WHITE}")

def WaitForEnter():
    while True:
        key = GetInput()
        if key == Enum.Enter:
            return



def DeleteComfirm(person): 
    print(f"Do you really want to * {person.name} / {person.phoneNumber}* ({person.city}) ? [yes/no]",end="")
    while True:
        decition = input().lower()
        if decition in ["yes",'y']:
            return True
        elif decition in ["no",'n']:
            return False
        else:
            print(Enum.InvalidComfirmation)

        