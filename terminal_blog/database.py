from pymongo import MongoClient

__author__ = 'shahn17'

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = []

    @staticmethod
    def initialize():
        client = MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data) 

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)
        
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)