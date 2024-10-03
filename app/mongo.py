from flask_pymongo import PyMongo

mongo = PyMongo()

def init_mongo(app):
    mongo.init_app(app)
    
def get_next_sequence_value(sequence_name):
    """Gets the next value of a sequence (auto-increment) from the counters collection."""
    sequence_document = mongo.db.counters.find_one_and_update(
        {'_id': sequence_name},
        {'$inc': {'sequence_value': 1}},  # Increment the sequence value by 1
        return_document=True,  # Return the updated document
        upsert=True  # If the sequence doesn't exist, create it
    )
    
    return sequence_document['sequence_value']