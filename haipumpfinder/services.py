import json
import urllib.request
import ssl 
from collections import namedtuple

#returns the json data
def get_CTJsonData(trial_id):
    context = ssl._create_unverified_context()   
    url1 = "https://clinicaltrialsapi.cancer.gov/v1/clinical-trial/" + trial_id  
    with urllib.request.urlopen(url1 , 
        context=context) as url:
            data = json.loads(url.read().decode())
            return data


class TrialLocation:
   def __init__(self, trial_id, site_name, city, state, lat, lon):
        self.trial_id = trial_id
        self.site_name = site_name
        self.city = city
        self.state_province = state
        self.lat = lon
        self.lon = lat


class Trial(object):
    def __str__(self):
        return self.name
    @staticmethod
    def locations(trial_id):
        locations = []
        trial_id = trial_id
        data = get_CTJsonData(trial_id)
            #print(len(data["sites"]));
        for x in range(0, len(data["sites"])):
            idr = data["nct_id"]
            namer = data["sites"][x]["org_name"]
            cityr = data["sites"][x]["org_city"]
            state_provincer = data["sites"][x]["org_state_or_province"]
            
            try:
            #print( data["sites"][x]["org_coordinates"]["lat"])
                latr = str(data["sites"][x]["org_coordinates"]["lat"])
            except KeyError:
                latr = 'null'
            try:
                #print(data["sites"][x]["org_coordinates"]["lon"])
                lonr = str(data["sites"][x]["org_coordinates"]["lon"])
            except KeyError:
                lonr = 'null'
            t = TrialLocation(idr, namer, cityr, state_provincer, latr, lonr)
            #print("Trial ID: " + t.trial_id)
            #locations.append(t[:]) #why not?
            locations.append(t)
            #print(len(locations))
        return locations
    id = ""
    name = ""
   

def get_trial(trial_id):
        trial = Trial()  
        trial.locations(trial_id) 
        data = get_CTJsonData(trial_id)
        trial.name = data["outcome_measures"][0]["name"] 
        trial.id = data["nct_id"]
        return trial
            
            
            
 #testing
#trial = get_trial('NCT02928224')
#locations = trial.locations(trial.id)
#print("Trial Name " + trial.name)
#print('num of of locs: ' +  str(len(trial.locations)))

#for location in locations: 
#        print(location.site_name + " " 
#        + location.city + " " 
#        + location.state_province + " " 
#        + location.lat + " " 
#        + location.lon)
        
     