




import json
import os

customer = os.getenv("CUSTOMER")
instance = os.getenv("INSTANCE")
geography = os.getenv("GEOGRAPHY")
realms = os.getenv("REALMS")
env_base_dir = "deployment"

def read_realms():
    base_path= os.path.join(env_base_dir or '', customer or '', instance or '', geography or '', "realms" )
    names = []
    seen = set()
    for filename in os.lisdir(base_path):
        file_path=os.path.join(base_path, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data=yaml.safe_load(f)
                    val = data.get('name')
                    if val not in seen:
                        names.append(val)
                        seen.add(val)
    return names:


def get_realms(realms_str):
    if not realms:
        raise ValueError("REALMS environment variable is empty.")
	if realms_str.strip() == '*':
		realms=read_realm()
		return realms
	else:
		return realm_str
	
def main():
    realms_list = get_realms(realms)
    print(realms_list)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}")


 