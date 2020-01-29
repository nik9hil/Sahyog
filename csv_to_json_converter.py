import csv,json

csvFilePath = "ngo_data.csv"
jsonFilePath = "ngo_data.json"

csvfile = open('ngo_data.csv', 'r')
jsonfile = open('ngo_data.json', 'w')

fieldnames = ("Ngo Name","Mobile No","Email","City")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')