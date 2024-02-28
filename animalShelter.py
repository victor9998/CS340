from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'aacuser'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30528
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connection Successful") # Shows that the connection was successul

# Method that implements the C in CRUD (create).
    def create(self, data):
        if data is not None: 
            self.database.animals.insert_one(data)  # data should be dictionary
            return True # Returns true if animal was successfully added
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
#Method that implements the R in CRUD (read).
    def read (self,data):
        if data is not None:
            result = self.database.animals.find(data)
            return result # Returns the data that matches
        
        else:
            raise Exception("Nothing to search, because data parameter is empty")
            
#Method that implements the U in CRUD (update).
    def update (self,data,newData):
        if data is not None and newData is not None:
            result = self.database.animals.update_many(data, {'$set': newData})
            return result.modified_count # Returns the numer of objects modified in the collection
        
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            
#Method that implements the D in CRUD(delete).
    def delete (self,data):
        if data is not None:
            result = self.database.animals.delete_many(data)
            return result.deleted_count # Returns the numer of objects modified in the collection
        
        else:
            raise Exception("Nothing to delete, because data parameter is empty")