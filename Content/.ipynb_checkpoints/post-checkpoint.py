from topic import Topic

class Post(Topic):
    def __init__(self, topic, detail, user):
        Topic.__init__(self, topic, user='')
        self.detail = detail
        self.user = user # anonymous??
        self.comments = []
        self.like = 0
    def add_comment(self, comment):
        self.comments.append(comment)
    def add_like(self):
        self.like += 1
    def check(self):
        return f'This post has {self.like} like and {len(self.comments)} comments.'
    def show(self):
        print(f'Topic: {self.tname}')
        print(self.detail)
        print('-----')
        if self.comments:
            print('Comments: ')
            for i in self.comments:
                print(i)
        else:
            print('[Currently no comment.]')