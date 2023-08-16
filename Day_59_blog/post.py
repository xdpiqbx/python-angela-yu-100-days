import requests
ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"

class Post:
    def __init__(self):
        self.posts = requests.get(ENDPOINT).json()

    def get_posts(self):
        return self.posts

    def get_post_by_id(self, post_id):
        return next((post for post in self.posts if post.get('id') == post_id), dict())
