import requests
import json
import pandas as pd

#token of facebook account of Qutbaddin kohi
token = "EAABnrF3ih88BAPP15jyL6BBSzzsypim5FoigDSpWLPDDEt6IF7KERcWfZClAEH6xUO0XXetnmGQuaDJaXBW3RwOLahU4qiuMYZCDnf7ntktpAZBEY5ngmdV4XpGTzCBS5xXUx7tRzNEyZC0XQOSR4kj4V6EAo5WGUAOQNJqdz7AzKAfow8ZBZArfnUZBLT6y6PMxD5xYkZBQqQZDZD"


def req_facebook(req):
    r = requests.get("https://graph.facebook.com/v9.0/" + req, {'access_token': token})
    return r

#req for my facebook page
#req ="271358766927222?fields=posts{comments.limit(0).summary(true),likes.limit(0).summary(true),message,created_time}"

#request for facebook account
reqzaini ="me?fields=posts{comments.limit(0).summary(true),like.limit(0).summary(true),message,created_time,location}"
results=req_facebook(reqzaini).json()

data = []

results = results['posts']

while True:
    try:
        #time.sleep(random.randint(2, 5))
        data.extend(results['data'])
        r = requests.get(results['paging']['next'])
        results = r.json()
        
    except:
        print('done')
        break

#pickle.dump(data, open("zaini_data.pkl", "w"))
#loaded_data = pickle.load(file=open("zaini_data.pkl"))

with open('zaini_data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
    

