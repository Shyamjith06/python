# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import os

def get_realmnames:
    root="deployment"
    basepath=os.path.join(root or '', customer or '', instance,geography, "realms")
    for filename in os.listdir(basepath):
        print(filename)
    return "hii"

def get_realm(realm_input):
    if not realm_input:
        print("please input realm")
    if realm_input != '*':
        return realm_input
    else:
        realms=get_realmnames()
        return realms

def main():
    realm=get_realm(realm_input)
        
    
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)