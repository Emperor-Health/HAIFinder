import json
import urllib.request
import ssl 
from collections import namedtuple

class TrialLocation(object):
    trial_id = ""
    site_name = ""
    city = ""
    state_province = ""
    lat = ""
    lon = ""
    
    # The class "constructor" - It's actually an initializer 
    def __init__(self, trial_id, site_name, city, state_province, lat, lon):
        self.trial_id = trial_id
        self.site_name = site_name
        self.city = city
        self.state_province = state_province
        self.lat = lat
        self.lon = lon
 
class Trial(object):
    trial_id = ""
    trial_name = ""
    trial_locations = []


def get_CTJSONData(trial_id):
    context = ssl._create_unverified_context() 
    with urllib.request.urlopen("https://clinicaltrialsapi.cancer.gov/v1/clinical-trial/" + trial_id, 
        context=context) as url:
        #data = json.dumps(url.read().decode(), indent = 4)
        data = json.loads(url.read().decode())
return data

# TODO: fix unverified CERT --import certifi
# https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error

def get_locations(trial_id):
    locations = []
    data = get_CTJSONData(trial_id)   
    for x in range(0, len(data["sites"])):
        t = TrialLocation()
        t.trial_id = data["nct_id"]
        çdata["sites"][x]["org_name"],
            data["sites"][x]["org_city"],
            data["sites"][x]["org_state_or_province"],
            'No_Lat',
            'No_Lon'
            )

        try:
            print( data["sites"][x]["org_coordinates"]["lat"])
            t.lat = str(data["sites"][x]["org_coordinates"]["lat"])
        except KeyError:
            t.lat = 'null'

        try:
            print(data["sites"][x]["org_coordinates"]["lon"])
            t.lon = str(data["sites"][x]["org_coordinates"]["lon"])
        except KeyError:
            t.lon = 'null'
        locations.append(t)   
    retun locations
        
     #print(data)
