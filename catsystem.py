import requests
import json
import webbrowser
import credentials

from pprint import pprint


def get_json_content_from_response(response):
    try:
       content = response.json()
    except json.decoder.JSONDecodeError:
       print("Unknown format", response.text)
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

print("Hey, sign in !")


userId = "agh2m"
name = "Artur"

print("Welcome " + name)
favouriteCats = get_favourite_cats(userId)
print("Your favourite cats are ", favouriteCats)
randomCat = get_random_cat()
print("You draw a cat: ", randomCat["url"])

addToFavourites = input ("Do you want add this cat to favourites? Y/N")

if (addToFavourites.upper () == "Y"):
    resultFromAddingFavouriteCat = add_favourite_cat (randomCat  ["id"], userId)
    newlyAddedCatInfo = {resultFromAddingFavouriteCat ["id"] : randomCat["url"]}
else:
    print ("Such a shame, cat will be sad :( ")



favouriteCatsById = {
    favouriteCat ["id"] : favouriteCat ["image"]["url"]
    for favouriteCat in favouriteCats
    }

print (favouriteCatsById)

favouriteCatId = input ("Which cat you want to delete? ")

print (remove_favourite_cat(userId, favouriteCatId))


