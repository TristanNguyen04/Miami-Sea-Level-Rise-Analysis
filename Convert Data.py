import csv
with open('Miami_mean_sea_level_dataset.csv', mode ='r', encoding='utf-8') as file:
  csvFile = csv.DictReader(file)
  for line in csvFile:
    print(line["mean_sea_level_rise"], end =',')