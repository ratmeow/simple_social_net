import json
from app.comments.dao.comment import Comment


class Comments:
    def __init__(self, path, post_id):
        self.path = path
        self.comments = []
        self.post_id = post_id

    def load_comments(self):
        self.comments = []
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for elem in data:
            if elem['post_id'] == self.post_id:
                comm = Comment(elem['commenter_name'], elem['comment'], elem['pk'])
                self.comments.append(comm)

    def get_all(self):
        return self.comments

    def get_comment_by_id(self, pk):
        for comm in self.comments:
            if comm.pk == pk:
                return comm
        return False

    def get_comments_by_keyword(self, keyword):
        need_comments = []
        for comment in self.comment:
            if keyword.lower() in comment.content.lower():
                need_comments.append(comment)
        return need_comments

    def get_comment_by_name(self, name):
        for comment in self.comments:
            if comment.name.lower() == name.lower():
                return comment
        return False
