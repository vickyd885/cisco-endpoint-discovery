# Cisco Device Discovery from UCM

Quick example API to show how you can query UCM using AXL and create spaces in Cisco ControlHub. 

### Usage

Setup: Please have Python3 and PHP installed on the machine you are running this on.


```
git clone {repository_url}  # clone the repo to your machine
virtualenv env # makes a local environment to load libraries into 
pip install -r requirements.txt

python3 example.py {ucm_username} {ucm_password} {ucm_server}
```

You'll also need a token to use to create the place in controlhub and can be fetched from https://developer.cisco.com

