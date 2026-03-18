# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import os
import yaml
customer = os.getenv("CUSTOMER")
instance = os.getenv("INSTANCE")
geography = os.getenv("GEOGRAPHY")
realmss = os.getenv("REALMS")
env_base_dir = "deployment"


def get_realmnames():
    root="deployment"
    basepath=os.path.join(root or '', customer or '', instance,geography, "realms")
    relm_list=[]
    for filename in os.listdir(basepath):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            file_path=os.path.join(basepath,filename)
            with open(file_path, 'r', encoding="utf-8") as f:
                data=yaml.safe_load(f)
                r=data.get("name")
                relm_list=relm_list.append(r)
    return relm_list
        
        


def get_realm(realm_input):
    if not realm_input:
        print("please input realm")
    if realm_input != '*':
        return realm_input
    else:
        realms=get_realmnames()
        return realms

def main():
    realm=get_realm(realmss)
    print(realm)
        
    
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)