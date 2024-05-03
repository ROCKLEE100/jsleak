import requests # This is used to send request to the web application.
import re # This is used to extract our api/secret infromation from the web application/source.
import json

def getText(filename):
       with open(filename,'r') as file:
              urls = file.read().split()
       return urls


def sendRequest(urls):
       for url in urls:
               print(url)
               response = requests.get(url).text
               with open('regex.json', 'r') as file:
                     json_data = json.load(file)
               for values in json_data:
                      result = re.findall(values['pattern'], response)
                      if len(result) > 0:
                               print(f"{values['apiName']} has been found in the response")
                               print(f"Value is {values['pattern']}")
                      else:
                             print(f"nothing found")

file = input("Enter a text file: ")
urls = getText(file)
sendRequest(urls)
