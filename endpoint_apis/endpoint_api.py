import json
import subprocess
import os

cwd = os.getcwd()

def get_endpoint_details(username, password, server):
    """
    Given UCM details, return info about all devices registered on UCM
    """
    result = subprocess.run(
        ['php', f'{cwd}/endpoint_apis/check_endpoints.php', username, password, server],    # program and arguments
        stdout=subprocess.PIPE,  # capture stdout
        check=False               # raise exception if program fails
    )
    #print(result.stdout.decode("utf-8"))         # result.stdout contains a byte-string
    try:
        return json.loads(result.stdout.decode("utf-8"))
    except Exception as e:
        print(f"Error in fetching devices: {e}")
    return None

