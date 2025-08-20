from services.dal.DBconnection import MongoConnector
from entities.solder import Soldier


class DataLoader:
    def __init__(self):
        self.connector = MongoConnector()

    def get_all_soldiers(self, collection = "soldier_details"):
        db = self.connector.get_connection()
        collection = db[collection]
        rows = list(collection.find({}))
        self.connector.close_connection()
        return rows

    def insert_soldier(self, ID, first_name, last_name, phone_number, rank, collection = "soldier_details"):
        soldier = Soldier(ID, first_name, last_name, phone_number, rank)
        db = self.connector.get_connection()
        collection = db[collection]
        result = collection.find({'ID': ID})
        if list(result):
            self.connector.close_connection()
            return {'msg': f"the ID: {ID} already exist."}

        result = collection.insert_one(document=soldier.to_dict())
        if result.inserted_id:
            self.connector.close_connection()
            return {"msg", f"inserted successfully. _id: {result.inserted_id}"}
        self.connector.close_connection()
        return {"msg": "there is a problem in the insertion"}

    def update_soldier(self, ID, field, value, collection = "soldier_details"):
        db = self.connector.get_connection()
        collection = db[collection]
        result = collection.update_one(
            {"ID": ID},
            {"$set": {field: value}}
        )

        if result.matched_count:
            self.connector.close_connection()
            return {'msg': f"the ID: {ID} was successfully updated."}
        self.connector.close_connection()
        return {"msg": f"there is no document with ID: {ID}."}

    def delete_soldier(self, ID, collection = "soldier_details"):
        db = self.connector.get_connection()
        collection = db[collection]
        result = collection.delete_one({'ID': ID})
        if result.deleted_count:
            self.connector.close_connection()
            return {'msg': f"the ID: {ID} was successfully deleted."}
        self.connector.close_connection()
        return {"msg": f"The document with ID: {ID} was not found."}
