import json
import os

def make_dir(path, allow_existing=False):
    if not allow_existing and os.path.exists(path):
        raise Exception("Directory already exists: " + path)
    try:
        os.makedirs(path)
    except FileExistsError:
        if allow_existing:
            return
        raise Exception("Directory already exists")
    except Exception as e:
        raise Exception("Error creating director: " + path + ": " + str(e))

def explode_list(list_obj, name):
    make_dir(name)
    for i in range(len(list_obj)):
        explode_object(list_obj[i], os.path.join(name, str(i)))

def explode_dict(dict_obj, name):
    make_dir(name)

    for k in dict_obj.keys():
        explode_object(dict_obj[k], os.path.join(name, str(k)))

def explode_object(obj, name):
    if type(obj) is list:
        explode_list(obj, name)
    if type(obj) is dict:
        explode_dict(obj, name)
    else:
        # Write any non-collection item to hd
        fname = str(name) + ".txt"
        parent_dir, basename = os.path.split(name)

        # Debug output
        # print("=" * 80)
        # print("type: " + str(type(obj)))
        # print("Writing: '" + fname + "'")

        make_dir(parent_dir, allow_existing=True)
        open(fname, "w").write(json.dumps(str(obj)))
    
def explode_json(json_str, name):

    explode_object(json.loads(json_str), name)


    
    