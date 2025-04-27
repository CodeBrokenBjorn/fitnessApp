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


def get_all_data():
    return jsonify(data_store)

def get_data_by_id(data_id):
    print(f"Retrieving data for ID: {data_id}")
    # Check if the data_id is valid
    for item in data_store:
        print(f"Checking item: {item}")
        if item["id"] == data_id:
            return jsonify(item)
    print(f"Data not found for ID: {data_id}")
    return jsonify({"error": "Data not found"}), 404
