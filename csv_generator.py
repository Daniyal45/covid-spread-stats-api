# Python program to convert
# JSON file to CSV
import json
import csv
import pandas as pd

dummyData = {
  "Product": {
    "0": "Desktop Computer",
    "1": "Tablet",
    "2": "Printer",
    "3": "Laptop"
  },
  "Price": {
    "0": 700,
    "1": 250,
    "2": 100,
    "3": 1200
  }
}
dummyData = json.dumps(dummyData)
df = pd.read_json(dummyData)
df.to_csv('data_file.csv')
