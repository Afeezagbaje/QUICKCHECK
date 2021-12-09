import requests


class HackerNewsApi:
    def __init__(self, item, **params):
        self.item = item
        base_url = "https://hacker-news.firebaseio.com/v0"
        self.news_url = f"{base_url}/{self.item}.json"
        self.item_url = f"{base_url}/item"

    def get_all_stories(self):
        res = requests.get(self.news_url)
        if res.status_code == 200:
            return res.json()
        else:
            return {"Status Code": res.status_code}

    def get_a_story(self, story_id):
        story = f"{self.item_url}/{story_id}.json"
        res = requests.get(story)
        if res.status_code == 200:
            return res.json()
        else:
            return {"Status Code": res.status_code}

    def getcomments(self, commentId):
        request = requests.get(f"{self.item_url}{commentId}.json")
        res = requests.get(request)
        if res.status_code == 200:
            return res.json()
        else:
            return {"Status": res.status_code}


# hack = HackerNewsApi("topstories")
# print(hack.get_all_stories())
# print(hack.get_a_story(29360801))
