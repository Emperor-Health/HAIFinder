import json
import urllib.request
import ssl 
from collections import namedtuple

#returns the json data
def get_CTJsonData():
    context = ssl._create_unverified_context()   
    url1 = "https://clinicaltrialsapi.cancer.gov/v1/clinical-trial/" 
    with urllib.request.urlopen(url1 , 
        context=context) as url:
            data = json.loads(url.read().decode())
            return data


     
def get_trials():
        trials = []
        data = get_CTJsonData()
            #print(len(data["sites"]));
        for x in range(0, len(data["trials"])):
            idr = data["nct_id"]
            print("trial id: " + idr)
            trials.append(idr)
            #print(len(locations))
        return trials
  
   
 
            
            
 #testing
#trial = Trial("NCT02928224") 
trials = []
trials = get_trials() 

for trial in trials: 
        print(trial.trial_id) 

         
        
     
