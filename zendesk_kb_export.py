import json 
import requests

credentials = <your email>, <your password>
zendesk = 'https://<your subdomain>.zendesk.com'
language = 'en-US'

kb_upload = {
    "title": 1,
    "answer": 2
}

endpoint = zendesk + '/api/v2/help_center/{locale}/articles.json'.format(locale=language.lower())
while endpoint:
    response = requests.get(endpoint, auth=credentials)
    if response.status_code != 200:
        print('Failed to retrieve articles with error {}'.format(response.status_code))
        exit()
    data = response.json()
    
    for article in data['articles']:
        if article['body'] is None:
            continue
        kb_upload["title"] = article['title']
        kb_upload["answer"] = article['body']
        kb_upload_json = json.dumps(kb_upload)
        url = 'https://kevinddemo.nanorep.co/api/kb/v1/import?account={}&kb={}&apiKey={}&isPreview=false&action=import'
        data = '[' + kb_upload_json + ']'
        headers = {"content-type": "application/json"}
        x = requests.post(url, data=data, headers=headers)
        response = x.status_code
        print(response)

    endpoint = data['next_page']
