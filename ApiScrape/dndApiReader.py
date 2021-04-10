import requests
import json
import os

print("starting read from DND Api")
base_url = 'https://www.dnd5eapi.co'

def GetRaces():
    r = requests.get(base_url + '/api/races')

    r_json = json.loads(r.content)
    os.chdir(os.getcwd() + "/Races")
    for race in r_json["results"]:
        stored_data = {}
        sing_race = requests.get(base_url + race["url"])
        sing_race_json = json.loads(sing_race.content)

        stored_data["name"] = sing_race_json["name"]
        stored_data["speed"] = sing_race_json["speed"]
        stored_data["abilityBonuses"] =[]
        i = 0
        for i in range(len(sing_race_json["ability_bonuses"])):
            stored_data["abilityBonuses"].append( {"name" : sing_race_json["ability_bonuses"][i]["ability_score"]["name"], "bonus" : sing_race_json["ability_bonuses"][i]["bonus"]} )
        stored_data["alignment"] = sing_race_json["alignment"]
        stored_data["age"] = sing_race_json["age"]
        stored_data["size"] = sing_race_json["size"]
        stored_data["sizeDescription"] = sing_race_json["size_description"]
        if len(sing_race_json["subraces"]) > 0:
            subList = []
            for i in range(len(sing_race_json["subraces"])):
                subStore = {}
                subrace = requests.get(base_url + sing_race_json["subraces"][i]["url"])
                subrace_json = json.loads(subrace.content)
                subStore["name"] = subrace_json["name"]
                subStore["description"] = subrace_json["desc"]
                subStore["abilityBonuses"] = []
                for j in range(len(subrace_json["ability_bonuses"])):
                    subStore["abilityBonuses"].append( {"name" : subrace_json["ability_bonuses"][j]["ability_score"]["name"], "bonus" : subrace_json["ability_bonuses"][j]["bonus"]} )
                subList.append(subStore)

            stored_data["subRaces"] = subList
        else:
            stored_data["subRaces"] = []

        f = open(race["name"] + ".json", "w")
        f.write(json.dumps(stored_data, indent=2))
        f.close()
        print("finished " + race["name"])
    os.chdir("../")

def GetClasses():
    r = requests.get(base_url + '/api/classes')

    r_json = json.loads(r.content)

    os.chdir(os.getcwd() + "/Classes")
    for rClass in r_json["results"]:
        stored_data = {}
        sing_rClass = requests.get(base_url + rClass["url"])
        sing_rClass_json = json.loads(sing_rClass.content)

        stored_data["name"] = sing_rClass_json["name"]
        stored_data["healthDie"] = sing_rClass_json["hit_die"]
        stored_data["savingThrows"] = []
        for i in range(len(sing_rClass_json["saving_throws"])):
            stored_data["savingThrows"].append( { "name" : sing_rClass_json["saving_throws"][i]["name"] } )
        stored_data["subclasses"] = []
        for i in range(len(sing_rClass_json["subclasses"])):
            store_sub = {}
            subC = requests.get(base_url + sing_rClass_json["subclasses"][i]["url"])
            subC_json = json.loads(subC.content)

            store_sub["name"] = subC_json["name"]
            store_sub["subclassFlavor"] = subC_json["subclass_flavor"]
            store_sub["description"] = subC_json["desc"]

            stored_data["subclasses"].append(store_sub)


        f = open(rClass["name"] + ".json", "w")
        f.write(json.dumps(stored_data, indent=2))
        f.close()
        print("finished " + rClass["name"])


os.chdir(os.getcwd() + "/ApiScrape")

GetRaces()
GetClasses()

#print(r_json["count"])

#print(json.dumps(r_json, indent=2))