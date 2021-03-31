"""Clean original archive CSV files and save them to the data folder
"""
import csv

sources = ['global', 'country_specific', 'region_specific']

for key in sources:
    data_list = []
    with open('archive/{}.csv'.format(key), newline='') as archive_file:

        for row in csv.DictReader(archive_file):
            data_list.append(row)

    # Methods to process the data would be called on the data_list object here

    fieldnames = list(data_list[0])

    with open('data/{}.csv'.format(key), 'w', newline='') as data_file:
        writer = csv.DictWriter(data_file, fieldnames)

        writer.writeheader()
        writer.writerows(data_list)
