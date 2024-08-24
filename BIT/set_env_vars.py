# set_env_vars.py
import json

def parse_deploy_json_and_get_env_vars(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    ipaddress = data['ipaddress']
    username = data['username']
    hostname = data['hostname']

    env_var_name = f'{ipaddress}-{username}-{hostname}'.replace('.', '_')
    env_var_value = f'{ipaddress}-{username}-{hostname}'

    # Print in a key=value format for Jenkins to capture
    print(f'{env_var_name}={env_var_value}')

if __name__ == "__main__":
    import sys
    parse_deploy_json_and_get_env_vars(sys.argv[1])
