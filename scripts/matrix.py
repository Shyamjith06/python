




import json
import os
import yaml

customer = os.getenv("CUSTOMER")
instance = os.getenv("INSTANCE")
geography = os.getenv("GEOGRAPHY")
realms = os.getenv("REALMS")
env_base_dir = "deployment"

def read_realms():
    base_path= os.path.join(env_base_dir or '', customer or '', instance or '', geography or '', "realms" )
    names = []
    seen = set()
    for filename in os.listdir(base_path):
        file_path=os.path.join(base_path, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data=yaml.safe_load(f)
                    val = data.get('name')
                    if val not in seen:
                        names.append(val)
                        seen.add(val)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    return names


def get_realms(realms_str):
    if not realms_str:
        raise ValueError("REALMS environment variable is empty.")
    if realms_str.strip() == '*':
        realms = read_realms()
        return realms
    return realms_str


def main():
    realms_list = get_realms(realms)
    #print(realms_list)
    matrix = {"include": realms_list}
    matrix_json = json.dumps(matrix)
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        try:
            with open(github_output, 'a', encoding='utf-8') as fh:
                fh.write(f"matrix={matrix_json}\n")
        except Exception as e:
            print(f"Warning: failed to write GITHUB_OUTPUT: {e}")
    print(matrix_json)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}")

