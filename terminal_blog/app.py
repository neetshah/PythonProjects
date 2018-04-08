from terminal_blog.database import Database
from terminal_blog.models.post import Post

__author__ = 'shahn17'

Database.initialize()

post = Post("123", "Another Great Post", "Sample Content", "Neet")

post.save_to_mongo()