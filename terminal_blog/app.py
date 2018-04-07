__author__ = 'shahn17'

from database import Database
from models.post import Post

Database.initialize()

post = Post("123", "Another Great Post", "Sample Content", "Neet")

post.save_to_mongo()