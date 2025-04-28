from flask import Flask, request, jsonify
from data.data_store import data_store
def delete_data( data_id):
    for item in data_store:
        if item["id"] == data_id:
            data_store.remove(item)
            return jsonify({"message": "Data deleted successfully"}), 200
    return jsonify({"error": "Data not found"}), 404