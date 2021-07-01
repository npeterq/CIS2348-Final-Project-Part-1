"Peter Nguyen"
"6/20/2021"
"CIS2348"
"1860823"
"Final Project Part 1"

# Importing in csv and date &time
import csv
from datetime import datetime

# This is where the input csv files will be read
from typing import Dict, Any

if __name__ == '__main__':
    items: Dict[str, Dict[Any, Any]] = {}
    # These files are the inputs so we can create an output based on them
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    manufacturer = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = manufacturer.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

# Class for output, this is where files will be created and the csv files will be imported
class output:

    # List of the items
    def __init__(self, item_list):
        self.item_list = item_list

    # FullInventory.csv, this is where fullinventory will be created and sorted.
    def full_inv(self):
        # Now creating the file.
        with open('FullInventory.csv', 'w') as file:
            items = self.item_list
            # Sorting out manufacturer
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            # Identifying the things that will be written in the file.
            for item in keys:
                id = item
                manufacturer = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                # This is when the id, manufacturer, item type, price, service date, and damaged will be written in order.
                file.write('{},{},{},{},{},{}\n'.format(id, manufacturer, item_type, price, service_date, damaged))

    # This is where the item type inventory file will be created and sorted.
    def type_inv(self):
        items = self.item_list
        types = []
        # Sorting out the items
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        # Where the files will be named and written.
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open(file_name, 'w') as file:
                for item in keys:
                    # Listing out the things needed to write in the file
                    id = item
                    manufacturer = items[item]['manufacturer']
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']
                    if type == item_type:
                        # Where the csv file will bne written
                        file.write('{},{},{},{},{}\n'.format(id, manufacturer, price, service_date, damaged))
    # This is where the PastServiceDateInventory.csv will be created based if the date is passed the day or not.
    def past_date(self):
        items = self.item_list
        # Sorting to see if the date is passed or not
        date = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date(),
                      reverse=True)
        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in date:
                id = item
                manufacturer = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                # expired will mean that the dates expired after the current date the program is ran on
                expired = service_expiration < today
                # If any dates are expired it will be written in the csv file
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, manufacturer, item_type, price, service_date, damaged))

    # This is where the d. DamagedInventory.csv will be created based if the item was damaged or not.
    def damaged_inv(self):
        items = self.item_list
        # Sorting based on price from most expensive to least expensive
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manufacturer = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    # Writing in the csv based on if it was damaged and in order by price
                    file.write('{},{},{},{},{}\n'.format(id, manufacturer, item_type, price, service_date))



#Final step is call in the outputs
output = output(items)
output.full_inv()
output.type_inv()
output.past_date()
output.damaged_inv()
