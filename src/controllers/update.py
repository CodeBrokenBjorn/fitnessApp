
from flask import Flask, jsonify, request
from data.data_store import data_store
list_that_requires_update = [
    "id",
    "name",
    "age",
    "city"
]

def update_data(data_id):
    updated_data = request.get_json()
    if not updated_data:
        return jsonify({"error": "No data provided"}), 400
    for field in list_that_requires_update:
        if field not in updated_data:
            return jsonify({"error": f"Missing field: {field}"}), 400
    for item in data_store:
        if item["id"] == data_id:
            item.update(updated_data)
            return jsonify({"message": "Data updated successfully!", "data": item}), 200
    return jsonify({"error": "Data not found"}), 404
# This code defines a function `update_data` that updates an entry in a data store based on the provided ID and new data. It checks for missing fields and returns appropriate error messages if the data is not found or if required fields are missing.    
