import requests
import json
import os

print("starting read from DND Api")
base_url = 'https://www.dnd5eapi.co'

def GetRaces():
    r = requests.get(base_url + '/api/races')

    r_json = json.loads(r.content)
    os.chdir(os.getcwd() + "/ApiScrapes")
    os.chdir(os.getcwd() + "/Races")
    for race in r_json["results"]:
        stored_data = {}
        sing_race = requests.get(base_url + race["url"])
        sing_race_json = json.loads(sing_race.content)

        stored_data["Name"] = sing_race_json["name"]
        stored_data["Speed"] = sing_race_json["speed"]
        stored_data["AbilityBonuses"] =[]
        i = 0
        for i in range(len(sing_race_json["ability_bonuses"])):
            stored_data["AbilityBonuses"].append( {"Name" : sing_race_json["ability_bonuses"][i]["ability_score"]["name"], "Bonus" : sing_race_json["ability_bonuses"][i]["bonus"]} )
        stored_data["Alignment"] = sing_race_json["alignment"]
        stored_data["Age"] = sing_race_json["age"]
        stored_data["Size"] = sing_race_json["size"]
        stored_data["SizeDescription"] = sing_race_json["size_description"]
        if len(sing_race_json["subraces"]) > 0:
            subList = []
            for i in range(len(sing_race_json["subraces"])):
                subStore = {}
                subrace = requests.get(base_url + sing_race_json["subraces"][i]["url"])
                subrace_json = json.loads(subrace.content)
                subStore["Name"] = subrace_json["name"]
                subStore["Description"] = subrace_json["desc"]
                subStore["AbilityBonuses"] = []
                for j in range(len(subrace_json["ability_bonuses"])):
                    subStore["AbilityBonuses"].append( {"Name" : subrace_json["ability_bonuses"][j]["ability_score"]["name"], "Bonus" : subrace_json["ability_bonuses"][j]["bonus"]} )
                subList.append(subStore)

            stored_data["SubRaces"] = subList
        else:
            stored_data["SubRaces"] = []

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

        stored_data["Name"] = sing_rClass_json["name"]
        stored_data["HealthDie"] = sing_rClass_json["hit_die"]
        stored_data["SavingThrows"] = []
        for i in range(len(sing_rClass_json["saving_throws"])):
            stored_data["SavingThrows"].append( { "Name" : sing_rClass_json["saving_throws"][i]["name"] } )
        stored_data["Subclasses"] = []
        for i in range(len(sing_rClass_json["subclasses"])):
            store_sub = {}
            subC = requests.get(base_url + sing_rClass_json["subclasses"][i]["url"])
            subC_json = json.loads(subC.content)

            store_sub["Name"] = subC_json["name"]
            store_sub["SubclassFlavor"] = subC_json["subclass_flavor"]
            store_sub["Description"] = subC_json["desc"]

            stored_data["Subclasses"].append(store_sub)


        f = open(rClass["name"] + ".json", "w")
        f.write(json.dumps(stored_data, indent=2))
        f.close()
        print("finished " + rClass["name"])


os.chdir(os.getcwd() + "/ApiScrape")

GetRaces()
GetClasses()

#print(r_json["count"])

#print(json.dumps(r_json, indent=2))