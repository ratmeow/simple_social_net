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

    def __repr__(self):
        return f"{self.name}"
