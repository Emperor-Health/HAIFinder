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
   def __init__(self, trial_id, site_name, contact_name, contact_email, contact_phone, recruitment_status, recruitment_status_date, address_1, address_2, city, state, postal_code, lat, lon):
        self.trial_id = trial_id
        self.site_name = site_name
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.recruitment_status = recruitment_status
        self.recruitment_status_date = recruitment_status_date
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.latitude = lat
        self.longitude = lon


class Trial:
    def __int__(self, trial_id):
        self.trial_id = trial_id
## creating static methods is bs
## need a class that can be instantiated based on 1 JSON query
    @staticmethod 
    def get_name(trial_id):
        data = get_CTJsonData(trial_id)
        if data["acronym"] is not None:
            result = data["acronym"]
        elif data["brief_title"] is not None:
            result = data["brief_title"]
        else: 
            result = data["official_title"]
       
        #print("name is " + result)
        return result
 
    @staticmethod
    def get_locations(trial_id):
        locations = []
        trial_idl = trial_id
        data = get_CTJsonData(trial_idl)
            #print(len(data["sites"]));
        for x in range(0, len(data["sites"])):
            idr = data["nct_id"]
            namer = data["sites"][x]["org_name"]
            contact_namer = data["sites"][x]["contact_name"]
            contact_emailr = data["sites"][x]["contact_email"]
            contact_phoner = data["sites"][x]["contact_phone"]
            recruitment_statusr = data["sites"][x]["recruitment_status"]
            recruitment_status_dater = data["sites"][x]["recruitment_status_date"]
            address_1r = data["sites"][x]["org_address_line_1"]
            address_2r = data["sites"][x]["org_address_line_2"]
            cityr = data["sites"][x]["org_city"]
            state_provincer = data["sites"][x]["org_state_or_province"]
            postal_coder = data["sites"][x]["org_postal_code"]
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

            t = TrialLocation(idr, namer, contact_namer, contact_emailr, contact_phoner, recruitment_statusr, recruitment_status_dater, address_1r, address_2r, cityr, state_provincer, postal_coder, latr, lonr)
            #print("City: " + t.city)
            locations.append(t)
            #print(len(locations))
        return locations
  
   

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
        
     