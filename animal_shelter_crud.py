from pymongo import MongoClient

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # MongoDB connection string with provided host, port, and user credentials
        self.client = MongoClient(f'mongodb://root:JmZM4AVcSG@nv-desktop-services.apporto.com:31871')
        self.database = self.client["AAC"]
        self.collection = self.database["animals"]

    def create(self, data):
        """ Method to insert a new document into the collection """
        if data is not None:
            return self.collection.insert_one(data).acknowledged
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, criteria=None):
        """ Method to query and return documents from the collection """
        if criteria is None:
            criteria = {}
            return list(self.collection.find(criteria))
        else: 
            return self.collection.find(criteria,{'_id':0})
        
    def test_read(self):
        # Test to ensure that the read method works
        search_query = {'animal_type': 'Dog'}
        results = self.shelter.read(search_query)
        self.assertIsInstance(results, list, "Read method did not return a list")
        if results:
            self.assertIn('animal_type', results[0], "Record does not contain 'animal_type' key")
            
    def update(self, query, new_values):
        """
        Update documents in the collection based on a query.
        :param query: A dictionary specifying the query conditions
        :param new_values: A dictionary specifying the new values
        :return: A count of documents updated
        """
        update_result = self.collection.update_many(query, {'$set': new_values})
        return update_result.modified_count

    def delete(self, query):
        """
        Delete documents from the collection based on a query.
        :param query: A dictionary specifying the query conditions
        :return: A count of documents deleted
        """
        delete_result = self.collection.delete_many(query)
        return delete_result.deleted_count


