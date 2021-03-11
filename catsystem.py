import requests
import json
import webbrowser
import credentials

from pprint import pprint


def get_json_content_from_response(response):
    try:
       content = response.json()
    except json.decoder.JSONDecodeError:
       print("Niepoprawny format", response.text)
    else:
       return content
    

def get_favourite_cats(userId):
    params = {
        "sub_id" : userId
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites/', params,
                 headers=credentials.headers)
    
    return get_json_content_from_response(r)

def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search',
                 headers=credentials.headers)
    
    return get_json_content_from_response(r) [0]

def add_favourite_cat(catId, userId):
    catData = {
        "image_id" : catId,
        "sub_id" : userId,
                }
    r = requests.post('https://api.thecatapi.com/v1/favourites/', json = catData,
                 headers=credentials.headers)
    
    return get_json_content_from_response(r)

def remove_favourite_cat (userId, favourtieCatId):
        r = requests.delete('https://api.thecatapi.com/v1/favourites/'+favouriteCatId,
                 headers=credentials.headers)
    
        return get_json_content_from_response(r)

print("Hej, zaloguj się - podaj login i hasło")
#pobranie loginu i hasla
#sprawdzamy czy login i haslo jest poprawne
#logowanie zaszlo poprawnie
#pobieramy z bazy danych userId i name - nazwe użytkownika

userId = "agh2m"
name = "Artur"

print("Witaj " + name)
favouriteCats = get_favourite_cats(userId)
print("Twoje ulubione kotki to ", favouriteCats)
randomCat = get_random_cat()
print("Wylosowano kotka: ", randomCat["url"])

addToFavourites = input ("Czy chcesz go dodać do ulubionych? T/N")

if (addToFavourites.upper () == "T"):
    resultFromAddingFavouriteCat = add_favourite_cat (randomCat  ["id"], userId)
    newlyAddedCatInfo = {resultFromAddingFavouriteCat ["id"] : randomCat["url"]}
else:
    print ("No to lipa, kotek będzie smutny :( ")



favouriteCatsById = {
    favouriteCat ["id"] : favouriteCat ["image"]["url"]
    for favouriteCat in favouriteCats
    }

print (favouriteCatsById)

favouriteCatId = input ("Którego kota chcesz usunąć ? ")

print (remove_favourite_cat(userId, favouriteCatId))


