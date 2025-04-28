from flask import Flask, jsonify, request
from data.data_store import data_store
thingsNeeded = [
    "id",
    "name",
    "age",
    "city"
]

def add_data():
    new_data = request.get_json()
    if not new_data:
        return jsonify({"error": "No data provided"}), 400
    for field in thingsNeeded:
        if field not in new_data:
            return jsonify({"error": f"Missing field: {field}"}), 400
    for item in data_store:
        if item["id"] == new_data["id"]:
            return jsonify({"error": "ID already exists"}), 400
        
    data_store.append(new_data)
    return jsonify({"message": "Data added successfully!", "data": new_data}), 201