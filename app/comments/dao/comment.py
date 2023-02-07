class Comment:
    def __init__(self, name, content, pk):
        self.name = name
        self.content = content
        self.pk = pk

    def __repr__(self):
        return f"{self.name}"
