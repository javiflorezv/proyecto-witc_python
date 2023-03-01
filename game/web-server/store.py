import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json() #el formato json lo va a tranformar a una lista de formato python y los elemento seran 
    for category in categories:                      # dicionarios y se puede hacer interaciones.
      print(category['name'])