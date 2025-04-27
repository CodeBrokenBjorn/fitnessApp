from flask import Flask, jsonify, request

data_store = [
    {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 25,
        "city": "Los Angeles"
    },
    {
        "id": 3,
        "name": "Sam Brown",
        "age": 22,
        "city": "Chicago"
    }
]

def add_data(new_data):

    new_data = request.get_json()
    if not new_data:
        return jsonify({"error": "No data provided"}), 400
    for item in data_store:
        if item["id"] == new_data["id"]:
            return jsonify({"error": "ID already exists"}), 400
    data_store.append(new_data)
    return jsonify(new_data), 201
