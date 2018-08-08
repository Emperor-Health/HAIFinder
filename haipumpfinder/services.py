import json
import urllib.request
import ssl 
from collections import namedtuple

single_trial_url = "https://clinicaltrialsapi.cancer.gov/v1/clinical-trial/"
#returns the json data
def get_CTJsonDataForSingleTrial(trial_id):
    context = ssl._create_unverified_context()   
    url1 = single_trial_url + trial_id  
    with urllib.request.urlopen(url1 , 
        context=context) as url:
            data = json.loads(url.read().decode())
            return data


class TrialLocation:
   def __init__(self, idr, site_name, contact_name, contact_email, contact_phone, recruitment_status, recruitment_status_date, address_1, address_2, city, state, postal_code, lat, lon):
        self.nct_id = idr
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


class Trial(object):    
    def __init__(self, trial_id):
        self.trial_id = trial_id
        data = get_CTJsonDataForSingleTrial(trial_id)
        self.acronym = data["acronym"]
        self.brief_title = data["brief_title"]
        self.official_title = data["official_title"] 
        self.current_trial_status = data["current_trial_status"]
        self.phase = data["phase"]["phase"] 
        ##get a default name
        if self.acronym is not None:
            self.name = self.acronym
        elif self.brief_title is not None:
            self.name = self.brief_title
        else:
            self.name = self.official_title
        
        ##get gender
        self.gender = data["eligibility"]["structured"]["gender"]
        if self.gender == "BOTH":
            #print("Tests BOTH!")
            self.gender = "Male & Female" 
     
        self.gender = data["eligibility"]["structured"]["gender"]
        self.age_range = str(data["eligibility"]["structured"]["min_age_number"]) + "-" + str(data["eligibility"]["structured"]["max_age_number"])[0:2]
        self.CTGovURL = single_trial_url + trial_id
       
        self.locations = get_locations(data["sites"], self.trial_id) 
        self.unique_states = get_unique_state_locations(self.locations)





def get_unique_state_locations(locations):
        unique_states = set()
        for x in locations:
                if x.state not in unique_states: 
                    if x.state is not None:
                        #print("unique " + x.state) 
                        unique_states.add(x.state)
        return unique_states
     
        


def get_locations(sites_json, trial_id):
        locations = [] 
            #print(len(data["sites"]));
        for x in range(0, len(sites_json)):
            idr = trial_id
            namer = sites_json[x]["org_name"]
            contact_namer = sites_json[x]["contact_name"]
            contact_emailr = sites_json[x]["contact_email"]
            contact_phoner = sites_json[x]["contact_phone"]
            recruitment_statusr = sites_json[x]["recruitment_status"]
            recruitment_status_dater = sites_json[x]["recruitment_status_date"]
            address_1r = sites_json[x]["org_address_line_1"]
            address_2r = sites_json[x]["org_address_line_2"]
            cityr = sites_json[x]["org_city"]
            state_provincer = sites_json[x]["org_state_or_province"]
            postal_coder = sites_json[x]["org_postal_code"]
            try:
            #print( data["sites"][x]["org_coordinates"]["lat"])
                latr = str(sites_json[x]["org_coordinates"]["lat"])
            except KeyError:
                latr = 'null'
            try:
                #print(data["sites"][x]["org_coordinates"]["lon"])
                lonr = str(sites_json[x]["org_coordinates"]["lon"])
            except KeyError:
                lonr = 'null'

            t = TrialLocation(idr, namer, contact_namer, contact_emailr, contact_phoner, recruitment_statusr, recruitment_status_dater, address_1r, address_2r, cityr, state_provincer, postal_coder, latr, lonr)
            #print("City: " + t.city)
            locations.append(t)
            #print(len(locations))
        return locations
  
   
 
            
            
 #testing
trial = Trial("NCT02928224")  
locations = []
locations = trial.locations 
us = trial.unique_states
#print("Trial Name " + trial.name)
#print("URL " + trial.CTGovURL)
#print("Gender " + trial.gender)
#print("age range " + trial.age_range)
#print('num of of locs: ' + len(locations))

#for state in us: 
       #print(state) 
#        + location.city + " " 
#        + location.state_province + " " 
#        + location.lat + " " 
#        + location.lon)
        
     
