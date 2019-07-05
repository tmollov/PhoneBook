from colorama import init
init(convert=True)
from colorama import Fore, Back, Style

Enter = "enter"
UpArrow = "up"
DownArrow = "down"
EnterForMainMenu = f"Press {Fore.LIGHTBLUE_EX}ENTER{Fore.LIGHTBLUE_EX}{Fore.WHITE} to return to main menu..."

#Menu 
Welcome = "Welcome to PhoneBook"
Controls = "Use up/down arrow to move up & down\nUse ENTER to select given option"

# Add Contact Info strings
NameAndCityInfo = "Name and City must contain only lower/upper case alphabetic character and spaces!\n"
EnterName = "Enter Name: "
EnterCity = "Enter City: "
EnterPhoneNumber = "Enter Phone Number: "
ContactAdded = f"{Fore.GREEN}*** Contact added! ***{Fore.GREEN}{Fore.WHITE}"

MenuOptions = ["Search by...", "All Contacts",
                  "Add Contact", "Delete Contact", "Edit Contact"]


#### INVALID INPUT
InvalidName = f"Name must contain only lower, upper or mixed case alphabetic character and spaces!"
InvNameLen = f"Name length must be between 2-50 charachters!"

InvalidCity = f"City must contain only lower, upper or mixed case alphabetic character and spaces!"
InvNameLen = f"City length must be between 2-50 charachters!"

InvalidPhone = f"Phone number must contains only digits!"
InvPhoneLen = f"Phone number must be between 5-15"

#### Exceptions
def ContactExist(contactName,contactCity,contactNumber):
 return f"{Fore.YELLOW}Contact: {contactNumber} - {contactName}|{contactCity} already exists!{Fore.YELLOW}{Fore.WHITE}"