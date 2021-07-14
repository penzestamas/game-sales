import csv
import sys


def get_dicts_from_csv(file_name):
    csv_list = []

    try:
        file = open(file_name, 'r')
        try:
            file_content = csv.DictReader(file)
            for row in file_content:
                csv_list.append(row)
        finally:
            file.close()
    except OSError:
        print('Hiba a fájl kezelése közben!')
        sys.exit()
    else:
        return tuple(csv_list)


def write_dicts_to_csv(file_name, list_of_sales):
    try:
        csvfile = open(file_name, 'w')
        try:
            fieldnames = tuple(list_of_sales[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()

            for sale in list_of_sales:
                writer.writerow(sale)
        finally:
            csvfile.close()
    except OSError:
        return 'Hiba a fájl létrehozása közben!'
    else:
        return 'Fájl létrehozva!'
