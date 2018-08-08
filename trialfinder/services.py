import json
import urllib.request
import ssl 
from collections import namedtuple
from haipumpfinder.services import TrialLocation, Trial, get_CTJsonDataForSingleTrial


ct_api_url = "https://clinicaltrialsapi.cancer.gov/v1/clinical-trials"
result_size = "100"
search_term = "colorectal"

#returns the json data
def get_CTJsonDataAllTrials(result_size, search_term):
    context = ssl._create_unverified_context()   
    url1 = ct_api_url + "?size=" + result_size + "&_fulltext=" + search_term
    with urllib.request.urlopen(url1 , 
        context=context) as url:
            data = json.loads(url.read().decode()) 
            return data

 
 


def get_trials():
        trials = []
        trials_jsondata = get_CTJsonDataAllTrials(result_size, search_term)
            #print(len(data["sites"]));
        for x in range(0, len(trials_jsondata["trials"])):
                #print(data)
            t = Trial(trials_jsondata["trials"][x]["nct_id"])
            trials.append(t)
            #print(len(locations))  
        return trials
  
   
 
            
            
 #testing

 

#for trial in get_trials(): 
#    print(trial.trial_id) 
#    print(trial.brief_title)  
#    print(trial.current_trial_status) 
#    print(trial.phase) 
    #t = Trial(trial.trial_id)

    #for location in t.locations:
       #print(location.site_name)
#        print(location.state)
        
        
     
