import re
import Regex


def Name(string,pattern = Regex.NamePattern):
    if re.findall(pattern,string):
        return True
    else:
        return False

def City(string,pattern = Regex.CityPattern):
    if re.findall(pattern,string):
        return True
    else:
        return False

def Number(string,pattern = Regex.NumberPattern):
    if re.findall(pattern,string):
        return True
    else:
        return False