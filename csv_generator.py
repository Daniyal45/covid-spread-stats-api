import requests
import csv
import json
import datetime
import pandas as pd
from predict import predict

def generate_csv(country):
  URL = "https://corona-api.com/countries/"+country+"?include=timeline"
  r = requests.get(url = URL)
  df = pd.DataFrame(list())
  df.to_csv('data_file.csv')
  response = r.json()
  data = response.items()
  for key, value in data:
      if key == 'data':
        new_data = value.items()
        for key, value in new_data:
            if key == 'timeline':
                raw_data_for_csv = value
  raw_data_for_csv.reverse()
  data_file = open('data_file.csv', 'w', newline='')
  csv_writer = csv.writer(data_file)
  count = 0
  for index, list_item in enumerate(raw_data_for_csv):
      list_item['Date'] = datetime.datetime.strptime(list_item['date'], "%Y-%m-%d").strftime("%m/%d/%Y")
      list_item['Total_Cases'] = list_item['confirmed']
      list_item['New_Cases'] = list_item['new_confirmed']
      list_item['Total_Deaths'] = list_item['deaths']
      list_item['New_Deaths'] = list_item['new_deaths']
      del(list_item['updated_at'])
      del(list_item['date'])
      del(list_item['deaths'])
      del(list_item['confirmed'])
      del(list_item['recovered'])
      del(list_item['new_confirmed'])
      del(list_item['new_recovered'])
      del(list_item['new_deaths'])
      del(list_item['active'])

  for data in raw_data_for_csv:
      if count == 0:
          header = data.keys()
          csv_writer.writerow(header)
          count = count + 1
      csv_writer.writerow(data.values())
  data_file.close()

  return(predict())