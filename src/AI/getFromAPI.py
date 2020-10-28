import requests
import cardFinder
import time

URL = "http://127.0.0.1:21337/positional-rectangles"


def getJsonFromAPI():
    r = requests.get(url = URL)
    data = r.json()
    myCards = []
    for i in data["Rectangles"]:
        if (i["CardCode"] != "face") and i["LocalPlayer"] == True:
            myCards.append(cardFinder.fromIDToName(i["CardCode"]))
    return myCards

if __name__ == '__main__':
    while 1:
        myCards = getJsonFromAPI()
        print(myCards)
        time.sleep(1)
