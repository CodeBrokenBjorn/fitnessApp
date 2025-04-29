import tkinter as tk
from tkinter import messagebox
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app import app  # Now you can import app

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness App")
        self.root.geometry("400x300")


        #Add buttons for different functionalities
        tk.Button(self.root, text="Add Data", command=self.add_data_window).pack(pady=10)
        # tk.Button(self.root, text="Delete Data", command=self.delete_data_window).pack(pady=10)
        # tk.Button(self.root, text="Update Data", command=self.update_data_).pack(pady=10)
        # tk.Button(self.root, text="Retrieve Data", command=self.retrieve_data).pack(pady=10)
    def add_data_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Data")
        add_window.geometry("300x200")

        tk.Label(add_window, text="ID").pack(pady=5)
        self.add_id_entry = tk.Entry(add_window)
        self.add_id_entry.pack(pady=5)
        
        tk.Label(add_window, text="Name").pack(pady=5)
        self.add_name_entry = tk.Entry(add_window)
        self.add_name_entry.pack(pady=5)

        tk.Label(add_window, text="Age").pack(pady=5)
        self.add_age_entry = tk.Entry(add_window)
        self.add_age_entry.pack(pady=5)

        tk.Label(add_window, text="City").pack(pady=5)
        self.add_city_entry = tk.Entry(add_window)
        self.add_city_entry.pack(pady=5)

        def submit_add_data():
            data = {
                "id": self.add_id_entry.get(),
                "name": self.add_name_entry.get(),
                "age": self.add_age_entry.get(),
                "city": self.add_city_entry.get()
            }
        #tries establish connection to the server and send data
            try:
                response = requests.post("http://127.0.0.1:5000/data/add", json=data)
                if response.status_code == 201:
                    messagebox.showinfo("Success", "Data added successfully!")
                else:
                    messagebox.showerror("Error", response.json().get("error", "Failed to add data"))
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"Failed to connect to server: {e}")
            add_window.destroy()
        tk.Button(add_window, text="Submit", command=submit_add_data).pack(pady=10)
def run_flask():
    app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
    # This code creates a GUI for a fitness app using Tkinter. It includes buttons for adding, deleting, updating, and retrieving data. The add_data_window method creates a new window for adding data with fields for ID, name, age, and city. When the user submits the data, it sends a POST request to the server and displays success or error messages based on the response.
    # The GUI is initialized and run in the main block.