from key import api_key
from apiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=api_key)

def search_vid(query):
    req = youtube.search().list(q=query, part='snippet', type='video')
    res = req.execute()
    return res['items'][0]['id']['videoId'], res['items'][0]['snippet']['title']
