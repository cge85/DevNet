import csv

with open("routerlist.csv") as fl:
    csv_list = csv.reader(fl)
    # Loop over each row in csv and leverage the data in code
    for row in csv_list:
        device = row[0]
        location = row[2]
        ip = row[1]
        print(f"{device} is in {location} and has IP {ip}.")