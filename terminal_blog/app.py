__author__ = 'shahn17'

from terminal_blog.models.post import Post
from terminal_blog.models.database import Database

Database.initialize()

post = Post("123", "Another Great Post", "Sample Content", "Neet")

post.save_to_mongo()