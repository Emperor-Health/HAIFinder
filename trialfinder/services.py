import json
import urllib.request
import ssl 
from collections import namedtuple

#returns the json data
def get_CTJsonData():
    context = ssl._create_unverified_context()   
    url1 = "https://clinicaltrialsapi.cancer.gov/v1/clinical-trials" 
    with urllib.request.urlopen(url1 , 
        context=context) as url:
            data = json.loads(url.read().decode()) 
            return data

class Trial:
       def __init__(self, nct_id, brief_name, current_trial_status):
        self.nct_id = nct_id
        self.brief_title = brief_name
        self.current_trial_status = current_trial_status
    
         
def get_trials():
        trials = []
        data = get_CTJsonData()
            #print(len(data["sites"]));
        for x in range(0, len(data["trials"])):
            nct_idr = data["trials"][x]["nct_id"]
            brief_titler = data["trials"][x]["brief_title"]
            current_trial_statusr = data["trials"][x]["current_trial_status"]
            print("nci id: " + nct_idr)
            t = Trial(nct_idr, brief_titler, current_trial_statusr)
           
            trials.append(t)
            #print(len(locations))
        return trials
  
   
 
            
            
 #testing 
trials = []
trials = get_trials() 

for trial in trials: 
        print(trial.nct_id) 
        print(trial.brief_title)  
        print(trial.current_trial_status) 
         
        
     
