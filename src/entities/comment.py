class Comment:

    def __init__(self, author, avatar, date, content):
        self.author = author
        self.avatar = avatar
        self.date = date
        self.content = content

    def to_dict(self):
        return {
            "author": self.author,
            "avatar": self.avatar,
            "date": self.date,
            "content": self.content
        }
    