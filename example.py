"""
Simple example script that queries UCM via AXL and creates a place in ControlHub based on the device
"""
import requests
import sys
import os

from endpoint_apis.endpoint_api import get_endpoint_details

API_TOKEN = os.environ.get("WEBEX_API_TOKEN", None)
if not API_TOKEN:
    print("WARNING: NO WEBEX API KEY SET")

def create_place_in_control_hub(place_name):
    """
    Creates a place in control hub named "place_name"
    """
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.post("https://api.ciscospark.com/v1/places", headers=headers, data={"displayName": place_name})
    print(f"Response status/msg: {response.status_code} |  {response.text}")


if __name__ == '__main__':
    ## Load the arguments via Command Line

    ucm_username = sys.argv[1]
    ucm_password = sys.argv[2]
    ucm_server = sys.argv[3]

    devices = get_endpoint_details(ucm_username, ucm_password, ucm_server)

    if devices:
        print(devices)
        for device in devices:
            place = device["description"]
            print(place)
            create_place_in_control_hub(place)
            break
