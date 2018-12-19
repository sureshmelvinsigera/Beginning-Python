'''
Make a Python script which adds comments to your any of the post on your timeline.
The script will qualify as a bomb if it is able to comment 50 times on a single post.
'''

import requests
import json

#replace with your access token, to be found at https://developers.facebook.com/tools/explorer
accesstoken = ''

query = 'SELECT post_id , created_time FROM stream where source_id = me()'
d = { 'access_token': accesstoken, 'q':query}

base_url = 'https://graph.facebook.com'
r = requests.get(base_url + "/fql", params=d)
result = json.loads(r.text)
posts = result['data']
post1 = posts[0]

comments_url = base_url + '/{}/comments'.format(post1['post_id'])

count =1
for i in range(50):
    msg = {'access_token': accesstoken, 'message': 'Bomb' + str(count)}
    requests.post(comments_url, data = msg)
    count+=1
    print count

