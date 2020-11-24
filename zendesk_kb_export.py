import datetime
import json 
import requests

credentials = 'kevin.odea2@logmein.com', 'G^^00zbx'
zendesk = 'https://logmeindev.zendesk.com'
language = 'en-US'

kb_upload = {
    "title": 1,
    "answer": 2
}


# date = datetime.date.today()
# backup_path = os.path.join(str(date), language)
# if not os.path.exists(backup_path):
#     os.makedirs(backup_path)

# log = []

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
        url = 'https://kevinddemo.nanorep.co/api/kb/v1/import?account=kevinddemo&kb=English&apiKey=2265560f-14ab-4aad-8be0-66966d9f8b3e&isPreview=false&action=import'
        data = '[' + kb_upload_json + ']'
        headers = {"content-type": "application/json"}
        x = requests.post(url, data=data, headers=headers)
        response = x.status_code
        print(response)

    endpoint = data['next_page']

# with open(os.path.join(backup_path, '_log.csv'), mode='wt', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow( ('File', 'Title', 'Author ID') )
#     for article in log:
#         writer.writerow(article)


# def _createnewarticle():
#     url = 'https://kevinddemo.nanorep.co/api/kb/v1/import?account=kevinddemo&kb=English&apiKey=2265560f-14ab-4aad-8be0-66966d9f8b3e&isPreview=false&action=import'
#     data = '[' + kb_upload_json + ']'
#     headers = {"content-type": "application/json"}
#     x = requests.post(url, data=data, headers=headers)
#     response = x.status_code
#     print(response)
