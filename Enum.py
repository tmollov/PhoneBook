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

    def YELLOW(content):
        return F"{Fore.YELLOW}{content}{Fore.YELLOW}{Fore.WHITE}"    
    
    def CYAN(content):
        return F"{Fore.CYAN}{content}{Fore.CYAN}{Fore.WHITE}"
    
    def LIGHTMAGENTA_EX(content):
        return F"{Fore.LIGHTMAGENTA_EX}{content}{Fore.LIGHTMAGENTA_EX}{Fore.WHITE}"
    
    def LIGHTBLUE_EX(content):
        return F"{Fore.LIGHTBLUE_EX}{content}{Fore.LIGHTBLUE_EX}{Fore.WHITE}"

SearchByName = 0
SearchByCity = 1
SearchByNumber = 2

Enter = "enter"
UpArrow = "up"
DownArrow = "down"

BlueEnter = StringFore.LIGHTBLUE_EX("ENTER")
EnterForMainMenu = f"Press {BlueEnter} to return to main menu..."

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
ContactAdded = StringFore.GREEN("*** Contact Added! ***")

# Delete Contact strings
DeleteInfo = StringFore.LIGHTMAGENTA_EX("Select contact to delete...")
ContactDeleted = StringFore.GREEN("*** Contact Deleted! ***")
ContactNotDeleted = StringFore.LIGHTCYAN_EX("Contact not deleted.")

# Update Contact strings
UpdateContactInfo = StringFore.LIGHTMAGENTA_EX("Select contact to update...")
ContactUpdated = StringFore.GREEN("*** Contact Updated! ***")

# Search By strings
SearchBy = "Search by ..."
SearchOptions = ["By Name", "By City", "By Phone Number"]
SearchOptionsClear = ["Name" , "City", "Phone Number"]

MenuOptions = ["Search by...", "All Contacts",
                  "Add Contact", "Delete Contact", "Edit Contact"]

def EnterNameUpdate(name):
    return f"Name from {name} to : "

def EnterCityUpdate(city):
    return f"City from {city} to : "

def EnterNumberUpdate(number):
    return f"Phone number from {number} to : "

#### INVALID INPUT
InvalidName = f"Name must contain only lower, upper or mixed case alphabetic character and spaces!"
InvNameLen = f"Name length must be between 3-50 charachters!"

InvalidCity = f"City must contain only lower, upper or mixed case alphabetic character and spaces!"
InvCityLen = f"City length must be between 3-50 charachters!"

InvalidPhone = f"Phone number must contains only digits!"
InvPhoneLen = f"Phone number must be between 5-15"

yesOption = StringFore.LIGHTBLUE_EX("y / yes")
noOption = StringFore.LIGHTBLUE_EX("n / no")
InvalidComfirmation = f"Please type {yesOption} or {noOption}"
#### Exceptions
def ContactExist(contactName,contactCity,contactNumber):
 return StringFore.YELLOW(f"Contact: {contactNumber} - {contactName}|{contactCity} already exists!")