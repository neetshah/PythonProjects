__author__ = 'shahn17'

from ..database import Database

class Post(object):

    def __init__(self, blog_id, title, content, date, author, id):
        self.blog_id = blog_id
        self.title = "Title"
        self.content = "Content"
        self.author = "Neet"
        self.created_date = date
        self.id = id

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())
            
    def json(self):
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            'created_date':self.created_date
        }

    @staticmethod
    def from_mongo(id):
        return Database.find_one('posts', {'id': id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find('posts', {'blog_id': id})]

