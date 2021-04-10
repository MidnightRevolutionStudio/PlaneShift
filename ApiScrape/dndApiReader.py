import requests
import json
import os

print("starting read from DND Api")
base_url = 'https://www.dnd5eapi.co'


def HitApi(urlExt):
    r = requests.get(base_url + urlExt)
    r_json = json.loads(r.content)
    return r_json

def GetRaces():
    r_json = HitApi('/api/races')
    os.chdir(os.getcwd() + "/Races")
    for race in r_json["results"]:
        stored_data = {}
        sing_race_json = HitApi(race["url"])

        stored_data["name"] = sing_race_json["name"]
        stored_data["speed"] = sing_race_json["speed"]
        stored_data["attributeMods"] =[]
        i = 0
        for i in range(len(sing_race_json["ability_bonuses"])):
            stored_data["attributeMods"].append( {"name" : sing_race_json["ability_bonuses"][i]["ability_score"]["name"], "bonus" : sing_race_json["ability_bonuses"][i]["bonus"]} )
        stored_data["alignment"] = sing_race_json["alignment"]
        stored_data["age"] = sing_race_json["age"]
        stored_data["size"] = sing_race_json["size"]
        stored_data["sizeDescription"] = sing_race_json["size_description"]
        if len(sing_race_json["subraces"]) > 0:
            subList = []
            for i in range(len(sing_race_json["subraces"])):
                subrace_json = HitApi(sing_race_json["subraces"][i]["url"])
                subList.append(subrace_json["name"])

            stored_data["subRaces"] = subList
        else:
            stored_data["subRaces"] = []

        f = open(race["name"] + ".json", "w")
        f.write(json.dumps(stored_data, indent=2))
        f.close()
        print("finished " + race["name"])
    os.chdir("../")

def GetClasses():
    r_json = HitApi('/api/classes')

    os.chdir(os.getcwd() + "/Classes")
    for rClass in r_json["results"]:
        stored_data = {}
        sing_rClass_json = HitApi(rClass["url"])

        stored_data["name"] = sing_rClass_json["name"]
        stored_data["healthDie"] = sing_rClass_json["hit_die"]
        stored_data["savingThrows"] = []
        for i in range(len(sing_rClass_json["saving_throws"])):
            stored_data["savingThrows"].append( { "name" : sing_rClass_json["saving_throws"][i]["name"] } )
        stored_data["subclasses"] = []
        for i in range(len(sing_rClass_json["subclasses"])):
            store_sub = {}
            subC_json = HitApi(sing_rClass_json["subclasses"][i]["url"])

            store_sub["name"] = subC_json["name"]
            store_sub["subclassFlavor"] = subC_json["subclass_flavor"]
            store_sub["description"] = subC_json["desc"]

            stored_data["subclasses"].append(store_sub)


        f = open(rClass["name"] + ".json", "w")
        f.write(json.dumps(stored_data, indent=2))
        f.close()
        print("finished " + rClass["name"])

    
    os.chdir("../")

def GetSubRace():
    sr_json = HitApi('/api/subraces')

    os.chdir(os.getcwd() + "/Subraces")
    for subR in sr_json["results"]:
        stored_data = {}
        sing_sr_json = HitApi(subR["url"])

        stored_data["name"] = sing_sr_json["name"]
        stored_data["race"] = sing_sr_json["race"]["name"]
        stored_data["description"] = sing_sr_json["desc"]
        stored_data["attributeMods"] = []
        for i in range(len(sing_sr_json["ability_bonuses"])):
            stored_data["attributeMods"].append( {"name" : sing_sr_json["ability_bonuses"][i]["ability_score"]["name"], "value" : sing_sr_json["ability_bonuses"][i]["bonus"]} )
        

        f = open(sing_sr_json["name"] + ".json", "w")
        f.write(json.dumps(stored_data, indent=2))
        f.close()
        print("finished " + sing_sr_json["name"])

    
    os.chdir("../")        

def GetAttributes():
    a_json = HitApi('/api/ability-scores')
    os.chdir(os.getcwd() + "/Attributes")

    for sing_a in a_json["results"]:
        a = HitApi(sing_a["url"])
        data = {}

        data["name"] = a["full_name"]
        data["abreviation"] = a["name"]
        data["description"] = a["desc"]
        data["skills"] = []
        for i in range(len(a["skills"])):
            data["skills"].append(a["skills"][i]["name"])

        f= open(a["full_name"] + ".json", "w")
        f.write(json.dumps(data, indent=2))
        f.close()
        print("finished " + a["name"])

    os.chdir("../")

def GetSkills():
    os.chdir(os.getcwd() + "/Skills")
    s_json = HitApi('/api/skills')

    for sing_s in s_json["results"]:
        data = {}
        s = HitApi(sing_s["url"])
        data["name"] = s["name"]
        data["description"] = s["desc"]
        data["attribute"] = s["ability_score"]["name"]

        f = open(s["name"] + ".json", "w")
        f.write(json.dumps(data, indent=2))
        f.close()
        print("finished " + s["name"])

    os.chdir("../")


os.chdir(os.getcwd() + "/ApiScrape")

#GetRaces()
#GetClasses()
#GetSubRace()
#GetAttributes()
GetSkills()

#print(r_json["count"])

#print(json.dumps(r_json, indent=2))