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

def IsPersonInDb(data,personObj):
    for person in data:
        if person.Compare(personObj):
            return True
    return False