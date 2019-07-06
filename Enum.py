from colorama import init
init(convert=True)
from colorama import Fore, Back, Style

class StringFore:
    def LIGHTCYAN_EX(content):
        return F"{Fore.LIGHTCYAN_EX}{content}{Fore.LIGHTCYAN_EX}{Fore.WHITE}"

    def GREEN(content):
        return F"{Fore.GREEN}{content}{Fore.GREEN}{Fore.WHITE}"
    
    def RED(content):
        return F"{Fore.RED}{content}{Fore.RED}{Fore.WHITE}"
    
    def CYAN(content):
        return F"{Fore.CYAN}{content}{Fore.CYAN}{Fore.WHITE}"

SearchByName = 0
SearchByCity = 1
SearchByNumber = 2
SearchName = "Enter Name: "
SearchCity = "Enter City: "
SearchNumber = "Enter Phone Number: "

Enter = "enter"
UpArrow = "up"
DownArrow = "down"
EnterForMainMenu = f"Press {Fore.LIGHTBLUE_EX}ENTER{Fore.LIGHTBLUE_EX}{Fore.WHITE} to return to main menu..."

NewLine = "\n"
Tab = "\t"

#Menu 
Welcome = "Welcome to PhoneBook"
Controls = "Use up/down arrow to move up & down\nUse ENTER to select given option"

# Add Contact Info strings
NameAndCityInfo = "Name and City must contain only lower/upper case alphabetic character and spaces!\n"
EnterName = "Enter Name: "
EnterCity = "Enter City: "
EnterPhoneNumber = "Enter Phone Number: "
SearchBy = "Search by ..."
ContactAdded = StringFore.GREEN("*** Contact Added! ***")
ContactUpdated = StringFore.GREEN("*** Contact Updated! ***")
DeleteInfo = f"{Fore.LIGHTMAGENTA_EX}Select contact to delete...{Fore.LIGHTMAGENTA_EX}{Fore.WHITE}"

UpdateContactInfo = f"{Fore.LIGHTMAGENTA_EX}Select contact to update...{Fore.LIGHTMAGENTA_EX}{Fore.WHITE}"

MenuOptions = ["Search by...", "All Contacts",
                  "Add Contact", "Delete Contact", "Edit Contact"]

SearchOptions = ["By Name", "By City", "By Phone Number"]
SearchOptionsClear = ["Name" , "City", "Phone Number"]
ContactNotDeleted = f"{Fore.LIGHTCYAN_EX}Contact not deleted.{Fore.LIGHTCYAN_EX}{Fore.WHITE}"



def EnterNameUpdate(name):
    return f"Name from {name} to : "

def EnterCityUpdate(city):
    return f"City from {city} to : "

def EnterNumberUpdate(number):
    return f"Phone number from {number} to : "

#### INVALID INPUT
InvalidName = f"Name must contain only lower, upper or mixed case alphabetic character and spaces!"
InvNameLen = f"Name length must be between 2-50 charachters!"

InvalidCity = f"City must contain only lower, upper or mixed case alphabetic character and spaces!"
InvNameLen = f"City length must be between 2-50 charachters!"

InvalidPhone = f"Phone number must contains only digits!"
InvPhoneLen = f"Phone number must be between 5-15"
InvalidComfirmation = f"Please type {Fore.LIGHTBLUE_EX}y / yes{Fore.LIGHTBLUE_EX}{Fore.WHITE} or {Fore.LIGHTBLUE_EX}n / no{Fore.LIGHTBLUE_EX}{Fore.WHITE}"
#### Exceptions
def ContactExist(contactName,contactCity,contactNumber):
 return f"{Fore.YELLOW}Contact: {contactNumber} - {contactName}|{contactCity} already exists!{Fore.YELLOW}{Fore.WHITE}"