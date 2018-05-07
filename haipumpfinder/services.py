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


class Trial(object):    
    def __init__(self, trial_id):
        self.trial_id = trial_id
        data = get_CTJsonData(trial_id)
        self.acronym = data["acronym"]
        self.brief_title = data["brief_title"]
        self.official_title = data["official_title"]
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
            print("Tests BOTH!")
            self.gender = "Male & Female" 
     
        self.gender = data["eligibility"]["structured"]["gender"]
        self.age_range = str(data["eligibility"]["structured"]["min_age_number"]) + "-" + str(data["eligibility"]["structured"]["max_age_number"])[0:2]
        #self.locations = []
        self.CTGovURL = "https://clinicaltrialsapi.cancer.gov/v1/clinical-trial/" + trial_id
        
        
     
        
    
 
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
  
   
 
            
            
 #testing
trial = Trial("NCT02928224") 
#locations = []
#locations = trial.get_locations(trial.id)
print("Trial Name " + trial.name)
print("URL " + trial.CTGovURL)
print("Gender " + trial.gender)
print("age range " + trial.age_range)
#print('num of of locs: ' + len(locations))

#for location in locations: 
#        print(location.site_name + " " 
#        + location.city + " " 
#        + location.state_province + " " 
#        + location.lat + " " 
#        + location.lon)
        
     
