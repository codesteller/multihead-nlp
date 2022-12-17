import os
import json


# write a function to get all the json files in the directory and subdirectories
def get_all_json_files(path):
    json_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files   

# write a function to get all the json objects in a json file
# and return a list of json objects
def get_all_json_objects(json_file):
    json_objects = []
    with open(json_file, 'r') as fptr:
        data = json.load(fptr)
        json_objects.append(data)
    return json_objects 
