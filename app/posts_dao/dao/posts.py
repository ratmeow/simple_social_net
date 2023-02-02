import json
from app.posts_dao.dao.post import Post


class Posts:
    def __init__(self, path):
        self.path = path
        self.posts = []

    def load_posts(self):
        self.posts = []
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for elem in data:
            post = Post(elem['poster_name'], elem['poster_avatar'], elem['pic'], elem['content'], elem['views_count'],
                        elem['likes_count'], elem['pk'])
            self.posts.append(post)

    def get_all(self):
        return self.posts

    def get_post_by_id(self, pk):
        for post in self.posts:
            if post.pk == pk:
                return post
        return False

    def get_posts_by_keyword(self, keyword):
        need_posts = []
        for post in self.posts:
            if keyword.lower() in post.content.lower():
                need_posts.append(post)
        return need_posts

    def get_post_by_name(self, name):
        for post in self.posts:
            if post.name.lower() == name.lower():
                return post
        return False
