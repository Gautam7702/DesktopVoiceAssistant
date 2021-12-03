
from apiclient.discovery import build
api_key  = "AIzaSyBnHr12yY-ZIYLdwdjm1XVkGRMP9b1ih0w"
youtube  = build('youtube','v3',developerKey=api_key)
def search_vid(query):
    req = youtube.search().list(q=query, part = 'snippet', type = 'video')
    res  =req.execute()
    return res['items'][0]['id']['videoId'],res['items'][0]['snippet']['title']