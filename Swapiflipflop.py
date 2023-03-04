import json
import xmltodict
import requests

# RestAPI request and parsing into dictionary object
#webRequest=requests.get('https://swapi.dev/api/people/')
#peopleObj=webRequest.json()


# Open both files, source as read only and destiantion as write
peopleFileJson = open('SwapiPoeple.json','r')
peopleFileXml = open('SwapiPeople.xml','w')

#load the file contents into a dictionary object
peopleObj = json.load(peopleFileJson)

#creating a destination dictionary object with a single root to match XML structure
poepleResult={'People':{}}

#Cleaning up some of the extra json data 
for p in peopleObj['results']:
    #converting the name data into a key to match XML structure.
    name=p.pop('name')
    poepleResult['People'][f'{name}']=p


#writing to XML file.
peopleFileXml.write(xmltodict.unparse(poepleResult,pretty=True))
peopleFileXml.close