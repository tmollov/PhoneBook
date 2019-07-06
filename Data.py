import json, os
import Enum
import uuid
import pickle
from Exception import AddException

class Person:
    def __init__(self,name,city,phoneNumber):
        self.guid = uuid.uuid4().urn.replace("urn:uuid:","")
        self.name = name
        self.city = city
        self.phoneNumber = phoneNumber
    
    def Compare(self,otherPerson):
        return True if otherPerson.name == self.name and \
           otherPerson.city == self.city and \
           otherPerson.phoneNumber == self.phoneNumber \
        else False

def GetDb():
    if os.path.isfile('db.p') :
        return pickle.load( open( "db.p", "rb" ) )
    else:
        return []

def SaveDb(data): 
    pickle.dump(data, open( "db.p", "wb" ) )

def AddContact(name,city,number):
    person = Person(name,city,number)
    data = GetDb()
    if IsPersonInDb(data,person):
        return AddException(Enum.ContactExist(name,city,number))
    else:
        data.append(person)
    SaveDb(data)

def DeleteContact(guid):
    data = GetDb()
    try:
        update = list(filter(lambda x : x.guid != guid,data))
        SaveDb(update)
        return True
    except Exception:
        return False

def UpdateContact(personIndex,name,city,number):
    data = list(GetDb())
    try:
        data[personIndex].name = name
        data[personIndex].city = city
        data[personIndex].phoneNumber = number
        SaveDb(data)
        return True
    except Exception:
        return False

def IsPersonInDb(data,personObj):
    for person in data:
        if person.Compare(personObj):
            return True
    return False

def GetPersonsWith(selection,by):
    data = GetDb()
    result = None
    if selection == Enum.SearchByName:
        result =  list(filter(lambda n: n.name == by,data))
    elif selection == Enum.SearchByCity:
        result = list(filter(lambda n: n.city == by,data))
    elif selection == Enum.SearchByNumber:
        result = list(filter(lambda n: n.phoneNumber == by,data))
    return result