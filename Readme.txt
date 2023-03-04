Practicing for the Devnet. 
Quick python script to convert Json to Python dictionary,some minor parsing, then converted to XML and written to file.
The Json data is pulled from the Star Wars Api at swapi.dev or loaded from a file with the same data

The XmlToDict module was having trouble with the strucutre of the Json file, even after cleaning up the extra data outside of the "results" key
Xmltodict.unparse failed when dealing with multiple duplicated dictionaries inside the "results" value list
I wrote a quick for loop to fix this issue by seperating each person into their own key value pair indexed by their name.