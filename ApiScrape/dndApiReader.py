import requests
import json
import os
import time

print("starting read from DND Api")
base_url = 'https://www.dnd5eapi.co'


def HitApi(urlExt):
    r = requests.get(base_url + urlExt)
    r_json = json.loads(r.content)
    return r_json

def GetRaces():
    final_file = []
    r_json = HitApi('/api/races')
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

        final_file.append(stored_data)
        print("finished " + race["name"])

    return final_file

def GetClasses():
    final_file = []
    r_json = HitApi('/api/classes')

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

        final_file.append(stored_data)
        print("finished " + rClass["name"])

    return final_file

def GetSubRace():
    final_file = []
    sr_json = HitApi('/api/subraces')

    for subR in sr_json["results"]:
        stored_data = {}
        sing_sr_json = HitApi(subR["url"])

        stored_data["name"] = sing_sr_json["name"]
        stored_data["race"] = sing_sr_json["race"]["name"]
        stored_data["description"] = sing_sr_json["desc"]
        stored_data["attributeMods"] = []
        for i in range(len(sing_sr_json["ability_bonuses"])):
            stored_data["attributeMods"].append( {"name" : sing_sr_json["ability_bonuses"][i]["ability_score"]["name"], "value" : sing_sr_json["ability_bonuses"][i]["bonus"]} )
        
        final_file.append(stored_data)
        print("finished " + sing_sr_json["name"])


    return final_file        

def GetAttributes():
    final_file = []
    a_json = HitApi('/api/ability-scores')

    for sing_a in a_json["results"]:
        a = HitApi(sing_a["url"])
        data = {}

        data["name"] = a["full_name"]
        data["abreviation"] = a["name"]
        data["description"] = a["desc"]
        data["skills"] = []
        for i in range(len(a["skills"])):
            data["skills"].append(a["skills"][i]["name"])

        final_file.append(data)
        print("finished " + a["name"])

    return final_file

def GetSkills():
    final_file = []
    s_json = HitApi('/api/skills')

    for sing_s in s_json["results"]:
        data = {}
        s = HitApi(sing_s["url"])
        data["name"] = s["name"]
        data["description"] = s["desc"]
        data["attribute"] = s["ability_score"]["name"]

        final_file.append(data)
        print("finished " + s["name"])

    return final_file

def GetBackgrounds():
    final_file = []
    b_json = HitApi('/api/backgrounds')

    for sing_b in b_json["results"]:
        data = {}
        b = HitApi('/api/backgrounds/' + sing_b["index"])

        data["name"] = b["name"]
        data["startingProficiencies"] = []
        for i in range(len(b["starting_proficiencies"])):
            data["startingProficiencies"].append(b["starting_proficiencies"][i]["name"].split()[1])
        data["abilities"] = []
        data["abilities"].append( { "name" : b["feature"]["name"], "description" : b["feature"]["desc"] } )
        data["personality"] = b["personality_traits"]["from"]
        data["ideals"] = []
        for i in range(len(b["ideals"]["from"])):
            store = {}
            store["description"] = b["ideals"]["from"][i]["desc"]
            store["alignment"] = []
            for j in range(len(b["ideals"]["from"][i]["alignments"])):
                store["alignment"].append(b["ideals"]["from"][i]["alignments"][j]["name"])
            data["ideals"].append(store)
        data["bonds"] = b["bonds"]["from"]
        data["flaws"] = b["flaws"]["from"]

        final_file.append(data)
        

    return final_file

def GetFeatures():
    to_return = []
    fea_json = HitApi("/api/features")
    for sing_fea in fea_json["results"]:
        data = {}
        fea = HitApi(sing_fea["url"])
        data["name"] = fea["name"]
        data["requirement"] = [{ "type" : "class", "reqName" : [fea["class"]["name"]], "level" : fea["level"] if "level" in fea else 0 }]
        for i in range(len(fea["prerequisites"])):
            if(fea["prerequisites"][i]["type"] == "Spell"):
                data['requirement'].append( { "type" : "spell", "reqName" : ["Eldritch Blast"] } )
            elif(fea["prerequisites"][i]["type"] == "feature"):
                reqFea = HitApi(fea["prerequisites"][i]["feature"])
                data['requirement'].append( { "type" : "feature", "reqName" : reqFea["name"] } )
        data["description"] = fea["desc"]
        if("group" in fea):
            data["group"] = fea["group"]

        to_return.append(data)
        print("finished " + fea["name"])
    return to_return

def GetTraits():
    to_return = []
    trait_json = HitApi("/api/traits")
    for sing_tra in trait_json["results"]:
        data = {}
        t = HitApi(sing_tra["url"])

        data["name"] = t["name"]
        data["requirement"] = [{ "type" : "race" if len(t["races"]) > 0 else "subrace", "reqNames" : [] }]
        for i in range(len(t["races"])):
            data["requirement"][0]["reqNames"].append(t["races"][i]["name"])
        for i in range(len(t["subraces"])):
            data["requirement"][0]["reqNames"].append(t["subraces"][i]["name"])
        if(len(t["proficiencies"]) > 0):
            data["proficiencies"] = []
            for i in range(len(t["proficiencies"])):
                data["proficiencies"].append(t["proficiencies"][i]["name"])
        data["description"] = t["desc"]

        to_return.append(data)
        print("finished " + t["name"])

    return to_return

def GetAbilities():
    #Features
    final_file = []
    feas= GetFeatures()
    for fea in feas:
        final_file.append(fea)
    
    tras = GetTraits()
    for tra in tras:
        final_file.append(tra)


    return final_file

os.chdir(os.getcwd() + "/ApiScrape")

start = time.time()
rules = {}
rules["name"] = "DnD 5E"
rules["races"] = GetRaces()
rules["classes"] = GetClasses()
rules["subRaces"] = GetSubRace()
rules["attributes"] = GetAttributes()
rules["skills"] = GetSkills()
rules["backgrounds"] = GetBackgrounds()
rules["abilities"] = GetAbilities()
f = open("Rules.json", "w")
f.write(json.dumps(rules, indent=2))
f.close()
end = time.time()

print(end - start)

#print(r_json["count"])

#print(json.dumps(r_json, indent=2))