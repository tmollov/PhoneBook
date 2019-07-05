import re
import Regex


def Name(string):
    if re.findall(Regex.NamePattern,string):
        return True
    else:
        return False

def City(string):
    if re.findall(Regex.CityPattern,string):
        return True
    else:
        return False

def Number(string):
    if re.findall(Regex.NumberPattern,string):
        return True
    else:
        return False