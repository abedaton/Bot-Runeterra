import json
import glob

cardID = "01SI026"


def fromIDToName(cardID):
    allJsons = glob.glob("API/set*.json")

    for jsonFile in allJsons:
        realOne = open(jsonFile, "r", encoding="utf8")
        data = json.load(realOne)
        realOne.close()
        for i in range(len(data)):
            if data[i]["cardCode"] == cardID:
                return data[i]["name"]



if __name__ == "__main__":
    print(fromIDToName(cardID))
