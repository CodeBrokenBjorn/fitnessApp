from flask import Flask
import pandas as pd
import numpy as np
import controllers.retrieve as retrieve
import controllers.add as add
import controllers.delete as delete
import controllers.update as update

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

# Route to retrieve data by ID
@app.route('/data/<int:data_id>')
def get_data(data_id):
    # Pass the data_id to the retrieve function
    return retrieve.get_data_by_id(data_id)

@app.route('/data/add', methods=['POST'])
def add_new_data():
    # Call the add_data function from the add module
    return add.add_data()
@app.route('/data/delete/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    return delete.delete_data(data_id)
# Route to retrieve all data
@app.route('/data')
def get_all_data():
    # Call the retrieve function to get all data
    return retrieve.get_all_data()
def update_data(data_id):
    # Call the update function to update data by ID
    return update.update_data(data_id)
@app.route('/data/update/<int:data_id>', methods=['PUT'])
def update_data_route(data_id):
    return update.update_data(data_id)



def data():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'A': np.random.rand(10),
        'B': np.random.rand(10)
    })
    return df.to_json()

if __name__ == '__main__':
    app.run(debug=True)

