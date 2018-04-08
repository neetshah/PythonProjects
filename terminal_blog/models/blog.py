import uuid

from terminal_blog.database import Database
from terminal_blog.models.post import Post
import datetime

class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date (DDMMYYYY) , or leave blank for today's date: ")
        post = Post(self.id, title, content, self.author, date=datetime.datetime.strptime(date, "%d%m%Y"))

    def get_posts(self):
        Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert('blogs', data=self.json())

    def json(self):
        return {self.author, self.title, self.description, self.id}

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one('blogs', {'id': id})
        return cls(blog_data['author'], blog_data['title'], blog_data['description'], blog_data['id'])