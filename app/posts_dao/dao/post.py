from app.comments.dao.comments import Comments


class Post:
    def __init__(self, name, avatar, pic, content, views, likes, pk):
        self.name = name
        self.avatar = avatar
        self.pic = pic
        self.content = content
        self.views = views
        self.likes = likes
        self.pk = pk
        self.short_descr = content[:30]
        comments = Comments('D:/skypro/coursework2_source/data/comments.json', pk)
        comments.load_comments()
        self.comments = comments.get_all()

    def __repr__(self):
        return f"{self.name}"
